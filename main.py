# This is a sample Python script.
from fetch_api import FetchApi
from connector import Connector
import connector
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db = Connector()
    # db.get_connection()
    # db.close_connection()
    api_key = '61ad4b5218580e550f21ab6091b01593'
    historical_url = f'https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/AAPL?apikey={api_key}'
    historical_api = FetchApi(historical_url)
    data = historical_api.get_request('historical')
    db.store_historical(data)
    db.close_connection()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
