# This is a sample Python script.
from fetch_api import FetchApi
from connector import Connector
import connector
def get_api(db,url,label):
    api = FetchApi(url)
    data = api.get_request(label)
    if label == 'historical':
        db.store_historical(data)
    else:
        db.store_delisted(data)
    # Use a breakpoint in the code line below to debug your script.
 # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db = Connector()
    api_key = '61ad4b5218580e550f21ab6091b01593'
    historical_url = f'https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/AAPL?apikey={api_key}'
    delisted_url = f'https://financialmodelingprep.com/api/v3/delisted-companies?page=0&apikey={api_key}'
    get_api(db,historical_url,'historical')
    get_api(db,delisted_url,'delisted')
    db.close_connection()

