import requests

APIkey = "d9c9b8f326b95316b1e7e8eca867e60a"


def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    filtered_data = filtered_data[:8 * days]
    location = data['city']
    return filtered_data, location
