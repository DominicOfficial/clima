from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Coordinates for all 47 counties in Kenya
COUNTY_COORDINATES = {
    "Nairobi": {"latitude": -1.286389, "longitude": 36.817223},
    "Mombasa": {"latitude": -4.043477, "longitude": 39.668206},
    "Kisumu": {"latitude": -0.091702, "longitude": 34.767956},
    "Nakuru": {"latitude": -0.303099, "longitude": 36.080025},
    "Eldoret": {"latitude": 0.514277, "longitude": 35.269779},
    "Thika": {"latitude": -1.03326, "longitude": 37.06933},
    "Nyeri": {"latitude": -0.416667, "longitude": 36.950001},
    "Meru": {"latitude": 0.04626, "longitude": 37.65587},
    "Garissa": {"latitude": -0.456944, "longitude": 39.658333},
    "Machakos": {"latitude": -1.5177, "longitude": 37.2634},
    "Mandera": {"latitude": 3.9373, "longitude": 41.8569},
    "Wajir": {"latitude": 1.7500, "longitude": 40.0667},
    "Isiolo": {"latitude": 0.3546, "longitude": 37.5822},
    "Marsabit": {"latitude": 2.3333, "longitude": 37.9833},
    "Turkana": {"latitude": 3.1167, "longitude": 35.8500},
    "West Pokot": {"latitude": 1.2389, "longitude": 35.1214},
    "Samburu": {"latitude": 1.8028, "longitude": 36.8219},
    "Trans Nzoia": {"latitude": 1.0167, "longitude": 35.0000},
    "Uasin Gishu": {"latitude": 0.5143, "longitude": 35.2698},
    "Elgeyo-Marakwet": {"latitude": 0.4708, "longitude": 35.3956},
    "Nandi": {"latitude": 0.1200, "longitude": 35.2500},
    "Baringo": {"latitude": 0.4667, "longitude": 36.0833},
    "Laikipia": {"latitude": 0.5167, "longitude": 37.0667},
    "Nyandarua": {"latitude": -0.1667, "longitude": 36.3667},
    "Kirinyaga": {"latitude": -0.5000, "longitude": 37.2833},
    "Embu": {"latitude": -0.5333, "longitude": 37.4500},
    "Kitui": {"latitude": -1.3667, "longitude": 38.0167},
    "Tana River": {"latitude": -1.5000, "longitude": 40.0000},
    "Lamu": {"latitude": -2.2717, "longitude": 40.9020},
    "Taita-Taveta": {"latitude": -3.3167, "longitude": 38.3667},
    "Kwale": {"latitude": -4.1833, "longitude": 39.4500},
    "Kilifi": {"latitude": -3.6333, "longitude": 39.8500},
    "Homa Bay": {"latitude": -0.5167, "longitude": 34.4500},
    "Migori": {"latitude": -1.0667, "longitude": 34.4667},
    "Kisii": {"latitude": -0.6833, "longitude": 34.7667},
    "Nyamira": {"latitude": -0.5667, "longitude": 34.9333},
    "Siaya": {"latitude": 0.0600, "longitude": 34.2883},
    "Busia": {"latitude": 0.4344, "longitude": 34.2422},
    "Bungoma": {"latitude": 0.5667, "longitude": 34.5667},
    "Vihiga": {"latitude": 0.0833, "longitude": 34.7333},
    "Kakamega": {"latitude": 0.2833, "longitude": 34.7500},
    "Kericho": {"latitude": -0.3667, "longitude": 35.2833},
    "Bomet": {"latitude": -0.7833, "longitude": 35.3500},
    "Narok": {"latitude": -1.0833, "longitude": 35.8667},
    "Kajiado": {"latitude": -1.8500, "longitude": 36.7833},
}

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City is required"}), 400

    # Check if the city is in the predefined coordinates
    if city not in COUNTY_COORDINATES:
        return jsonify({"error": f"{city} is not a valid county or not supported"}), 400

    # Get latitude and longitude for the city
    lat, lon = COUNTY_COORDINATES[city]["latitude"], COUNTY_COORDINATES[city]["longitude"]

    # Open-Meteo API URL
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(weather_url)

    if response.status_code != 200:
        return jsonify({"error": "API error"}), response.status_code

    # Parse the weather data
    weather_data = response.json()
    simplified_data = {
        "city": city,
        "temperature": weather_data["current_weather"]["temperature"],
        "wind_speed": weather_data["current_weather"]["windspeed"],
        "description": "Current weather data",
    }
    return jsonify(simplified_data)

@app.route('/alerts', methods=['GET'])
def get_alerts():
    alerts = [
        {"title": "Heavy Rainfall Expected", "description": "Prepare for heavy rainfall in Nairobi."},
        {"title": "Strong Winds", "description": "Strong winds expected in Mombasa."},
    ]
    return jsonify(alerts)

@app.route('/news', methods=['GET'])
def get_news():
    news = [
        {"title": "Climate Change Impact", "description": "How climate change is affecting Kenya's weather."},
        {"title": "Flood Preparedness", "description": "Tips to prepare for floods during the rainy season."},
    ]
    return jsonify(news)

if __name__ == '__main__':
    app.run(debug=True)