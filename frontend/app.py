import streamlit as st
import requests

API_URL = "https://expensetracker-w0l7.onrender.com"

st.title("💰 Expense Tracker App")

# 👉 ADD EXPENSE
st.header("Add Expense")

category = st.text_input("Category")
amount = st.number_input("Amount")
date = st.text_input("Date (YYYY-MM-DD)")

if st.button("Add"):
    data = {
        "category": category,
        "amount": amount,
        "date": date
    }

    res = requests.post(f"{API_URL}/expenses", json=data)

    if res.status_code == 200:
        st.success("Added successfully!")
    else:
        st.error("Error adding expense")

# 👉 VIEW EXPENSES
import pandas as pd

st.header("All Expenses")

if st.button("Load Expenses"):
    res = requests.get(f"{API_URL}/expenses")
    data = res.json()

    df = pd.DataFrame(data)
    st.dataframe(df)

    # delete option
    idx = st.number_input("Enter index to delete", min_value=0)

    if st.button("Delete"):
        res = requests.delete(f"{API_URL}/expenses/{int(idx)}")
        st.write(res.json())

# 👉 TOTAL
st.header("Total Spending")

if st.button("Get Total"):
    res = requests.get(f"{API_URL}/expenses/total")
    total = res.json()

    st.write(total)

st.header("Filter by Category")

cat = st.text_input("Enter category")

if st.button("Filter"):
    res = requests.get(f"{API_URL}/expenses/category/{cat}")
    st.write(res.json())

st.header("Spending Chart")

if st.button("Show Chart"):
    res = requests.get(f"{API_URL}/expenses")
    data = res.json()

    df = pd.DataFrame(data)

    if not df.empty:
        chart_data = df.groupby("category")["amount"].sum()
        st.bar_chart(chart_data)

st.header("Category Summary")

if st.button("Analyze"):
    res = requests.get(f"{API_URL}/expenses")
    data = res.json()

    df = pd.DataFrame(data)

    summary = df.groupby("category")["amount"].sum()
    st.write(summary)
