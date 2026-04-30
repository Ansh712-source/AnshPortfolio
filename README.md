# 🌐 Personal Portfolio Website

🚀 A dynamic full-stack portfolio website built using Flask and MySQL.  
This project allows you to showcase your projects, receive messages from visitors, and manage content through an admin panel.

---

## ✨ Features

- 📌 Dynamic Projects Section (data fetched from database)
- 📩 Contact Form (stores user messages in MySQL)
- 🔐 Admin Panel (Add/Delete projects)
- 🎨 Clean and responsive UI
- ⚙️ Backend powered by Flask

---

## 🛠 Tech Stack

**Frontend:**
- HTML
- CSS
- JavaScript

**Backend:**
- Python (Flask)

**Database:**
- MySQL

---

## 📂 Project Structure

portfolio/
│── app.py
│
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── admin.html
│
├── static/
│ ├── style.css
│ ├── script.js


---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

### 2️⃣ Install Dependencies

### 3️⃣ Setup MySQL Database

Open MySQL and run:

```sql
CREATE DATABASE portfolio;

USE portfolio;

CREATE TABLE projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT
);

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    message TEXT
);
