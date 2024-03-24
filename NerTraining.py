import spacy
import random
from spacy.training import Example

# Load a blank English model
nlp = spacy.blank("en")

# Define the NER pipeline component
ner = nlp.add_pipe("ner")

# Read raw text from file
with open("raw_text.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

# Extracted furniture items
furniture_items = [
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

# Generate training data with annotations
TRAIN_DATA = []
for text in raw_text.split("\n"):
    for item in furniture_items:
        start_index = text.find(item)
        if start_index != -1:
            end_index = start_index + len(item)
            # Each furniture item is considered as a separate entity
            annotation = {"entities": [(start_index, end_index, "furniture")]}
            TRAIN_DATA.append((text, annotation))

# Add labels to the NER component
ner.add_label("furniture")

# Disable other pipeline components for training
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()
    for itn in range(10):  # Adjust the number of iterations as needed
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in TRAIN_DATA:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], drop=0.5, losses=losses)
        print(losses)

# Save the trained model
nlp.to_disk("trained_ner_model")
