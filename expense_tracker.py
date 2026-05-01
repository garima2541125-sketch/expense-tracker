import json
import os
from tkinter import *
from tkinter import messagebox
from datetime import datetime

FILE = "expenses.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

data = load_data()

def add_expense():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        note = note_entry.get()
        date = datetime.now().strftime("%Y-%m-%d")

        data.append({
            "amount": amount,
            "category": category,
            "note": note,
            "date": date
        })

        save_data(data)
        messagebox.showinfo("Success", "Expense Added!")

        amount_entry.delete(0, END)
        category_entry.delete(0, END)
        note_entry.delete(0, END)

    except:
        messagebox.showerror("Error", "Invalid Input")

def view_expenses():
    listbox.delete(0, END)
    for exp in data:
        listbox.insert(END, f"₹{exp['amount']} | {exp['category']} | {exp['date']}")

def total_expense():
    total = sum(exp["amount"] for exp in data)
    messagebox.showinfo("Total", f"Total Expense: ₹{total}")

# Window
root = Tk()
root.title("Expense Tracker")
root.geometry("420x550")
root.configure(bg="#f4f6f8")

# Title
Label(root, text="💰 Expense Tracker", font=("Arial", 18, "bold"), bg="#f4f6f8").pack(pady=10)

# Frame
frame = Frame(root, bg="white", bd=2, relief=RIDGE)
frame.pack(padx=20, pady=10, fill="both")

Label(frame, text="Amount", bg="white").pack(pady=5)
amount_entry = Entry(frame, font=("Arial", 12))
amount_entry.pack(pady=5)

Label(frame, text="Category", bg="white").pack(pady=5)
category_entry = Entry(frame, font=("Arial", 12))
category_entry.pack(pady=5)

Label(frame, text="Note", bg="white").pack(pady=5)
note_entry = Entry(frame, font=("Arial", 12))
note_entry.pack(pady=5)

# Buttons
btn_frame = Frame(root, bg="#f4f6f8")
btn_frame.pack(pady=10)

Button(btn_frame, text="Add", width=10, bg="#4CAF50", fg="white", command=add_expense).grid(row=0, column=0, padx=5)
Button(btn_frame, text="View", width=10, bg="#2196F3", fg="white", command=view_expenses).grid(row=0, column=1, padx=5)
Button(btn_frame, text="Total", width=10, bg="#FF9800", fg="white", command=total_expense).grid(row=0, column=2, padx=5)

# Listbox
listbox = Listbox(root, font=("Arial", 11), height=12)
listbox.pack(padx=20, pady=10, fill="both")

root.mainloop()