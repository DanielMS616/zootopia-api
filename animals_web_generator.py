import data_fetcher


def serialize_animal(animal_obj):
    """Converts one animal object into HTML."""

    output = ""
    output += '<li class="cards__item">\n'

    if "name" in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

    output += '  <div class="card__text">\n'
    output += '    <ul class="card__list">\n'

    if "characteristics" in animal_obj:
        characteristics = animal_obj["characteristics"]

        if "diet" in characteristics:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Diet:</strong> '
                f'{characteristics["diet"]}</li>\n'
            )

        if "common_name" in characteristics:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Common Name:</strong> '
                f'{characteristics["common_name"]}</li>\n'
            )

        if "type" in characteristics:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Type:</strong> '
                f'{characteristics["type"]}</li>\n'
            )

        if "lifespan" in characteristics:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Lifespan:</strong> '
                f'{characteristics["lifespan"]}</li>\n'
            )

        if "weight" in characteristics:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Weight:</strong> '
                f'{characteristics["weight"]}</li>\n'
            )

        if "length" in characteristics:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Length:</strong> '
                f'{characteristics["length"]}</li>\n'
            )

        if "top_speed" in characteristics:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Top Speed:</strong> '
                f'{characteristics["top_speed"]}</li>\n'
            )

        if "skin_type" in characteristics:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Skin Type:</strong> '
                f'{characteristics["skin_type"]}</li>\n'
            )

        if "color" in characteristics:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Color:</strong> '
                f'{characteristics["color"]}</li>\n'
            )

        if "venomous" in characteristics:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Venomous:</strong> '
                f'{characteristics["venomous"]}</li>\n'
            )

        if "aggression" in characteristics:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Aggression:</strong> '
                f'{characteristics["aggression"]}</li>\n'
            )

    if "locations" in animal_obj:
        if len(animal_obj["locations"]) > 0:
            locations = ", ".join(animal_obj["locations"])

            output += (
                f'      <li class="card__list-item">'
                f'<strong>Locations:</strong> '
                f'{locations}</li>\n'
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
    animals_data = data_fetcher.fetch_data(animal_name)

    # If no data could be fetched, stop the program.
    # This is different from an empty list returned by the API.
    if animals_data is None:
        print("Website was not generated because the animal data could not be loaded.")
        return

    output = ""

    # If the API returns an empty list, no animal was found.
    if not animals_data:
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