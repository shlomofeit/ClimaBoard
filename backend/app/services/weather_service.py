import requests


def get_coordinates(city: str):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 10,
    }

    response = requests.get(url, params=params)

    response.raise_for_status()

    data = response.json()

    result = data.get("results")

    if not result:
        return None

    cities_list = []
    for city in result:
        cities_list.append(
            {
                "id": city.get("id"),
                "name": city.get("name"),
                "country": city.get("country"),
                "latitude": city.get("latitude"),
                "longitude": city.get("longitude"),
            }
        )

    return cities_list


def get_current_weather(lat: float, lon: float):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current": [
            "temperature_2m",
            "precipitation",
            "relative_humidity_2m",
            "wind_speed_10m",
        ],
    }

    respons = requests.get(url, params=params)

    respons.raise_for_status()

    result = respons.json()

    current = result.get("current")
    units = result.get("current_units")

    return {
        "temperature": f"{current.get("temperature_2m")} {units.get("temperature_2m")}",
        "precipitation": f"{current.get("precipitation")} {units.get("precipitation")}",
        "relative_humidity": f"{current.get("relative_humidity_2m")} {units.get("relative_humidity_2m")}",
        "wind_speed": f"{current.get("wind_speed_10m")} {units.get("wind_speed_10m")}",
    }


def get_forecast_weather(lat: float, lon: float):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": [
            "temperature_2m",
            "precipitation",
            "relative_humidity_2m",
            "wind_speed_10m",
        ],
    }

    respons = requests.get(url, params=params)

    respons.raise_for_status()

    result = respons.json()

    daily = result.get("daily")

    if not daily:
        return []

    times = daily.get("time")
    temp_min = daily.get("temperature_2m_min")
    temp_max = daily.get("temperature_2m_max")

    forecast_list = []
    for i in range(len(times)):
        forecast_list.append(
            {"date": times[i], "temp_min": temp_min[i], "temp_max": temp_max[i]}
        )

    return forecast_list
