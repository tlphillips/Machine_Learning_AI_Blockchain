'''What happens if you make a suggestion to your user, and they don't like it? Your bot will look really silly if it makes the same suggestion again right away.

Here, you're going to modify your respond() function so that it accepts and returns 4 arguments:

The user message as an argument, and the bot response as the first return value.
A dictionary params including the entities the user has specified.
A suggestions list. When passed to respond(), this should contain the suggestions made in the previous bot message. When returned by respond(), it should contain the current suggestions.
An excluded list, which contains all of the results your user has already explicitly rejected.
Your function should add the previous suggestions to the excluded list whenever it receives a "deny" intent. It should also filter out excluded suggestions from the response.'''
#TASK
# Define a respond() function with 4 arguments: message, params, prev_suggestions, and excluded.
# The value of the "intent" key of parse_data is itself a dictionary of key-value pairs. Assign parse_data["intent"]["name"] to intent, and parse_data["entities"] to entities.
# If the intent is "deny", use the .extend() method of the excluded list to add prev_suggestions to it.
# Initialize the empty params dictionary and empty suggestions and excluded lists. Then, hit 'Submit Answer' to send the messages to the bot.

# Define respond()
def ____:
    # Interpret the message
    parse_data = ____
    # Extract the intent
    intent = ____
    # Extract the entities
    entities = ____
    # Add the suggestion to the excluded list if intent is "deny"
    if ____ == "____":
        ____
    # Fill the dictionary with entities
    for ent in entities:
        params[ent["entity"]] = str(ent["value"])
    # Find matching hotels
    results = [
        r 
        for r in find_hotels(params, excluded) 
        if r[0] not in excluded
    ]
    # Extract the suggestions
    names = [r[0] for r in results]
    n = min(len(results), 3)
    suggestions = names[:2]
    return responses[n].format(*names), params, suggestions, excluded

# Initialize the empty dictionary and lists
params, suggestions, excluded = {}, [], []

# Send the messages
for message in ["I want a mid range hotel", "no that doesn't work for me"]:
    print("USER: {}".format(message))
    response, params, suggestions, excluded = respond(message, params, suggestions, excluded)
    print("BOT: {}".format(response))





#SOLUTION
# Define respond()
def respond(message, params, prev_suggestions, excluded):
    # Interpret the message
    parse_data = interpret(message)
    # Extract the intent
    intent = parse_data["intent"]["name"]
    # Extract the entities
    entities = parse_data["entities"]
    # Add the suggestion to the excluded list if intent is "deny"
    if intent == "deny":
        excluded.extend(prev_suggestions)
    # Fill the dictionary with entities
    for ent in entities:
        params[ent["entity"]] = str(ent["value"])
    # Find matching hotels
    results = [
        r 
        for r in find_hotels(params, excluded) 
        if r[0] not in excluded
    ]
    # Extract the suggestions
    names = [r[0] for r in results]
    n = min(len(results), 3)
    suggestions = names[:2]
    return responses[n].format(*names), params, suggestions, excluded

# Initialize the empty dictionary and lists
params, suggestions, excluded = {}, [], []

# Send the messages
for message in ["I want a mid range hotel", "no that doesn't work for me"]:
    print("USER: {}".format(message))
    response, params, suggestions, excluded = respond(message, params, suggestions, excluded)
    print("BOT: {}".format(response))
