'''Now you're going to put together some of the ideas from previous exercises, 
and allow users to tell your bot about what they do and what they don't want, split across multiple messages.

The negated_ents() function has already been defined for you.
Additionally, a slightly tweaked version of the find_hotels() function, which accepts a neg_params dictionary in addition to a params dictionary, has been defined.'''
#TASK
# Define a respond() function which accepts a message, params, and neg_params as arguments.
# Use the negated_ents() function with message and ent_vals and store the result in negated.
# Use the tweaked find_hotels() function with the params and neg_params dictionaries to find matching hotels.
# Initialize the params and neg_params dictionary outside the respond() function and hit 'Submit Answer' to see the bot's responses!

# Define the respond function
def ____:
    # Extract the entities
    entities = interpreter.parse(message)["entities"]
    ent_vals = [e["value"] for e in entities]
    # Look for negated entities
    negated = ____
    for ent in entities:
        if ent["value"] in negated and negated[ent["value"]]:
            neg_params[ent["entity"]] = str(ent["value"])
        else:
            params[ent["entity"]] = str(ent["value"])
    # Find the hotels
    results = ____
    names = [r[0] for r in results]
    n = min(len(results),3)
    # Return the correct response
    return responses[n].format(*names), params, neg_params

# Initialize params and neg_params
params = ____
neg_params = ____

# Pass the messages to the bot
for message in ["I want a cheap hotel", "but not in the north of town"]:
    print("USER: {}".format(message))
    response, params, neg_params = respond(message, params, neg_params)
    print("BOT: {}".format(response))




#SOLUTION
# Define the respond function
def respond(message, params, neg_params):
    # Extract the entities
    entities = interpreter.parse(message)["entities"]
    ent_vals = [e["value"] for e in entities]
    # Look for negated entities
    negated = negated_ents(message, params)
    for ent in entities:
        if ent["value"] in negated and negated[ent["value"]]:
            neg_params[ent["entity"]] = str(ent["value"])
        else:
            params[ent["entity"]] = str(ent["value"])
    # Find the hotels
    results = find_hotels(params, neg_params)
    names = [r[0] for r in results]
    n = min(len(results),3)
    # Return the correct response
    return responses[n].format(*names), params, neg_params

# Initialize params and neg_params
params = {}
neg_params = {}

# Pass the messages to the bot
for message in ["I want a cheap hotel", "but not in the north of town"]:
    print("USER: {}".format(message))
    response, params, neg_params = respond(message, params, neg_params)
    print("BOT: {}".format(response))
