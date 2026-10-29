# Expense Tracker 💰

A web-based expense management application built using Python, Flask, SQLite, HTML, and CSS. It helps users record income and expenses, monitor their spending, and track their available balance through a simple dashboard.

## Features

* ➕ Add income and expense transactions.
* 📋 View transaction history.
* 🔍 Search transactions by title.
* 🗂️ Filter transactions by income or expense.
* 💵 Calculate total income.
* 📉 Calculate total expenses.
* 💰 Automatically calculate the remaining balance.
* 🗑️ Delete transactions.
* 💾 Store transaction data using SQLite.
* 📱 Responsive user interface.

## Technologies Used

* Python
* Flask
* SQLite
* HTML5
* CSS3

## Project Structure

```text
ExpenseTracker/
├── app.py
├── .gitignore
├── README.md
├── templates/
│   ├── base.html
│   └── index.html
└── static/
    └── style.css
```

The `expenses.db` database is generated automatically when the application starts. It is excluded from GitHub through `.gitignore`.

## Prerequisites

* Python 3
* pip

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sharanyaveeranki-creator/ExpenseTracker.git
```

### 2. Open the Project Folder

```bash
cd ExpenseTracker
```

### 3. Install Flask

```bash
py -m pip install flask
```

### 4. Run the Applicatio
