from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Task


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'birth_date']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'due_date', 'status', 'priority', 'project', 'assigned_to', 'category', 'tags']
#         widgets = {
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#             'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'status': forms.Select(attrs={'class': 'form-control'}),
#             'priority': forms.Select(attrs={'class': 'form-control'}),
#             'project': forms.TextInput(attrs={'class': 'form-control'}),
#             'assigned_to': forms.Select(attrs={'class': 'form-control'}),
#             'category': forms.Select(attrs={'class': 'form-control'}),
#             'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
#         }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'priority', 'project', 'assigned_to', 'category', 'tags']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'tags': forms.CheckboxSelectMultiple(),
        }