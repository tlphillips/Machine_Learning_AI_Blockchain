'''In this exercise you'll use spaCy's built-in entity recognizer to extract names, dates, and organizations from search queries. 
The spaCy library has been imported for you, and it's English model has been loaded as nlp.

Your job is to define a function called extract_entities() which takes in a single argument message and returns a dictionary with the included entity types as keys, and the extracted entities as values. 
The included entity types are contained in a list called include_entities.'''
#TASK
# Create a dictionary called ents to hold the entities by calling dict.fromkeys() with include_entities as the sole argument.
# Create a spacy document called doc by passing the message to the nlp object.
# Iterate over the entities in the document (doc.ents).
# Check whether the entity's .label_ is one we are interested in. If so, assign the entity's .text attribute to the corresponding key in the ents dictionary.

# Define included entities
include_entities = ['DATE', 'ORG', 'PERSON']

# Define extract_entities()
def extract_entities(message):
    # Create a dict to hold the entities
    ents = ____
    # Create a spacy document
    doc = ____
    for ent in ____:
        if ____ in ____:
            # Save interesting entities
            ents[____] = ____
    return ents

print(extract_entities('friends called Mary who have worked at Google since 2010'))
print(extract_entities('people who graduated from MIT in 1999'))




#SOLUTION
# Define included entities
include_entities = ['DATE', 'ORG', 'PERSON']

# Define extract_entities()
def extract_entities(message):
    # Create a dict to hold the entities
    ents = dict.fromkeys(include_entities)
    # Create a spacy document
    doc = nlp(message)
    for ent in doc.ents:
        if ent.label_ in include_entities:
            # Save interesting entities
            ents[ent.label_] = ent.text
    return ents

print(extract_entities('friends called Mary who have worked at Google since 2010'))
print(extract_entities('people who graduated from MIT in 1999'))
