'''Quite often you'll find your users telling you what they don't want - and that's important to understand! In general, negation is a difficult problem in NLP.
 Here we'll take a very simple approach that works for many cases.

A list of tests called tests has been defined for you. Explore it in the Shell - you'll find that each test is a tuple consisting of:

A string containing a message with entities
A dictionary containing the entities as keys, and a Boolean saying whether they are negated as the key
Your job is to define a function called negated_ents() which looks for negated entities in a message.'''

#TASK
# Define negated_ents()
def negated_ents(phrase):
    # Extract the entities using keyword matching
    ents = [e for e in ["____", "____"] if e in phrase]
    # Find the index of the final character of each entity
    ends = sorted([____ + ____ for e in ents])
    # Initialise a list to store sentence chunks
    chunks = []
    # Take slices of the sentence up to and including each entitiy
    start = 0
    for end in ends:
        chunks.____(phrase[____:____])
        start = end
    result = {}
    # Iterate over the chunks and look for entities
    for chunk in chunks:
        for ent in ents:
            if ent in chunk:
                # If the entity is preceeded by a negation, give it the key False
                if "not" in chunk or "n't" in chunk:
                    result[ent] = ____
                else:
                    result[ent] = ____
    return result  

# Check that the entities are correctly assigned as True or False
for test in tests:
    print(negated_ents(test[0]) == test[1])





#SOLUTION
# Define negated_ents()
def negated_ents(phrase):
    # Extract the entities using keyword matching
    ents = [e for e in ["south", "north"] if e in phrase]
    # Find the index of the final character of each entity
    ends = sorted([phrase.index(e) + len(e) for e in ents])
    # Initialise a list to store sentence chunks
    chunks = []
    # Take slices of the sentence up to and including each entitiy
    start = 0
    for end in ends:
        chunks.append(phrase[start:end])
        start = end
    result = {}
    # Iterate over the chunks and look for entities
    for chunk in chunks:
        for ent in ents:
            if ent in chunk:
                # If the entity is preceeded by a negation, give it the key False
                if "not" in chunk or "n't" in chunk:
                    result[ent] = False
                else:
                    result[ent] = True
    return result  

# Check that the entities are correctly assigned as True or False
for test in tests:
    print(negated_ents(test[0]) == test[1])
