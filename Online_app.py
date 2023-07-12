import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_style('darkgrid')

def get_stock_description(stock_name):
    # Retrieve stock information using yfinance
    stock = yf.Ticker(stock_name)
    info = stock.info

    # Extract relevant information
    description = info.get('longBusinessSummary', 'N/A')
    sector = info.get('sector', 'N/A')
    industry = info.get('industry', 'N/A')

    return description, sector, industry

def plot_stocks_with_barrier(stock_names, barrier_level, period):
    # Create a DataFrame to store the stock data
    stock_data = pd.DataFrame()

    # Fetch stock data for each stock name
    for stock_name in stock_names:
        stock = yf.Ticker(stock_name)
        stock_history = stock.history(period=period)['Close']
        stock_data[stock_name] = stock_history / stock_history.iloc[-1] * 100  # Normalize to base 100 from the end

    # Plotting the stock prices
    plt.figure(figsize=(10, 6))
    for stock_name in stock_names:
        plt.plot(stock_data[stock_name], label=stock_name, linewidth=2)

    plt.axhline(barrier_level, color='red', linestyle='--', label='Barrier Level', linewidth=2)
    plt.xlabel('Date')
    plt.ylabel('Normalized Price (Base 100 from the end)')
    plt.title('Optimize your idea')
    plt.legend()
    plt.tight_layout()

    # Set plot style
    sns.despine()

    # Display the plot
    st.pyplot(plt)

# Streamlit app code
def main():
    # Set the page title
    st.title('Stock Chart with Barrier Level')

    # Input stock names and barrier level
    stock_names = st.text_input('Enter Stock Names (comma-separated)', 'AAPL,GOOGL,MSFT').split(',')
    barrier_level = st.slider('Enter Barrier Level', 0.0, 200.0, 100.0, step=0.1)
    period = st.selectbox('Select Period', ('6mo', '1y', '1d', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'))

    # Check if the barrier level is within the valid range
    if 0 <= barrier_level <= 200:
        plot_stocks_with_barrier(stock_names, barrier_level, period)

        # Display stock descriptions and summary
        st.subheader('Stock Descriptions')
        for stock_name in stock_names:
            st.write(f"**{stock_name}**")
            description, sector, industry = get_stock_description(stock_name)
            st.write(f"Description: {description}")
            st.write(f"Sector: {sector}")
            st.write(f"Industry: {industry}")
            st.write('---')

        st.subheader('Investment Summary')
        st.write('Based on historical data and market trends, investing in these stocks could be interesting due to various factors such as strong financial performance, growth potential, and industry dominance. However, it is important to conduct thorough research and consider your own investment goals and risk tolerance before making any investment decisions.')

    else:
        st.error('Invalid barrier level. Please enter a value between 0 and 200.')

# Run the Streamlit app
if __name__ == '__main__':
    main()
