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

