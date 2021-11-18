import details
import requests

def send_message_to_telegram(message):
    api_key = details.API_KEY
    group_id = details.group_id

    # https://api.telegram.org/bot2146001890:AAFqdKoiF3ftzz4QM1LtREfUxe0aJ1aX9Xc/getUpdates
    # https://api.telegram.org/bot<token>/sendMessage?chat_id=<group chat id >&text=<our text>
    parameters = {
        "chat_id":group_id,
        "text":message
    }
    tele_endpoint = "https://api.telegram.org/bot"
    msg = "/sendMessage"
    response = requests.get(f"{tele_endpoint}{api_key}{msg}",params=parameters)
    response.raise_for_status()
