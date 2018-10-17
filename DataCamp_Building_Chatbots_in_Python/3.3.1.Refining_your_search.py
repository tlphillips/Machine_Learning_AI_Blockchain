'''Now you'll write a bot that allows users to add filters incrementally, in case they don't specify all of their preferences in one message.

To do this, initialize an empty dictionary params outside of your respond() function (unlike inside the function, like in the previous exercise). 
Your respond() function will take in this dictionary as an argument.'''
#TASK
# Define a respond() function that accepts two arguments - a message and a dictionary of params - and returns two results - the message to send to the user, and the updated param list.
# Extract "entities" from the message using the .parse() method of the interpreter, exactly like you did in the previous exercise.
# Find the hotels that match params using your find_hotels() function.
# Initialize the params dictionary outside the respond() function and hit 'Submit Answer' to pass the messages to the bot.

# Define a respond function, taking the message and existing params as input
def ____(____, ____):
    # Extract the entities
    entities = ____
    # Fill the dictionary with entities
    for ent in entities:
        params[ent["entity"]] = str(ent["value"])

    # Find the hotels
    results = ____
    names = [r[0] for r in results]
    n = min(len(results), 3)
    # Return the appropriate response
    return responses[n].format(*names), params

# Initialize params dictionary
params = ____

# Pass the messages to the bot
for message in ["I want an expensive hotel", "in the north of town"]:
    print("USER: {}".format(message))
    response, params = respond(message, params)
    print("BOT: {}".format(response))






#SOLUTION
# Define a respond function, taking the message and existing params as input
def respond(message, params):
    # Extract the entities
    entities = interpreter.parse(message)["entities"]
    # Fill the dictionary with entities
    for ent in entities:
        params[ent["entity"]] = str(ent["value"])

    # Find the hotels
    results = find_hotels(params)
    names = [r[0] for r in results]
    n = min(len(results), 3)
    # Return the appropriate response
    return responses[n].format(*names), params

# Initialize params dictionary
params = {}


# Pass the messages to the bot
for message in ["I want an expensive hotel", "in the north of town"]:
    print("USER: {}".format(message))
    response, params = respond(message, params)
    print("BOT: {}".format(response))