import re

# Define the entities to be labeled
entities = [
    "bed", "chair", "sofa", "table", "desk", "wardrobe", "dresser", "nightstand", "bookcase", "ottoman",
    "bench", "dining table", "coffee table", "side table", "console table", "TV stand", "bar stool",
    "counter stool", "recliner", "chaise lounge", "loveseat", "sectional sofa", "futon", "murphy bed",
    "rocking chair", "armchair", "accent chair", "lounge chair", "office chair", "patio furniture",
    "baby crib", "changing table", "high chair", "vanity table", "hall tree", "sideboard", "buffet", "cabinet",
    "shelving unit", "filing cabinet", "counter height table", "pub table", "breakfast nook", "kitchen island",
    "bar cabinet", "wine rack", "coat rack", "entryway bench", "shoe rack", "magazine rack", "plant stand",
    "vanity stool", "makeup vanity", "jewelry armoire", "fireplace mantel", "grandfather clock", "piano bench",
    "home bar", "pool table", "ping pong table", "foosball table", "poker table", "massage chair",
    "bean bag chair", "hammock", "swing chair", "murphy desk", "computer desk", "gaming desk", "standing desk",
    "L-shaped desk", "secretary desk", "drafting table", "trestle table", "conference table"
]

# Read the original text from the file
with open("input_file.txt", "r", encoding="utf-8") as file:
    original_text = file.readlines()

# Initialize a list to store modified lines
modified_lines = []

# Iterate over each line in the original text
for line in original_text:
    # Append the original line to the modified lines list
    modified_lines.append(line.strip())
    # Check if the line contains any entity matches
    for entity in entities:
        # Create a regular expression pattern for the entity
        pattern = re.compile(re.escape(entity), re.IGNORECASE)
        # Find all occurrences of the entity in the line
        matches = pattern.finditer(line)
        # Iterate over each match and append the modified lines with entity indices and "PRODUCT"
        for match in matches:
            start_index, end_index = match.span()
            # Append the modified lines with entity indices and "PRODUCT" to the list
            modified_lines.append(f"({start_index}, {end_index}, 'PRODUCT')")

# Write the modified lines to a new file
with open("output_file.txt", "w", encoding="utf-8") as file:
    for line in modified_lines:
        file.write(f"{line}\n")
