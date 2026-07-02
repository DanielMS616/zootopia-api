import requests


API_KEY = ""
API_URL = "https://api.api-ninjas.com/v1/animals"


def main():
    """
    Send a test request to the Animals API and print the response.
    """

    animal_name = "Fox"

    # Query parameters are sent with params in a GET request.
    params = {
        "name": animal_name,
    }

    # The API key is sent in the request headers.
    headers = {
        "X-Api-Key": API_KEY,
    }

    # Send the GET request to the API.
    response = requests.get(API_URL, params=params, headers=headers)

    # Print the status code to check if the request was successful.
    print(response.status_code)

    # Convert the JSON response into Python data.
    animals = response.json()

    # Print the Python data.
    print(animals)


if __name__ == "__main__":
    main()