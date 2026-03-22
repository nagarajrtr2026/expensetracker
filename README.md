# Expense Tracker Advanced

## Overview

Expense Tracker Advanced is a modular Python application designed to manage and analyze personal expenses. The project focuses on clean architecture, separation of concerns, and practical data handling using JSON storage.

This application allows users to record expenses, analyze spending patterns, and visualize category-wise expenditure.

---

## Features

* Add new expenses with category, amount, and date
* Delete existing expenses using index-based selection
* View total expenditure
* Generate monthly spending summary
* Analyze category-wise spending
* Visualize expenses using bar charts
* Generate synthetic data for testing and experimentation

---

## Project Structure

```
expense-tracker-advanced/
│
├── data/
│   └── expenses.json
│
├── src/
│   ├── main.py
│   ├── models/
│   │   └── expense_model.py
│   ├── services/
│   │   ├── expense_service.py
│   │   └── analytics_service.py
│   ├── storage/
│   │   └── file_handler.py
│   ├── utils/
│   │   ├── date_utils.py
│   │   └── generator.py
│   └── visualization/
│       └── charts.py
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python 3
* JSON for data storage
* Matplotlib for visualization

---

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/YOUR_USERNAME/expense-tracker-advanced.git
   ```

2. Navigate to the project directory:

   ```
   cd expense-tracker-advanced
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

---

## Usage

1. Navigate to the source folder:

   ```
   cd src
   ```

2. Run the application:

   ```
   python main.py
   ```

3. Follow the menu options to:

   * Add expenses
   * Delete entries
   * View analytics
   * Generate reports

---

## Sample Data Format

```
[
    {
        "category": "Food",
        "amount": 250,
        "date": "2026-03-22"
    }
]
```

---

## Design Approach

The project follows a modular design:

* Models define data structure
* Services handle business logic
* Storage manages file operations
* Utilities provide helper functions
* Visualization handles data representation

This separation improves readability, scalability, and maintainability.

---

## Future Improvements

* User authentication system
* Web interface using Streamlit or Flask
* Database integration (SQLite or PostgreSQL)
* Machine learning-based expense prediction
* Export reports in CSV or PDF format

---

## Author

Developed as part of a hands-on learning process in building real-world Python applications with structured architecture and practical features.
