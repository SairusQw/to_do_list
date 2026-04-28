# 🚀 Django Todo App

A sleek, functional, and user-friendly Task Management System built with **Python** and **Django**. This application allows users to organize their daily activities using tasks, deadlines, and customizable tags with a modern, sidebar-driven UI.

## ✨ Features

- **Dashboard:** A comprehensive overview with real-time statistics (Total, Completed, and Pending tasks).
- **Task Management:** - Create, Edit, and Delete tasks.
    - Toggle task completion status with a single click.
    - Assign deadlines and multiple tags to each task.
- **Tag System:** - Organize tasks with custom tags.
    - All tags are automatically sorted **alphabetically**.
    - Dedicated interface for tag management (CRUD).
- **Modern UI/UX:**
    - Responsive **Sidebar** that stays at the top for easy navigation.
    - Styled with **Bootstrap 5** and **Bootstrap Icons**.
    - Clean, card-based layout for better readability.
- **Robust Validation:** Professional form handling with error messages and field validation.

## 🛠️ Tech Stack

- **Backend:** Python 3.x, Django Framework.
- **Frontend:** HTML5, CSS3 (Custom Flexbox layout), JavaScript.
- **Styling:** Bootstrap 5, Bootstrap Icons.
- **Database:** SQLite (default).

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd <project-folder>
   
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   
3. **Apply migrations:**
   ```bash
   python manage.py migrate
   
4. **Run the development server:**
   ```bash
   python manage.py runserver
   
5. **Access the app:**
   ```bash
   Open http://127.0.0.1:8000 in your browser.

# 📁 Project Structure
- **models.py:** Task and Tag entities.

- **views.py:** Class-Based Views (CBVs) for all operations.

- **static/css/style.css:** Custom UI styles and sidebar positioning.

- **templates/:** Modular Django templates with includes for Sidebar and Navigation.