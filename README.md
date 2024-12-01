# EduConnect

EduConnect is a web platform designed for students and teachers, where they can interact, share educational content, ask questions, and receive answers. It allows teachers and students to create and manage posts, and make interactactions. The platform includes user authentication and roles management for students and teachers.

## Features

- **User Authentication:** Register, login, and logout functionality.
- **Role-based System:** Two user roles, `student` and `teacher`, with specific permissions for each.
- **Post Creation:** Teachers can create posts, with options to add images, labels, and descriptions.
- **Comment System:** Users can comment on posts.
- **Profile Management:** Users can manage their profiles, including personal information and points system.
- **Dashboard:** Provides an overview of posts, comments, and the user's activities.
- **Responsive Design:** The website is fully responsive and built with Bootstrap.

## Tech Stack

- **Frontend:**
  - HTML5
  - CSS3 (via Bootstrap 5)
  - JavaScript (via Bootstrap Icons)

- **Backend:**
  - Django
  - Python

- **Database:**
  - SQLite (default for development)
  - PostgresSql
  - Cloudinary (to be extended)

## Setup

### Prerequisites

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv env
   ```

   **Activate the virtual environment:**

   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Django development server:**

   ```bash
   python manage.py runserver
   ```

   This command will start the server, and you should be able to access your project at `http://127.0.0.1:8000/`.

## Additional Commands

- **Make migrations:**

   ```bash
   python manage.py makemigrations
   ```

- **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

- **Create a superuser (for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create an admin user.

## Usage

Include instructions for using the project here.

## Requirements

Make sure you have a `requirements.txt` file in your project directory. You can generate it using:

```bash
pip freeze > requirements.txt
```
