import json


def load_data(file_path):
    """Loads a JSON file."""

    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")

for animal in animals_data:
    if "name" in animal:
        print(f"Name: {animal['name']}")

    if "characteristics" in animal:
        if "diet" in animal["characteristics"]:
            print(f"Diet: {animal['characteristics']['diet']}")

    if "locations" in animal:
        if len(animal["locations"]) > 0:
            print(f"Location: {animal['locations'][0]}")

    if "characteristics" in animal:
        if "type" in animal["characteristics"]:
            print(f"Type: {animal['characteristics']['type']}")

    print()