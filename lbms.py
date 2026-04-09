import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Database connection
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    quantity INTEGER
)
""")

conn.commit()

# Function to Add Book
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    quantity = quantity_entry.get()

    if title == "" or author == "" or quantity == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    cursor.execute("INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)",
                   (title, author, quantity))
    conn.commit()

    messagebox.showinfo("Success", "Book Added Successfully!")

    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)


# Function to View Books
def view_books():
    cursor.execute("SELECT * FROM books")
    records = cursor.fetchall()

    view_window = tk.Toplevel(root)
    view_window.title("All Books")
    view_window.geometry("500x300")

    tree = ttk.Treeview(view_window, columns=("ID", "Title", "Author", "Quantity"), show="headings")

    tree.heading("ID", text="ID")
    tree.heading("Title", text="Title")
    tree.heading("Author", text="Author")
    tree.heading("Quantity", text="Quantity")

    tree.pack(fill="both", expand=True)

    for row in records:
        tree.insert("", tk.END, values=row)


# Main Window
root = tk.Tk()
root.title("Library Management System")
root.geometry("400x400")

tk.Label(root, text="Library Management System", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Book Title").pack()
title_entry = tk.Entry(root)
title_entry.pack()

tk.Label(root, text="Author").pack()
author_entry = tk.Entry(root)
author_entry.pack()

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Button(root, text="Add Book", command=add_book).pack(pady=10)
tk.Button(root, text="View Books", command=view_books).pack(pady=5)

root.mainloop()