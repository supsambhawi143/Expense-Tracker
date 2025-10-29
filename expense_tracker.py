import csv
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

Filename = 'expenses.csv'

def initialize_file():
    try:
        with open(Filename, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])
    except FileExistsError:
        pass

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = category_entry.get()
    amount = amount_entry.get()
    description = description_entry.get()


    if not category or not amount:
        messagebox.showwarning("Input Error", "Please enter category and amount!")
        return 
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number!")
        return
    
    with open(Filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    messagebox.showinfo("Success", "Expense recorded successfully!")
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    view_expenses()


def view_expenses():
    for row in tree.get_children():
        tree.delete(row)
    
    try:
        with open(Filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                tree.insert("", tk.END, values=row)
    except FileNotFoundError:
        pass

initialize_file()

root = tk.Tk()
root.title("Expense Tracker")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Category:").grid(row=0, column=0)
category_entry = tk.Entry(frame)
category_entry.grid(row=0, column=1)

tk.Label(frame, text="Amount:").grid(row=1, column=0)
amount_entry = tk.Entry(frame)
amount_entry.grid(row=1, column=1)

tk.Label(frame, text="Description:").grid(row=2, column=0)
description_entry = tk.Entry(frame)
description_entry.grid(row=2, column=1)

tk.Button(frame, text="Add Expense", command=add_expense).grid(row=3, column=0, columnspan=2, pady=10)

tree = ttk.Treeview(root, columns=("Date", "Category", "Amount", "Description"), show="headings")
tree.heading("Date", text="Date")
tree.heading("Category", text="Category")
tree.heading("Amount", text="Amount")
tree.heading("Description", text="Description")
tree.pack(pady=10)

view_expenses()

root.mainloop()