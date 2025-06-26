# 📝 Post & Comments Web App

This is a full-stack web application built using **Flask (Python)** on the backend and **HTML/CSS/JavaScript** on the frontend.  
It allows users to create, view, and delete blog posts, add comments, and optionally upload an image for each post.

---

## 🔧 Features

- ✅ Create and view blog posts
- 🖼️ Upload and display an image with each post
- 💬 Add and delete comments under each post
- 🗑️ Delete posts and comments
- 🎨 Simple, user-friendly frontend interface
- 🗂 Powered by **SQLite** (lightweight, file-based database)
- 🔗 Built using **Flask** and **SQLAlchemy**

---

## 🗂️ Project Structure
post-comments-service/
│
├── app.py # Main Flask application
├── models.py # SQLAlchemy ORM models
├── templates/
│ └── index.html # Frontend UI with dynamic content
├── static/
│ └── uploads/ # Uploaded images stored here
├── .gitignore # Git ignore rules
└── README.md # This file

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/stalepizza/posts-comments-service.git
cd posts-comments-service
```
### 2. Set up virtual environment (optional but reccommended)

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```
### 3. Install Dependencies

```bash
pip install Flask Flask-SQLAlchemy
```
### 4. Run

```bash
python app.py
```
---
## 🧠 Technologies Used

- **Python 3**
- **Flask** – Lightweight Python web framework
- **SQLAlchemy** – ORM to interact with SQLite database
- **HTML, CSS & JS** – Frontend stack
- **SQLite** – Embedded database

---

## 💡 Future Improvements

- User authentication (login/signup)
- Post editing
- Pagination for posts and comments
- Better image optimization and file validation

