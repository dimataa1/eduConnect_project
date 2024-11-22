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

Before running the project, ensure you have the following installed:

- Python 3.x
- Django (>= 3.2)
- pip (Python package installer)

### Install Dependencies

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
