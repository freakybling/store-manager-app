# store-manager-app
This is a small command-line app I built to solve a real-life problem for my friend's store. It helps manage perfumes—keeping track of their name, stock, and price. You can add, search, update, and delete perfumes easily. All the data is stored locally in an SQLite database. Simple, fast, and gets the job done.

# Perfume Inventory Manager 🧴 (CLI Version)

A simple command-line Python app to manage perfume inventory using `SQLite3`. You can **Add**, **View**, **Search**, **Update**, and **Delete** perfumes right from your terminal.

---

## 🖥️ Features

- Add new perfumes with name, stock, and price.
- View all perfume entries.
- Search perfumes by name.
- Update existing perfume records using ID.
- Delete perfumes using ID.
- Keeps data persistent using an SQLite database.

---

## 🛠️ Built With

- **Python 3**
- **SQLite3**

---

## 📁 Project Structure

perfume-inventory-cli/
│
├── db.py # Database logic and functions (CRUD)
├── app.py # CLI app logic (user interaction and menu)
├── perfume.db # SQLite database file (auto-created if not present)
└── README.md # This file