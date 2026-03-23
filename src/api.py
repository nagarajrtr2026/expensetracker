from fastapi import FastAPI
from src.routes.expense_routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Expense Tracker API Running 🚀"}
