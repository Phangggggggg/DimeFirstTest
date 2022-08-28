import requests
from requests.exceptions import HTTPError


class FetchApi:

    def __init__(self,url):
        super(FetchApi,self).__init__()
        self.url = url

    def get_request(self, label):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            status = response.status_code
            if (status == 200):
                data = response.json()
                if label == 'historical':
                     data = data[label]
                return data
            else:
                raise Exception(F'The status is {status}')
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6

