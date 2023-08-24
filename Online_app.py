import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_style('darkgrid')

def get_closing_prices(ticker_list, target_date):
    closing_prices = {}
    
    for ticker in ticker_list:
        stock = yf.Ticker(ticker)
        stock_data = stock.history(period='1d', start=target_date, end=target_date)
        
        if not stock_data.empty:
            closing_price = stock_data['Close'].iloc[0]
            closing_prices[ticker] = closing_price
    
    return closing_prices

# Streamlit app code
def main():
    # Set the page title
    st.title('Closing Prices of Stocks on Specific Date')

    # Add your logo image from GitHub
    logo_path = 'https://raw.githubusercontent.com/username/my-repo/main/images/logo.png'
    st.image(logo_path, use_column_width=True)

    # Input stock names and target date
    ticker_list = st.text_input('Enter Ticker Symbols (comma-separated)', 'AAPL,GOOGL,MSFT').split(',')
    target_date = st.date_input('Select Date')

    if st.button('Get Closing Prices'):
        closing_prices = get_closing_prices(ticker_list, target_date.strftime('%Y-%m-%d'))
        
        if closing_prices:
            st.write('Closing Prices on', target_date)
            for ticker, price in closing_prices.items():
                st.write(f"{ticker}: {price:.2f}")
        else:
            st.warning('No data available for the selected date or tickers.')

# Run the Streamlit app
if __name__ == '__main__':
    main()
