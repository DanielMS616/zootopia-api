import os

import requests
from dotenv import load_dotenv


API_URL = "https://api.api-ninjas.com/v1/animals"

# Load the variables from the .env file.
load_dotenv()

# Read the API key from the environment.
API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
            ...
        },
        'locations': [
            ...
        ],
        'characteristics': {
            ...
        }
    }
    """

    # Stop the API request if no API key was found.
    if not API_KEY:
        print("API key is missing. Please add it to the .env file.")
        return None

    params = {
        "name": animal_name,
    }

    headers = {
        "X-Api-Key": API_KEY,
    }

    response = requests.get(API_URL, params=params, headers=headers)

    # If the API request failed, return None instead of animal data.
    if response.status_code != 200:
        print(f"API request failed with status code {response.status_code}.")
        return None

    # Convert the JSON response into Python data.
    animals_data = response.json()

    return animals_data
