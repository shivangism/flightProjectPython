import urllib
from pymongo import MongoClient


# SHEETY_ENDPOINT = 'https://api.sheety.co/bdcd63f97245eb0bfa656da3c719d3f8/flightDeals/prices'
DBURI = f'mongodb+srv://{urllib.parse.quote_plus("shivangism2")}:{urllib.parse.quote_plus("tyagi25")}@cluster0.qjm1u.mongodb.net/flightDb?retryWrites=true&w=majority'
client = MongoClient(DBURI)
db = client.flightDb
flights_collection = db.flights
user_collection = db.users


class DataManager:
    # This class is responsible for talking to the DB.
    def __init__(self):
        pass

    # def update_sheet(self, sheet_data):
    #     for row in sheet_data:
    #         put_config = {'price': {
    #             'iataCode': row['iataCode']
    #         }}
    #         put_url = f'{SHEETY_ENDPOINT}/{row["id"]}'
    #         response = requests.put(put_url, json=put_config)
    #         print(response.json());
    def set_flight(self,from_code,to_code,minimum_price,flight):
        flights_collection.update_one({'from': flight['from'],'to': flight['to']}, {'$set': {'from_code':from_code,
                                                                   'to_code':to_code,
                                                                   'minimum_price':minimum_price}})


    def get_mails(self,user_ids):
        mail_ids = []
        for user_id in user_ids:
            user = user_collection.find_one({'_id':user_id})
            mail_ids.append(user['username'])
        return  mail_ids


    def all_flights(self):
        return flights_collection.find()


