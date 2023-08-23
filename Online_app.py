import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from openbb_terminal.stocks.stocks_helper import load

# Set Seaborn style
sns.set_style('darkgrid')

# ... Other functions and code ...

# Streamlit app code
def main():
    # Set the page title
    st.title('Closing Prices of Stocks on Specific Date')

    # Add your logo image
    logo_path = 'logo.png'
    st.image(logo_path, use_column_width=True)

    # Input stock names and target date
    ticker_list = st.text_input('Enter Ticker Symbols (comma-separated)', 'AAPL,GOOGL,MSFT').split(',')
    target_date = st.date_input('Select Date', pd.to_datetime('2023-05-26'))

    if st.button('Get Closing Prices'):
        closing_prices = get_closing_prices(ticker_list, target_date)

        if closing_prices:
            st.write('Closing Prices on', target_date)
            for ticker, price in closing_prices.items():
                st.write(f"{ticker}: {price:.2f}")
        else:
            st.warning('No data available for the selected date or tickers.')

# Run the Streamlit app
if __name__ == '__main__':
    main()
