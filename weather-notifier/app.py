from requests import get
from plyer import notification
import time

api_key = '773b2dcee13fd68fe49e6fcd94a7880d'

def fetch_weather_data():
    # Fetch location data
    data = get('https://ipinfo.io').json()
    lat, lon = data['loc'].split(",")

   
    weather_data = get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}').json()

   
    temp = round(weather_data['main']['temp'] - 273.15)
    feels_like = round(weather_data['main']['feels_like'] - 273.15)
    humidity = weather_data['main']['humidity']

    return temp, feels_like, humidity

def send_notification(temp, feels_like, humidity):
    notification.notify(
        title="Weather Update",
        app_icon='icon.ico',
        message=f"Temperature: {temp}°C\nFeels Like: {feels_like}°C\nHumidity: {humidity}%",
        timeout=10  # Notification will stay for 10 seconds
    )

while True:
    temp, feels_like, humidity = fetch_weather_data()
    send_notification(temp, feels_like, humidity)
    time.sleep(7200)  # Sleep for 2 hours (7200 seconds)
