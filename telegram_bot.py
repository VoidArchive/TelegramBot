import api
import requests

def send_message_to_telegram(message):
    api_key = api.API_KEY
    group_id = api.group_id

    # https://api.telegram.org/bot<token>/sendMessage?chat_id=<group chat id >&text=<our text>
    parameters = {
        "chat_id":group_id,
        "text":message
    }
    tele_endpoint = "https://api.telegram.org/bot"
    msg = "/sendMessage"
    response = requests.get(f"{tele_endpoint}{api_key}{msg}",params=parameters)
    response.raise_for_status()

send_message_to_telegram("HelLo")
