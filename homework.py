import logging
import os
import time

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
VK_API_VERSION = os.getenv('vk_api_version')
ACCESS_TOKEN = os.getenv('access_token')
ACCOUNT_SID = os.getenv('account_sid')
AUTH_TOKEN = os.getenv('auth_token')
NUMBER_FROM = os.getenv('NUMBER_FROM')
NUMBER_TO = os.getenv('NUMBER_TO')
client = Client(ACCOUNT_SID, AUTH_TOKEN)
URL = 'https://api.vk.com/method/'


def get_status(user_id):
    params = {
        'user_ids': user_id,
        'v': VK_API_VERSION,
        'access_token': ACCESS_TOKEN,
        'fields': 'online'
    }
    url = f'{URL}users.get'
    try:
        status = requests.post(url=url, params=params)
        return status.json()['response'][0]['online']
    except Exception as e:
        logging.exception(f'Ошибка: {e}')


def sms_sender(sms_text):
    message = client.messages.create(
        body=sms_text,
        from_=NUMBER_FROM,
        to=NUMBER_TO
    )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
