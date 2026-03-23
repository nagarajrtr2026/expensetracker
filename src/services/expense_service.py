from src.models.expense_model import Expense
from src.utils.date_utils import get_today

def add_expense(data):
    cat = input("Category: ")
    amt = float(input("Amount: "))

    exp = Expense(cat, amt, get_today())
    data.append(exp.to_dict())
    print("✅ Expense added!")

def delete_expense(data):
    if not data:
        print("❌ No expenses to delete!")
        return

    for i, exp in enumerate(data):
        print(i, exp)

    idx = int(input("Enter index to delete: "))

    if 0 <= idx < len(data):
        data.pop(idx)
        print("✅ Deleted!")
    else:
        print("❌ Invalid index!")
