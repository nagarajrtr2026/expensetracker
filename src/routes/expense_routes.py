from fastapi import APIRouter
from storage.file_handler import load_data, save_data
from services.expense_service import add_expense
from services.analytics_service import total

router = APIRouter()

# 👉 GET all expenses
@router.get("/expenses")
def get_expenses():
    data = load_data()
    return data

# 👉 ADD expense
@router.post("/expenses")
def create_expense(expense: dict):
    data = load_data()

    data.append(expense)

    save_data(data)
    return {"message": "Expense added"}

# 👉 TOTAL
@router.get("/expenses/total")
def get_total():
    data = load_data()
    return {"total": total(data)}

@router.delete("/expenses/{index}")
def delete_expense(index: int):
    data = load_data()

    if 0 <= index < len(data):
        deleted = data.pop(index)
        save_data(data)
        return {"message": "Deleted", "data": deleted}

    return {"error": "Invalid index"}

@router.get("/expenses/category/{category}")
def get_by_category(category: str):
    data = load_data()
    result = [d for d in data if d['category'].lower() == category.lower()]
    return result