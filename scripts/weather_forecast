import argparse
import requests

class WeatherForecast:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_current_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            print(f"Current Weather in {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Description: {data['weather'][0]['description']}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        else:
            print(f"Error: {data['message']}")

    def get_weather_forecast(self, city):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == "200":
            print(f"Weather Forecast for {city} (next 5 days):")
            for forecast in data['list']:
                date = forecast['dt_txt']
                temp = forecast['main']['temp']
                description = forecast['weather'][0]['description']
                print(f"{date}: {temp}°C, {description}")
        else:
            print(f"Error: {data['message']}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Weather Forecast CLI')
    parser.add_argument('api_key', help='OpenWeatherMap API key')
    parser.add_argument('city', help='City name for weather forecast')

    args = parser.parse_args()

    weather_forecast = WeatherForecast(args.api_key)
    weather_forecast.get_current_weather(args.city)
    weather_forecast.get_weather_forecast(args.city)
