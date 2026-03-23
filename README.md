# Expense Tracker Application (Full Stack)

## Overview

This project is a full-stack Expense Tracker application built using **FastAPI (backend)** and **Streamlit (frontend)**. It allows users to record daily expenses, categorize them, and analyze spending patterns through a simple and interactive interface.

The backend is deployed as a REST API, and the frontend consumes these APIs to provide a user-friendly experience.

---

## Features

* Add new expenses (amount, category, date)
* View all recorded expenses
* Categorize spending
* Backend API with FastAPI
* Interactive frontend using Streamlit
* Deployed and accessible via public URLs

---

## Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### Frontend

* Streamlit
* Requests (API communication)

### Deployment

* Render (Backend + Frontend hosting)
* GitHub (Version control)

---

## Project Structure

```
expense-tracker-advanced/
│
├── requirements.txt
│
├── src/
│   ├── api.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── storage/
│   └── utils/
│
├── data/
│   └── expenses.json
│
└── frontend/
    └── app.py
```

---

## How It Works

1. The user interacts with the Streamlit frontend.
2. Frontend sends HTTP requests to the FastAPI backend.
3. Backend processes data and stores it in a JSON file.
4. Response is returned to frontend and displayed.

---

## API Endpoints

| Method | Endpoint  | Description      |
| ------ | --------- | ---------------- |
| POST   | /expenses | Add new expense  |
| GET    | /expenses | Get all expenses |

---

## Installation (Local Setup)

### 1. Clone Repository

```
git clone <your-repo-link>
cd expense-tracker-advanced
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Backend

```
uvicorn src.api:app --reload
```

### 4. Run Frontend

```
cd frontend
streamlit run app.py
```

---

## Deployment

### Backend

* Hosted on Render as a Web Service
* Runs using Uvicorn

### Frontend

* Hosted on Render as a separate Web Service
* Uses Streamlit

---

## Live URLs

* Backend API: https://expensetracker-w0l7.onrender.com
* Frontend App: https://expensetracker-1-fwke.onrender.com

---

## Key Learnings

* Building REST APIs using FastAPI
* Structuring scalable Python projects
* Integrating frontend with backend using HTTP requests
* Debugging deployment issues
* Deploying full-stack applications on cloud platforms

---

## Future Improvements

* Database integration (PostgreSQL / MongoDB)
* User authentication
* Advanced analytics and charts
* Mobile-friendly UI

---

## Conclusion

This project demonstrates a complete full-stack workflow, from development to deployment. It highlights the integration of backend APIs with a frontend interface and provides a solid foundation for building production-ready applications.

---
