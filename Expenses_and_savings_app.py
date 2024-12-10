import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Get pocket money input
        pocket_money = float(pocket_money_entry.get())
        if pocket_money <= 0:
            raise ValueError("Pocket money must be greater than 0.")

        # Gather expenses
        expenses = {}
        total_expenses = 0
        for category, entry in expense_entries.items():
            expense = float(entry.get() or "0")
            if expense < 0:
                raise ValueError("Expenses must be positive numbers.")
            expenses[category] = expense
            total_expenses += expense

        # Calculate savings
        savings = pocket_money - total_expenses

        # Display results
        result_text = f"Total Pocket Money: Ru.{pocket_money:.2f}\n"
        result_text += f"Total Expenses: Ru.{total_expenses:.2f}\n"
        result_text += "\nCategory-wise Expenses:\n"
        for category, expense in expenses.items():
            result_text += f"  {category}: Ru.{expense:.2f}\n"
        result_text += f"\nSavings: Ru.{savings:.2f}\n"

        if savings >= 0:
            savings_percentage = (savings / pocket_money) * 100
            result_text += f"Percentage Saved: {savings_percentage:.2f}%\n"
            result_text += f"Congratulations! You saved Ru.{savings:.2f} this month."
        else:
            result_text += "Warning: You have overspent this month."

        result_label.config(text=result_text)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create main app window
root = tk.Tk()
root.title("Pocket Money Tracker")

# Pocket money input
tk.Label(root, text="Enter your total monthly pocket money:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
pocket_money_entry = tk.Entry(root, width=20)
pocket_money_entry.grid(row=0, column=1, padx=10, pady=5)

# Expense categories
categories = ["Food", "Transport", "Entertainment", "Shopping", "Personal care", "Grocery", 
              "Phone Recharge", "Internet", "Gym", "Stationary", "Other"]
expense_entries = {}

tk.Label(root, text="Enter your expenses for each category:").grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

for i, category in enumerate(categories, start=2):
    tk.Label(root, text=f"  {category}:").grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(root, width=20)
    entry.grid(row=i, column=1, padx=10, pady=5)
    expense_entries[category] = entry

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=len(categories) + 2, column=0, columnspan=2, pady=10)

# Result display
result_label = tk.Label(root, text="", justify="left", anchor="w")
result_label.grid(row=len(categories) + 3, column=0, columnspan=2, padx=10, pady=10, sticky="w")

# Run the app
root.mainloop()
