import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def plot_stocks_with_barrier(stock_names, barrier_level):
    # Create a DataFrame to store the stock data
    stock_data = pd.DataFrame()

    # Fetch stock data for each stock name
    for stock_name in stock_names:
        stock = yf.Ticker(stock_name)
        stock_history = stock.history(period='3y')['Close']
        stock_data[stock_name] = stock_history / stock_history.iloc[-1] * 100  # Normalize to base 100 from the end

    # Plotting the stock prices
    plt.figure(figsize=(10, 6))
    for stock_name in stock_names:
        plt.plot(stock_data[stock_name], label=stock_name)
        plt.axhline(stock_data[stock_name].iloc[-1] * barrier_level, linestyle='--', label=f'{stock_name} Barrier Level')

    plt.xlabel('Date')
    plt.ylabel('Normalized Price (Base 100 from the end)')
    plt.title('Stock Prices with Barrier Level')
    plt.legend()
    plt.grid(True)

    # Display the plot
    st.pyplot(plt)

# Streamlit app code
def main():
    # Set the page title
    st.title('Stock Chart with Barrier Level')

    # Input stock names and barrier level
    stock_names = st.text_input('Enter Stock Names (comma-separated)', 'AAPL,GOOGL,MSFT').split(',')
    barrier_level = st.slider('Enter Barrier Level (between 0 and 100%)', 0.0, 1.0, 0.5)

    # Check if the barrier level is within the valid range
    if 0 <= barrier_level <= 1:
        plot_stocks_with_barrier(stock_names, barrier_level)
    else:
        st.error('Invalid barrier level. Please enter a value between 0 and 100%.')

# Run the Streamlit app
if __name__ == '__main__':
    main()
