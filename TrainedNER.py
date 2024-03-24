import spacy

# Load the trained NER model
nlp = spacy.load("C:/Users/Sorin/PycharmProjects/Ner/trained_ner_model")

# Read the text from the input file
with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Initialize a set to store unique entities
unique_entities = set()

# Process each line with the NER model
for line in lines:
    # Process the text with the NER model
    doc = nlp(line.strip())

    # Check if the model is loaded properly
    if not nlp.has_pipe("ner"):
        print("Error: NER component not found in the loaded model.")
        exit()

    # Extract unique entities from the processed text
    entities = {(ent.text, ent.label_) for ent in doc.ents}

    # Add unique entities to the set
    unique_entities.update(entities)

# Print the unique entities
print("Unique Entities found:")
for entity, label in unique_entities:
    print(f"Entity: {entity}")
