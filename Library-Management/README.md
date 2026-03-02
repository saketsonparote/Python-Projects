# 📚 Library Management System

A complete Library Management System built using Python with both:

- 🖥 CLI (Command Line Interface)
- 🌐 Web App Interface using Streamlit

This project allows managing books and members, including borrowing and returning books with persistent JSON storage.

---

## 🚀 Features

### 📘 Book Management
- Add new books
- List all books
- Track total and available copies
- Unique Book ID generation

### 👤 Member Management
- Add new members
- List all members
- Unique Member ID generation

### 🔁 Borrow / Return System
- Borrow books (with availability check)
- Return books (updates available copies)
- Track borrowed history per member

### 💾 Persistent Storage
- Data stored in `library.json`
- Automatically loads and saves data
- Maintains consistency between books and members

---

## 🛠 Technologies Used

- Python
- OOP (Object-Oriented Programming)
- JSON for storage
- Streamlit (for web interface)
- pathlib
- datetime
- random & string (ID generation)

---

## 📂 Project Structure

Library-Management/
│
├── main.py # CLI Version
├── streamlit_ui.py # Streamlit Web Version
├── library.json # Database File
└── README.md


---

## ▶️ How To Run

### 🔹 Run CLI Version

python main.py

🔹 Run Streamlit Web App

First install Streamlit (if not installed):

pip install streamlit

Then run:

streamlit run streamlit_ui.py

The web app will open in your browser.

🧠 Key Learning Outcomes

Designing structured data models

Managing state with JSON storage

Implementing borrowing logic with consistency checks

Working with both CLI and Web interfaces

Applying OOP principles in a real-world scenario

📌 Future Improvements

Add search functionality (by title or author)

Add book update/delete feature

Add due dates and fine calculation

Add authentication system

Replace JSON with SQLite database

👨‍💻 Author

Saket Sonparote

⭐ This project was built to strengthen core Python and OOP fundamentals before moving into advanced Data Science projects.
