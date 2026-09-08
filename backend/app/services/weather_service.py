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
