from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, UserProfileForm, TaskForm
from .models import UserProfile, Task
import datetime
from django.urls import reverse_lazy

def landing_page(request):
    return render(request, 'landing.html')

# User Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('profile')
        else:
            for field in form.errors:
                error_message = form.errors[field].as_text()
                messages.warning(request, f"{field.capitalize()}: {error_message}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Profile view
@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Count tasks based on their status
    pending_tasks_count = request.user.task_set.filter(status='Pending').count()
    completed_tasks_count = request.user.task_set.filter(status='Completed').count()
    overdue_tasks_count = request.user.task_set.filter(due_date__lt=datetime.date.today(), status='Pending').count()
    recent_tasks = request.user.task_set.order_by('-due_date')[:5]

    context = {
        'user': request.user,
        'user_profile': user_profile,
        'pending_tasks_count': pending_tasks_count,
        'completed_tasks_count': completed_tasks_count,
        'overdue_tasks_count': overdue_tasks_count,
        'recent_tasks': recent_tasks,
    }
    return render(request, 'registration/profile.html', context)

# Profile Editing View
@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
        else:
            messages.warning(request, "Please correct the errors below.")
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'registration/edit_profile.html', {'form': form})

# Custom Login View
class CustomLoginView(LoginView):
    def form_valid(self, form):
        messages.success(self.request, f'Logged in successfully as {form.get_user().username}!')
        return super().form_valid(form)

# Logout View
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

# Task List View
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-due_date')

# Task Detail View
class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_object(self, queryset=None):
        return get_object_or_404(Task, id=self.kwargs['pk'], user=self.request.user)

# Task Create view
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user who creates the task
        return super().form_valid(form)

# Task Update View
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Task, id=self.kwargs['pk'], user=self.request.user)

# Task Delete View
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Task, id=self.kwargs['pk'], user=self.request.user)
    



