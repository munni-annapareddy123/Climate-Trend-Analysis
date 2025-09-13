import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# --- Title ---
st.title("🌍 Climate Trend Analysis")
st.write("This app visualizes climate trends. Using embedded sample data as CSV.")

# --- Embedded CSV Data ---
csv_data = """
Year,Temperature
2000,14.3
2005,14.5
2010,14.8
2015,15.0
2020,15.4
2022,15.7
2024,16.1
"""

# --- Read CSV from string ---
df = pd.read_csv(StringIO(csv_data))

# --- Show Data ---
st.subheader("📋 Data Preview")
st.dataframe(df)

# --- Plot ---
st.subheader("📈 Temperature Trends")
fig, ax = plt.subplots()
ax.plot(df['Year'], df['Temperature'], marker='o', linestyle='-', color='blue')
ax.set_xlabel("Year")
ax.set_ylabel("Temperature (°C)")
ax.set_title("Average Global Temperature Over Time")
st.pyplot(fig)

# --- Stats ---
st.subheader("🔎 Basic Statistics")
st.write(df.describe())

st.success("✅ Climate Trend Analysis App is Ready!")
