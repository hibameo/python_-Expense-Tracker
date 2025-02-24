import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💰 Expense Tracker")

# Initialize session state
if "expenses" not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=["Date", "Category", "Amount"])

# Input fields
date = st.date_input("Select Date")
category = st.selectbox("Select Category", ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Others"])
amount = st.number_input("Enter Amount", min_value=0.0, format="%.2f")

# Add expense button
if st.button("Add Expense"):
    new_expense = pd.DataFrame([[date, category, amount]], columns=["Date", "Category", "Amount"])
    
    # ✅ Fix: Avoid Concat on Empty DataFrame
    if st.session_state.expenses.empty:
        st.session_state.expenses = new_expense
    else:
        st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)
    
    st.success("Expense Added!")

# Show expense table
st.subheader("📋 Expense History")
st.dataframe(st.session_state.expenses)

# Category-wise Expense Visualization
st.subheader("📊 Expense Distribution")
if not st.session_state.expenses.empty:
    fig = px.pie(st.session_state.expenses, names="Category", values="Amount", title="Expenses by Category")
    st.plotly_chart(fig)
