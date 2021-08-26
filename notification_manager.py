# TWILIO_ID = 'ACbbe0210ffe0b814b3fb0d719fe0a4349'
# TWILIO_KEY = 'ab147313b8d403a4593b151d95a9bb7a'
# from twilio.rest import Client
MY_MAIL_ID = 'shivangrawatiitism@gmail.com'
PAASSWORD = 'tyagi@25dec'
import smtplib

class NotificationManager:
# This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_message(self, flight,mail_ids):

        message = f"Low price alert! Only GBP {flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "
        f"{flight.destination_city}-{flight.destination_airport}," f" from {flight.out_date} to {flight.return_date}.\n\n"
        f"\nyou can book the flight using the link\n "
# and a link
        f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*"
        f"{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        for mail_id in mail_ids:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_MAIL_ID, password=PAASSWORD)
                connection.sendmail(from_addr=MY_MAIL_ID, to_addrs=mail_id, msg='Subject:Flight deal alert'
                                                                                      f'\n\n{message} ')

    # account_sid = TWILIO_ID
    # auth_token = TWILIO_KEY
    # from_date = flight_info['route'][0]['utc_arrival'].split('T')[0]
    # to_date = flight_info['route'][1]['utc_arrival'].split('T')[0]
    #
    # client = Client(account_sid, auth_token)
    #
    # message = client.messages \
    #     .create(
    #     body=f"Low prise alert!!!!only GBP {flight_info['conversion']['GBP']} to fly from {flight_info['cityFrom']}"
    #          f"{flight_info['flyFrom']}  to {flight_info['cityTo']} {flight_info['flyTo']}"
    #          f",from {from_date} to {to_date}",
    #     from_='+18589433342',
    #     to='+917726098384'
    # )
    # print(message.status)
