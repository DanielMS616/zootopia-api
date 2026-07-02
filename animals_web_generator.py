import json
import requests


API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = ""


def get_animals_from_api(animal_name):
    """
    Get animal data from the API Ninjas Animals API.
    The animal name is sent as a GET parameter.
    The API key is sent in the request headers.
    """

    params = {
        "name": animal_name,
    }

    headers = {
        "X-Api-Key": API_KEY,
    }

    response = requests.get(API_URL, params=params, headers=headers)

    # Convert the JSON response into Python data.
    animals_data = response.json()

    return animals_data


def load_data(file_path):
    """Loads a JSON file."""

    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_skin_types(animals_data):
    """Returns all available skin types"""

    skin_types = []

    for animal in animals_data:
        if "characteristics" in animal:
            characteristics = animal["characteristics"]

            if "skin_type" in characteristics:
                skin_type = characteristics["skin_type"]

                if skin_type not in skin_types:
                    skin_types.append(skin_type)

    return skin_types


def get_user_skin_type(skin_types):
    """Asks the user to enter a valid skin type"""

    print("Available skin types:")

    for skin_type in skin_types:
        print(skin_type)

    print("All")
    print()
    print("Enter all to show all animals.")
    print("Enter q to quit.")
    print()

    while True:
        selected_skin_type = input("Enter a skin type: ")
        selected_skin_type = selected_skin_type.strip()

        if selected_skin_type == "":
            print("No skin type entered. Please try again.")

        elif selected_skin_type.isdigit():
            print("Numbers are not valid. Please enter a skin type.")

        elif selected_skin_type.lower() == "q":
            print("Program stopped.")
            return "quit"

        elif selected_skin_type.lower() == "quit":
            print("Program stopped.")
            return "quit"

        elif selected_skin_type.lower() == "all":
            return "all"

        else:
            for skin_type in skin_types:
                if selected_skin_type.lower() == skin_type.lower():
                    return skin_type

            print("No matching skin type found. Please try again.")


def serialize_animal(animal_obj):
    """Converts one animal object into HTML"""

    output = ""
    output += '<li class="cards__item">\n'

    if "name" in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

    output += '  <div class="card__text">\n'
    output += '    <ul class="card__list">\n'

    if "characteristics" in animal_obj:
        if "diet" in animal_obj["characteristics"]:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Diet:</strong> '
                f'{animal_obj["characteristics"]["diet"]}</li>\n'
            )

    if "locations" in animal_obj:
        if len(animal_obj["locations"]) > 0:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Location:</strong> '
                f'{animal_obj["locations"][0]}</li>\n'
            )

    if "characteristics" in animal_obj:
        if "type" in animal_obj["characteristics"]:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Type:</strong> '
                f'{animal_obj["characteristics"]["type"]}</li>\n'
            )

    if "characteristics" in animal_obj:
        if "lifespan" in animal_obj["characteristics"]:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Lifespan:</strong> '
                f'{animal_obj["characteristics"]["lifespan"]}</li>\n'
            )

    if "characteristics" in animal_obj:
        if "weight" in animal_obj["characteristics"]:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Weight:</strong> '
                f'{animal_obj["characteristics"]["weight"]}</li>\n'
            )

    if "characteristics" in animal_obj:
        if "top_speed" in animal_obj["characteristics"]:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Top Speed:</strong> '
                f'{animal_obj["characteristics"]["top_speed"]}</li>\n'
            )

    if "characteristics" in animal_obj:
        if "skin_type" in animal_obj["characteristics"]:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Skin Type:</strong> '
                f'{animal_obj["characteristics"]["skin_type"]}</li>\n'
            )

    output += "    </ul>\n"
    output += "  </div>\n"
    output += "</li>\n"

    return output


def main():
    """Generates an HTML page for animals selected by the user."""

    # Ask the user which animal should be searched in the API.
    animal_name = input("Enter a name of an animal: ")
    animal_name = animal_name.strip()

    # Get the animal data from the API using the user's input.
    animals_data = get_animals_from_api(animal_name)

    output = ""

    # If the API returns an empty list, no animal was found.
    if animals_data == []:
        output += '<li class="cards__item">\n'
        output += f'  <h2>Das Tier "{animal_name}" existiert nicht.</h2>\n'
        output += "</li>\n"

    else:
        # Create one HTML card for every animal returned by the API.
        for animal in animals_data:
            output += serialize_animal(animal)

    # Read the HTML template file.
    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        template = template_file.read()

    # Replace the placeholder in the template with the generated animal cards.
    new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    # Write the final HTML page to animals.html.
    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(new_html)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()