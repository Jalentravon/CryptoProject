import streamlit as st
import pandas as pd
import plotly.express as px

# Load cryptocurrency data
btc = pd.read_csv("coin_Bitcoin.csv")
eth = pd.read_csv("coin_Ethereum.csv")
xrp = pd.read_csv("coin_XRP.csv")
doge = pd.read_csv("coin_Dogecoin.csv")

# Convert 'Date' column to datetime format
for df in [btc, eth, xrp, doge]:
    df['Date'] = pd.to_datetime(df['Date'])

st.title("Cryptocurrency Market Analysis")

#create a dropdown to select the cryptocurrency
coin = st.selectbox("Select a cryptocurrency", ["Bitcoin", "Ethereum", "XRP", "Dogecoin"])

# Display the selected cryptocurrency's price over time
if coin == "Bitcoin":
    df = btc
elif coin == "Ethereum":
    df = eth
elif coin == "XRP":
    df = xrp
else:
    df = doge

# Plot price over time
fig1 = px.line(df, x='Date',
                y='Close', 
                title=f"{coin} Price Over Time")
st.plotly_chart(fig1)

# Calculate daily returns
df['Returns'] = df['Close'].pct_change()

# Plot daily returns over time
fig2 = px.line(df, x='Date', 
               y='Returns', 
               title=f"{coin} Daily Returns")
st.plotly_chart(fig2)