# 🚀 Employee Management System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?style=for-the-badge&logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=for-the-badge&logo=mysql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

<p align="center">
An advanced Employee Management System developed using <b>Flask, MySQL, SQLAlchemy, and Bootstrap 5</b> with modern UI, dashboard analytics, pagination, searching, sorting, filtering, and complete CRUD operations.
</p>

---

# 📌 Features

## 👨‍💼 Employee Management

- ✅ Add Employee
- ✅ Update Employee
- ✅ Delete Employee
- ✅ View Employee Details
- ✅ Employee Dashboard

---

## 🏢 Department Management

- ✅ Add Department
- ✅ Edit Department
- ✅ Delete Department
- ✅ Department Statistics
- ✅ Employee Count per Department

---

## 🔍 Advanced Features

- ✅ Pagination
- ✅ Searching
- ✅ Sorting
- ✅ Filtering
- ✅ Dashboard Analytics
- ✅ Responsive UI
- ✅ Bootstrap Cards
- ✅ Animated Statistics
- ✅ Progress Bars
- ✅ Modern Navigation
- ✅ Mobile Friendly Design

---

# 📊 Dashboard

The dashboard displays:

- Total Employees
- Total Departments
- Total Payroll
- Average Salary
- Highest Salary
- Lowest Salary
- Largest Department
- Recent Employees
- Top Earners
- Department-wise Statistics

---

# 🛠 Tech Stack

| Technology | Used |
|------------|------|
| Python | ✅ |
| Flask | ✅ |
| SQLAlchemy ORM | ✅ |
| MySQL | ✅ |
| HTML5 | ✅ |
| CSS3 | ✅ |
| Bootstrap 5 | ✅ |
| Jinja2 | ✅ |

---

# 📂 Project Structure

```
Employee-Management-System/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   └── __init__.py
│
├── migrations/
├── app.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/adityaraj1001/Employee-Management-System.git

cd Employee-Management-System
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 Configure MySQL

Create a MySQL database:

```sql
CREATE DATABASE employee_db;
```

Update your **config.py**

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:YOUR_PASSWORD@localhost/employee_db"
```

---

# 🔄 Run Database Migration

```bash
flask db upgrade
```

---

# ▶️ Run the Project

```bash
python app.py
```

or

```bash
flask run
```

Visit

```
http://127.0.0.1:5000/home
```

---

# 📸 Project Modules

### 🏠 Dashboard

- Analytics Cards
- Charts
- Salary Statistics

### 👨 Employees

- Employee List
- Search Employees
- Filter Employees
- Sort Employees
- Pagination

### 🏢 Departments

- Department Statistics
- CRUD Operations
- Employee Distribution

---

# 📈 Implemented Assignment Features

| Requirement | Status |
|------------|--------|
| Employee CRUD | ✅ |
| Department CRUD | ✅ |
| Pagination | ✅ |
| Searching | ✅ |
| Sorting | ✅ |
| Filtering | ✅ |
| Responsive UI | ✅ |
| Dashboard | ✅ |
| SQLAlchemy ORM | ✅ |
| MySQL Integration | ✅ |

---

# 💻 Useful Commands

Install packages

```bash
pip install -r requirements.txt
```

Freeze requirements

```bash
pip freeze > requirements.txt
```

Run application

```bash
python app.py
```

Run migrations

```bash
flask db upgrade
```

---

# 🚀 Future Improvements

- Authentication & Login
- Employee Profile Images
- Excel Export
- PDF Reports
- Email Notifications
- REST API
- Role Based Access Control
- Dark Mode

---

# 👨‍💻 Developer

**Aditya Raj**

**GitHub**

https://github.com/adityaraj1001

---

# ⭐ Repository

If you like this project, consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is developed for educational purposes as part of a Flask Development coursework.
