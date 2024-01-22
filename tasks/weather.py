import random

from utils import request

ignore_letters = ("!", "?", ",", ".")


def run(args, response: str):

    args = [w for w in args if w not in ignore_letters]

    dataCity = request.get(
        f'https://geocoding-api.open-meteo.com/v1/search?name={args[-1]}&count=1&language=en&format=json')
    city = dataCity["results"][0]

    dataWeather = request.get(
        f'https://api.open-meteo.com/v1/forecast?latitude={city["latitude"]}&longitude={city["longitude"]}&hourly=temperature_2m&timezone={city["timezone"]}')
    return random.choice(response).replace("[city]", args[-1]).replace("[temperature]", str(dataWeather["hourly"]["temperature_2m"][-1]))
