'''In this exercise you'll use spaCy's powerful syntax parser to assign roles to the entities in your users' messages.
 To do this, you'll define two functions, find_parent_item() and assign_colors(). In doing so, you'll use a parse tree to assign roles, similar to how Alan did in the video.

Recall that you can access the ancestors of a word using its .ancestors attribute.'''
#TASK
# Create a spaCy document called doc by passing the message "let's see that jacket in red and some blue jeans" to the nlp object.
# In the find_parent_item(word) function, iterate over the ancestors of each word until an entity_type of "item" is found.
# In the assign_colors(doc) function, iterate over the doc until an entity_type of "color" is found. Then, find the parent item of this word.
# Pass in the spaCy document to the assign_colors() function.

# Create the document
doc = ____

# Iterate over parents in parse tree until an item entity is found
def find_parent_item(word):
    # Iterate over the word's ancestors
    for parent in ____:
        # Check for an "item" entity
        if entity_type(____) == "____":
            return parent.text
    return None

# For all color entities, find their parent item
def assign_colors(doc):
    # Iterate over the document
    for word in ____:
        # Check for "color" entities
        if entity_type(word) == "____":
            # Find the parent
            item =  ____
            print("item: {0} has color : {1}".format(item, word))

# Assign the colors
____ 





#SOLUTION
# Create the document
doc = nlp("let's see that jacket in red and some blue jeans")

# Iterate over parents in parse tree until an item entity is found
def find_parent_item(word):
    # Iterate over the word's ancestors
    for parent in word.ancestors:
        # Check for an "item" entity
        if entity_type(parent) == "item":
            return parent.text
    return None

# For all color entities, find their parent item
def assign_colors(doc):
    # Iterate over the document
    for word in doc:
        # Check for "color" entities
        if entity_type(word) == "color":
            # Find the parent
            item =  find_parent_item(word)
            print("item: {0} has color : {1}".format(item, word))

# Assign the colors
assign_colors(doc)
