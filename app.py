from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/weatherapp', methods=['POST', 'GET'])
def get_weather_data():
    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "d751762f4fd82552431f9d257ba2dbee"

    city = request.form.get("city")
    params = {
        'q': city,
        'appid': api_key,
        'units': "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        # Extract relevant weather information
        weather_description = data['weather'][0]['description'].capitalize()
        temperature = data['main']['temp']
        minimum_temp = data['main']['temp_min']
        maximum_temp = data['main']['temp_max']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        # Format the response for display
        result = f"Weather in {city}: {weather_description}, Temperature: {temperature}°C,\nMaximum Temp: {maximum_temp}°C, Minimum Temp: {minimum_temp}°C,\nHumidity: {humidity}%, Pressure: {pressure} mb"

    else:
        result = f"Error fetching weather data for {city}. Please check the city name and try again."

    return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
