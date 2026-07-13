import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Forecasting Dashboard", layout="wide")

st.title("📊 Sales Forecasting Dashboard")

# Load dataset
df = pd.read_csv("train.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Information")
st.write(df.describe())

# Sales by Category
st.subheader("Sales by Category")

category_sales = df.groupby("Category")["Sales"].sum()

fig, ax = plt.subplots(figsize=(8,5))
category_sales.plot(kind="bar", ax=ax)
ax.set_ylabel("Sales")
ax.set_title("Sales by Category")

st.pyplot(fig)

# Sales by Region
st.subheader("Sales by Region")

region_sales = df.groupby("Region")["Sales"].sum()

fig, ax = plt.subplots(figsize=(8,5))
region_sales.plot(kind="bar", ax=ax)
ax.set_ylabel("Sales")
ax.set_title("Sales by Region")

st.pyplot(fig)

# Top Products
st.subheader("Top 10 Products")

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig, ax = plt.subplots(figsize=(10,5))
top_products.plot(kind="barh", ax=ax)

st.pyplot(fig)

# Forecast
st.subheader("Future Sales Forecast")

forecast = pd.read_csv("future_sales_forecast.csv")

st.dataframe(forecast)

fig, ax = plt.subplots(figsize=(8,5))

ax.plot(
    forecast.iloc[:,0],
    forecast.iloc[:,1],
    marker="o"
)

ax.set_title("Future Sales Forecast")
ax.set_xlabel("Date")
ax.set_ylabel("Forecast")

st.pyplot(fig)

st.success("Dashboard Loaded Successfully!")