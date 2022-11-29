import datetime
import datetime as dt
from data_manager import DataManager
import requests
API_KEY = 'QldAgAPgeseNp1w1NXGMc5ybEodWgQ-q'
from notification_manager import NotificationManager

data_manager = DataManager()
class FlightSearch:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        pass

    def searchflight(self, flight_data):
        from_location = flight_data['from_code']
        to_location = flight_data['to_code']

        headers = {'apikey': API_KEY}
        today = dt.datetime.now()
        search_endpoint = 'https://tequila-api.kiwi.com/v2/search'
        tomorrow = today + datetime.timedelta(days=1)
        post_six_months = today + datetime.timedelta(days=180)
        flight_config = {'fly_from': from_location,
                         'fly_to': to_location,
                         'date_from': tomorrow.strftime('%d/%m/%Y'),
                         'date_to': post_six_months.strftime('%d/%m/%Y'),
                         'nights_in_dst_from': '7',
                         'nights_in_dst_to': '28',
                         'flight_type': 'round',
                         'max_stopovers': '0',
                         'limit':'1',
                         'curr':'INR'}
        response = requests.get(url=search_endpoint, params=flight_config, headers=headers)
        notification_manager = NotificationManager()
        min_price = flight_data['minimum_price']

        for flights in response.json()['data']:
            if float(flights['conversion']['INR']) < min_price:
                min_price = float(flights['conversion']['INR'])
                user_ids = flight_data['user_ids']
                mail_ids = data_manager.get_mails(user_ids)
                notification_manager.send_message(flights,mail_ids)
        print(min_price)

        return min_price

    def get_destination_code(self, city):
        headers = {'apikey': API_KEY}
        location_endpoint = 'https://tequila-api.kiwi.com/locations/query'
        location_config = {'term': city,
                           'location_types': 'city'}
        response = requests.get(url=location_endpoint, params=location_config, headers=headers)
        return response.json()['locations'][0]['code']
    def get_average_price(self,from_location,to_location,time):
        headers = {'apikey': API_KEY}
        search_endpoint = 'https://tequila-api.kiwi.com/v2/min-price'
        flight_config = {'fly_from': from_location,
                         'fly_to': to_location,
                         'date': time,
                         'nights_in_dst_from': '7',
                         'nights_in_dst_to': '28',
                         'flight_type': 'round',
                         'max_stopovers': '0',
                         'limit': '1',
                         'curr': 'INR'
                        }
        response = requests.get(url=search_endpoint, params=flight_config, headers=headers)
        return response.json()[0]

    def get_min_price(self,from_location,to_location):
        headers = {'apikey': API_KEY}
        today = dt.datetime.now()
        search_endpoint = 'https://tequila-api.kiwi.com/v2/search'
        tomorrow = today + datetime.timedelta(days=1)
        post_six_months = today + datetime.timedelta(days=180)
        flight_config = {'fly_from': from_location,
                         'fly_to': to_location,
                         'date_from': tomorrow.strftime('%d/%m/%Y'),
                         'date_to': post_six_months.strftime('%d/%m/%Y'),
                         'nights_in_dst_from': '7',
                         'nights_in_dst_to': '28',
                         'flight_type': 'round',
                         'max_stopovers': '0',
                         'curr': 'INR',
                         'limit':'1'}
        response = requests.get(url=search_endpoint, params=flight_config, headers=headers)

        for flights in response.json()['data']:
            print(float(flights['conversion']['INR']))
            return float(flights['conversion']['INR'])


