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
    