'''You'll often want your bot to guide users through a series of steps, such as when they're placing an order.

In this exercise, you'll begin building a bot that lets users order coffee. 
They can choose between two types: Colombian, and Kenyan. If the user provides unexpected input, your bot will handle this differently depending on where they are in the flow.

Your job here is to identify the appropriate state and next state based on the intents and response messages provided. For example, if the intent is "order", then the state changes from INIT to CHOOSE_COFFEE.

A function send_message(policy, state, message) has already been defined for you. 
It takes the policy, the current state and message as arguments, and returns the new state as a result.
 Additionally, an interpret(message) function, similar to the one Alan described in the video, has been pre-defined for you.'''
#TASK
# Define three states: INIT with value 0, CHOOSE_COFFEE with value 1, and ORDERED with value 2.
# Create a dictionary called policy with tuples as keys and values. Each key is a tuple containing a state and an intent, and each value is a tuple containing the next state and the response message. The messages have been filled in for you. Your job is to fill in the states.
# Instantiate a variable state with the value INIT.
# For each of the messages, call the send_message() function, passing in the policy, state, and message.

# Define the INIT state
____

# Define the CHOOSE_COFFEE state
____

# Define the ORDERED state
____

# Define the policy rules
policy = {
    (____, "order"): (____, "ok, Colombian or Kenyan?"),
    (INIT, "none"): (INIT, "I'm sorry - I'm not sure how to help you"),
    (____, "specify_coffee"): (____, "perfect, the beans are on their way!"),
    (____, "none"): (____, "I'm sorry - would you like Colombian or Kenyan?"),
}

# Create the list of messages
messages = [
    "I'd like to become a professional dancer",
    "well then I'd like to order some coffee",
    "my favourite animal is a zebra",
    "kenyan"
]

# Call send_message() for each message
state = ____
for message in messages:    
    state = ____




#SOLUTION
# Define the INIT state
INIT = 0

# Define the CHOOSE_COFFEE state
CHOOSE_COFFEE = 1

# Define the ORDERED state
ORDERED = 2

# Define the policy rules
policy = {
    (INIT, "order"): (CHOOSE_COFFEE, "ok, Columbian or Kenyan?"),
    (INIT, "none"): (INIT, "I'm sorry - I'm not sure how to help you"),
    (CHOOSE_COFFEE, "specify_coffee"): (ORDERED, "perfect, the beans are on their way!"),
    (CHOOSE_COFFEE, "none"): (CHOOSE_COFFEE, "I'm sorry - would you like Colombian or Kenyan?"),
}

# Create the list of messages
messages = [
    "I'd like to become a professional dancer",
    "well then I'd like to order some coffee",
    "my favourite animal is a zebra",
    "kenyan"
]

# Call send_message() for each message
state = INIT
for message in messages:    
    state = send_message(policy, state, message)