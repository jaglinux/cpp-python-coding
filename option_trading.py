import sys
import yfinance as yf
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
# Example list of top 100 NASDAQ stocks (replace this with your actual data)
top_nasdaq_stocks = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'NVDA', 'INTC', 'CSCO', 'AMD',
    'PYPL', 'NFLX', 'ADBE', 'AMAT', 'ATVI', 'AVGO', 'BIDU', 'BIIB', 'BMRN', 'CELG',
    'CTRP', 'CSX', 'EA', 'EBAY', 'EXPE', 'GILD', 'HAS', 'ILMN', 'INCY', 'LRCX',
    'MAR', 'MCHP', 'MU', 'MXIM', 'MYL', 'NTAP', 'NTES', 'ORLY', 'PCAR', 'PAYX',
    'PCLN', 'QCOM', 'REGN', 'ROST', 'SBUX', 'SHPG', 'SNPS', 'SWKS', 'SYMC', 'TMUS',
    'TXN', 'VRSK', 'VRSN', 'VRTX', 'WBA', 'WDAY', 'WDC', 'WYNN', 'XLNX', 'XRAY',
    'GOOG', 'CMCSA', 'BKNG', 'AMGN', 'CHTR', 'BABA', 'SBAC', 'COST', 'ASML', 'AMD',
    'ATVI', 'AVGO', 'BIDU', 'BIIB', 'CDNS', 'CERN', 'CHKP', 'CTAS', 'CSCO', 'CSX',
    'CTSH', 'DLTR', 'EA', 'EBAY', 'EXPE', 'FAST', 'FISV', 'FOXA', 'GILD', 'HAS',
    'HSIC', 'IDXX', 'ILMN', 'INCY', 'INTC', 'INTU', 'ISRG', 'JBHT', 'JD', 'KLAC',
]


def get_all_tickers():
    print("Calling get_all_tickers")
    url = 'https://www.nasdaq.com/market-activity/stocks/screener'
    response = requests.get(url)
    print(1)
    # Use pandas to extract the table data
    df = pd.read_html(response.text, header=0)[0]
    print(2)
    # Extract tickers from the 'Symbol' column
    tickers = df['Symbol'].head(100).tolist()
    
    return tickers

def get_call_options(symbol, expiration_date, max_premium):
    stock = yf.Ticker(symbol)
    options = stock.option_chain(expiration_date).calls
    selected_options = options[options['lastPrice'] < max_premium]
    
    return selected_options

def get_options(symbol = "nvda"):
    print(f"Calling get_options for ticker {symbol}")
    # Calculate expiration date one month from now
    today = datetime.today()
    expiration_date = today + timedelta(days=30)
    
    # Format expiration date as 'YYYY-MM-DD'
    #expiration_date_str = expiration_date.strftime('%Y-%m-%d')
    expiration_date_str = "2023-12-08"
    
    # Set the maximum premium for the options
    max_premium = 10
    
    # Get call options
    call_options = get_call_options(symbol, expiration_date_str, max_premium)
    
    # Print the selected call options
    print(f"Call options for {symbol} expiring on {expiration_date_str} with premium less than ${max_premium}:")
    print(call_options)

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 1:
        get_options()
    else:
        if sys.argv[1] == '0':
            stocks = get_all_tickers()
            print(stocks)
        elif sys.argv[1] == '1':
            #stocks = get_all_tickers()
            stocks = top_nasdaq_stocks
            print(stocks)
            for stock in stocks:
                get_options(stock)
        elif sys.argv[1] == '2':
            get_options(sys.argv[2])
        else:
            print("not defined")
        
        
