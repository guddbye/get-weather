import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Replace with your API key
API_KEY = 'b9fbe65155e64b90fce6dee912c4a9b1'

@app.route('/', methods=['GET', 'POST'])
def index():
    city = None
    weather = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather = get_weather(city)

    return render_template('index.html', city=city, weather=weather)

def get_weather(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=1&hour=6'
    response = requests.get(url)
    data = response.json()
    
    forecasts = []
    if 'forecast' in data and 'forecastday' in data['forecast'] and data['forecast']['forecastday']:
        for forecast in data['forecast']['forecastday'][0]['hour']:
            forecasts.append({
                'time': forecast['time'],
                'temp': forecast['temp_c'],
                'condition': forecast['condition']['text']
            })
    
    return forecasts[:6]  # Return the next six hours' forecast

# ... rest of your code ...


if __name__ == '__main__':
    app.run(debug=True)
