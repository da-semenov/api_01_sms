import os
import time

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


def get_status(user_id):
    params = {
        'user_ids': user_id,
        'v': 5.92,
        'access_token': os.getenv('access_token'),
        'fields': 'online'
    }
    url = 'https://api.vk.com/method/users.get'
    status = requests.post(url=url, params=params)
    return status.json()['response'][0]['online']


def sms_sender(sms_text):
    account_sid = os.getenv('account_sid')
    auth_token = os.getenv('auth_token')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='The user we need online!',
        from_=os.getenv('NUMBER_FROM'),
        to=os.getenv('NUMBER_TO')
    )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
