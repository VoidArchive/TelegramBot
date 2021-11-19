import requests
import telegram_bot as void
import details

open_weather_api_end_point = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat" : details.my_lat,
    "lon" : details.my_lon,
    "exclude":"current,minutely,daily",
    "appid": details.ow_apikey
}
def get_current_weather():
    response = requests.get(open_weather_api_end_point,params=parameters)
    response.raise_for_status()
    data = response.json()
    weather_data = data["hourly"][:12]
    weather = [hour_data["weather"][0]["id"] for hour_data in weather_data]
    avg_wid = sum(weather)/len(weather)
    message = ''
    if avg_wid > 800:
        message = "Today's weather is going to as clear as sky. Enjoy Your Day!"
    elif avg_wid > 700:
        message = "It's won't be sunny but you won't have to worry about the rain for today."
    elif avg_wid >600:
        message = "It's going to be cold. Wear warm clothes"
    elif avg_wid >= 500:
        message = "Might be your favorite Day. It might to rain."
    elif avg_wid < 500:
        message = "Stay Home, Or have a umbrella with your at all times. We are going to have a heavy rain."
    else:
        message = "Weather forecast error."

    return message
# 800 = clear sky
# 800 > Cloudy
# 700 > Misty/Cloudy
# 600 > Snow
# 500 > Rain
message = get_current_weather()
void.send_message_to_telegram(message)