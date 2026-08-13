import requests

from config import (
    THIRUKKURAL_API_BASE_URL,
    THIRUKKURAL_APP_ID
)


def get_kural(number):
    """
    Get a particular Thirukkural from the API.
    """

    url = f"{THIRUKKURAL_API_BASE_URL}/kural/{number}"

    params = {
        "appid": THIRUKKURAL_APP_ID,
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=10)

    response.raise_for_status()

    return response.json()


def get_random_kural():
    """
    Get a random Thirukkural from the API.
    """

    url = f"{THIRUKKURAL_API_BASE_URL}/kural/rnd"

    params = {
        "appid": THIRUKKURAL_APP_ID,
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=10)

    response.raise_for_status()

    return response.json()