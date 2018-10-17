'''Now you'll write a respond() function which can handle messages like "I want an expensive hotel in the south of town" and respond appropriately according to the number of matching results in a database. 
This is important functionality for any database-backed chatbot.

Your find_hotels() function from the previous exercises has already been defined for you, along with a rasa NLU interpreter object which can handle hotel queries and a list of responses, which you can explore in the Shell.'''
#TASK
# Use the .parse() method of interpreter to extract the "entities" in the message.
# Find matching hotels using the params dictionary and find_hotels() function.
# Use the min() function to choose the right index for the response to send. Here, n is the number of results.
# Select the appropriate response from the responses list and insert the names of hotels using the .format() method.

# Define respond()
def respond(message):
    # Extract the entities
    entities = ____.____(____)["____"]
    # Initialize an empty params dictionary
    params = {}
    # Fill the dictionary with entities
    for ent in entities:
        params[ent["entity"]] = str(ent["value"])

    # Find hotels that match the dictionary
    results = ____
    # Get the names of the hotels and index of the response
    names = [r[0] for r in results]
    n = ____(len(results),3)
    # Select the nth element of the responses array
    return ____[n].____(*names)




#SOLUTION
# Define respond()
def respond(message):
    # Extract the entities
    entities = interpreter.parse(message)["entities"]
    # Initialize an empty params dictionary
    params = {}
    # Fill the dictionary with entities
    for ent in entities:
        params[ent["entity"]] = str(ent["value"])

    # Find hotels that match the dictionary
    results = find_hotels(params)
    # Get the names of the hotels and index of the response
    names = [r[0] for r in results]
    n = min(len(results),3)
    # Select the nth element of the responses array
    return responses[n].format(*names)

print(respond("I want an expensive hotel in the south of town"))