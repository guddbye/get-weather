from flask import Flask, render_template
import requests

app = Flask(__name__)

# Replace with your weather API URL
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Replace with your OpenWeatherMap API key
API_KEY = "d0eff8ebebd5c7b7cba5635389a1c486"

@app.route('/')
def index():
    city = "New York"  # Replace with the city you want to get weather for
    weather_data = get_weather(city)
    return render_template('index.html', weather=weather_data)

def get_weather(city):
    url = WEATHER_API_URL.format(city=city, api_key=API_KEY)
    response = requests.get(url)
    data = response.json()
    weather = {
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    }
    return weather

if __name__ == '__main__':
    app.run(debug=True)
