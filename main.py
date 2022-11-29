# This file will need to use the DataManager,FlightSearch, NotificationManager classes to achieve the program requirements.
import requests

from flight_search import FlightSearch
from data_manager import DataManager
import datetime as dt

flight_search = FlightSearch()
data_manager = DataManager()

all_flights = data_manager.all_flights()

for flight in all_flights:

# setting new flis]ght
    if not 'to_key' in flight.keys():
        from_code = flight_search.get_destination_code(flight['from'])
        to_code = flight_search.get_destination_code(flight['to'])
        total_price = 0;
        today = dt.datetime.now();
        for t in range(1,31):
            total_price=total_price + flight_search.get_average_price(from_code, to_code,today - dt.timedelta(days=t))
        average_price=total_price/30;
        data_manager.set_flight(from_code,to_code,average_price,flight)
#or cheacking for deal

        flight_search.searchflight(flight)





# response = requests.get(SHEETY_ENDPOINT)
# sheet_data = response.json()['prices']


# flight_data = FlightData()
#
# for row in sheet_data:
#     row['lowestPrice'] = flight_data.searchflight(row)
#
# for row in sheet_data:
#     print(f'{row["city"]}:{row["lowestPrice"]}')
