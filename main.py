import requests
# import telegram_bot as void
import user

icon_dict = {
    "clear sky": "☀️",
    "few clouds": "🌤️",
    "scattered clouds": "☁️" ,
    "broken clouds": "🌫️" ,
    "shower rain": "🌦️",
    "rain": "🌧️",
    "thunderstorm": "⛈️" ,
    "snow": "🌨️",
    "mist": "🌁"
}



open_weather_api_end_point = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat" : user.my_lat,
    "lon" : user.my_lon,
    "exclude":"current,minutely,daily",
    "appid": user.ow_apikey
}
def get_current_weather():
    response = requests.get(open_weather_api_end_point,params=parameters)
    response.raise_for_status()
    data = response.json()
    weather_data = data["hourly"][:12]
    weather_description = [hour_data["weather"][0]["description"] for hour_data in weather_data]
    icon_dict = {
    "clear sky": "🌞",
    "few clouds": "🌤️",
    "scattered clouds": "🌥️" ,
    "broken clouds": "🌫️" ,
    "shower rain": "🌦️",
    "rain": "🌧️",
    "thunderstorm": "⛈️" ,
    "snow": "🌨️",
    "mist": "🌁"
}
    weather_emo = [icon_dict[i] for i in weather_description]
    
    return "  " .join(weather_emo)



print(get_current_weather())