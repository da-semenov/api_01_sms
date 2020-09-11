import time

import requests
from twilio.rest import Client


def get_status(user_id):
    params = {
        ...
    }
    ...
    return ...  # Верните статус пользователя в ВК


def sms_sender(sms_text):
    ...
    return ...  # Верните sid отправленного сообщения из Twilio


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
