# Task Management System

A web-based Task Management System built with Django that allows users to manage tasks, organize them into categories, assign due dates and priorities, and filter/search for tasks. The application provides user authentication and role-based access control, making it an efficient tool for individual and team task management.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [License](#license)
- [Contributing](#contributing)

## Features

- **User Authentication**: Registration, login, and logout features for users.
- **User Profiles**: Users can update their profile with additional information.
- **CRUD Operations**: Create, read, update, and delete tasks.
- **Task Categories**: Organize tasks into categories and add tags.
- **Due Dates & Reminders**: Set due dates and reminders for tasks.
- **Task Filtering & Searching**: Search and filter tasks based on categories, tags, status, and due dates.
- **Dashboard**: Provides an overview of all tasks upon user login.
- **Role-based Access Control**: Assign roles to users to control access to different features.

## Installation

### Prerequisites

- Python 3.8+
- Django 4.x
- PostgreSQL
- Bootstrap 5.x
- Tailwind CSS (optional for styling)
  
### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/task-management-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd task-management-system
    ```

3. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    venv\Scripts\activate     # For Windows
    ```

4. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Create a `.env` file in the root directory and configure your environment variables (PostgreSQL database, secret key, etc.):

    ```bash
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgres://user:password@localhost:5432/task_db
    ```

6. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

8. Start the development server:

    ```bash
    python manage.py runserver
    ```

9. Visit `http://localhost:8000` to access the application.

## Usage

### User Authentication

- Register a new account or log in with an existing one.
- Once logged in, users are redirected to the dashboard where they can create, view, and manage tasks.

### Managing Tasks

- Users can create new tasks by providing the task name, description, due date, priority, category, and tags.
- Tasks can be marked as "Completed" or "In Progress."
- Tasks can be filtered and searched using the search bar on the dashboard.

### Categories & Tags

- Users can create and assign categories and tags to organize tasks.
- Tasks can be filtered based on categories and tags.

## Technologies Used

- **Django** - Backend web framework
- **PostgreSQL** - Relational database
- **Bootstrap 5** - Frontend framework for responsive design
- **Tailwind CSS** (Optional) - For advanced styling
- **HTML5** & **CSS3** - Markup and styling
- **JavaScript** - Interactivity and dynamic features

## Project Structure

task-management-system/ │ ├── task_manager/ # Main Django application │ ├── settings.py # Django settings │ ├── urls.py # Application URLs │ ├── models.py # Database models │ ├── views.py # View functions and classes │ ├── templates/ # HTML templates │ │ ├── base.html # Base template │ │ ├── task_list.html # Template for displaying tasks │ │ ├── includes/ # Folder for reusable templates │ │ │ ├── sidebar.html # Sidebar template │ └── static/ # Static files (CSS, JS) │ ├── db.sqlite3 # SQLite database (if used locally) ├── manage.py # Django management script ├── README.md # Project README └── requirements.txt # Project dependencies


## Screenshots

### Task List
![Task List](path/to/task_list_screenshot.png)

### Task Form
![Task Form](path/to/task_form_screenshot.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add a new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

---

For any issues or questions, please open a GitHub issue or contact us at [support@example.com](mailto:support@example.com).
