# 💰 Expense Tracker (Full Stack App)

A complete **full-stack expense tracking application** built using:

* ⚡ FastAPI (Backend API)
* 🎨 Streamlit (Frontend UI)
* 🐍 Python (Core logic)
* 📊 Data Visualization

---

## 🚀 Features

### ✅ Core Features

* Add Expense (Category, Amount, Date)
* View All Expenses
* Delete Expense
* Filter by Category

### 📊 Analytics

* Total Spending
* Category-wise Summary
* Monthly Summary
* Data Visualization (Bar Chart)

### 🔥 Advanced

* FastAPI REST API
* Streamlit Interactive UI
* JSON-based storage
* Modular project structure

---

## 🗂️ Project Structure

```
expense-tracker-advanced/
│
├── data/
│   └── expenses.json
│
├── frontend/
│   └── app.py
│
├── src/
│   ├── api.py
│   ├── main.py
│
│   ├── routes/
│   │   └── expense_routes.py
│
│   ├── models/
│   │   └── expense_model.py
│
│   ├── services/
│   │   ├── expense_service.py
│   │   └── analytics_service.py
│
│   ├── storage/
│   │   └── file_handler.py
│
│   ├── utils/
│   │   ├── date_utils.py
│   │   └── generator.py
│
│   └── visualization/
│       └── charts.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```
git clone https://github.com/nagarajrtr2026/expensetracker.git
cd expense-tracker-advanced
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run Backend (FastAPI)

```
cd src
uvicorn api:app --reload
```

👉 Open in browser:
http://127.0.0.1:8000
👉 API Docs:
http://127.0.0.1:8000/docs

---

## 🎨 Run Frontend (Streamlit)

```
cd frontend
streamlit run app.py
```

👉 Opens automatically in browser

---

## 🔗 API Endpoints

| Method | Endpoint                      | Description        |
| ------ | ----------------------------- | ------------------ |
| GET    | /expenses                     | Get all expenses   |
| POST   | /expenses                     | Add expense        |
| DELETE | /expenses/{index}             | Delete expense     |
| GET    | /expenses/total               | Total spending     |
| GET    | /expenses/category/{category} | Filter by category |

---

## 🧪 Sample JSON

```
{
  "category": "Food",
  "amount": 200,
  "date": "2026-03-23"
}
```

---

## 📊 Example Output

* Category-wise spending chart
* Total expense calculation
* Filtered results

---

## 🧠 Future Improvements

* 🔐 User Authentication
* 🗄️ Database (SQLite / MongoDB)
* 📱 Mobile App Integration
* 🤖 ML-based Expense Prediction
* 🌐 Deployment (Render / AWS)

---

## 👨‍💻 Author

**NAGARAJ M**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
