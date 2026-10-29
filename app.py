from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "expense_tracker_secret"

DB = "expenses.db"


def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL
            )
        """)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        category = request.form.get("category", "")
        date = request.form.get("date", "")

        try:
            amount = float(request.form.get("amount", ""))
        except ValueError:
            amount = 0

        if not title or not date or category not in ["Income", "Expense"] or amount <= 0:
            flash("Enter valid transaction details.")
            return redirect(url_for("index"))

        with sqlite3.connect(DB) as conn:
            conn.execute(
                "INSERT INTO transactions (title, amount, category, date) VALUES (?, ?, ?, ?)",
                (title, amount, category, date)
            )

        flash("Transaction added successfully!")
        return redirect(url_for("index"))

    search = request.args.get("search", "").strip()
    category = request.args.get("category", "")

    query = "SELECT * FROM transactions WHERE title LIKE ?"
    params = [f"%{search}%"]

    if category in ["Income", "Expense"]:
        query += " AND category = ?"
        params.append(category)

    query += " ORDER BY date DESC, id DESC"

    with sqlite3.connect(DB) as conn:
        conn.row_factory = sqlite3.Row
        transactions = conn.execute(query, params).fetchall()

        totals = conn.execute("""
            SELECT
                COALESCE(SUM(CASE WHEN category = 'Income' THEN amount ELSE 0 END), 0) AS income,
                COALESCE(SUM(CASE WHEN category = 'Expense' THEN amount ELSE 0 END), 0) AS expenses
            FROM transactions
        """).fetchone()

    balance = totals["income"] - totals["expenses"]

    return render_template(
        "index.html",
        transactions=transactions,
        income=totals["income"],
        expenses=totals["expenses"],
        balance=balance,
        search=search,
        selected_category=category
    )


@app.route("/delete/<int:transaction_id>", methods=["POST"])
def delete_transaction(transaction_id):
    with sqlite3.connect(DB) as conn:
        conn.execute(
            "DELETE FROM transactions WHERE id = ?",
            (transaction_id,)
        )

    flash("Transaction deleted.")
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
