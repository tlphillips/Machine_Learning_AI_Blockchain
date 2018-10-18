'''With your chitchat_response(message) function defined, 
the next step is to define a send_message() function which first calls chitchat_response(message), 
and only uses the coffee bot policy if there is no matching message.'''
#TASK
# Define a send_message() function which takes in 3 arguments - state, pending, and message.
# Call chitchat_response(message), storing the result in response. If there is a response, print it and return the state along with None.
# Unpack the policy_rules dictionary into the variables new_state, response, and pending_state. To do this, pass in a tuple consisting of state and interpret(message).
# If pending is not none, extract the new states and response by using pending as the key of policy_rules.

# Define send_message()
def ____:
    print("USER : {}".format(message))
    response = ____
    if response is not None:
        print("BOT : {}".format(response))
        return state, None
    
    # Calculate the new_state, response, and pending_state
    ____, ____, ____ = ____[(____, ____)]
    print("BOT : {}".format(response))
    if pending is not None:
        new_state, response, pending_state = ____
        print("BOT : {}".format(response))        
    if pending_state is not None:
        pending = (pending_state, interpret(message))
    return new_state, pending

# Define send_messages()
def send_messages(messages):
    state = INIT
    pending = None
    for msg in messages:
        state, pending = send_message(state, pending, msg)

# Send the messages
send_messages([
    "I'd like to order some coffee",
    "555-12345",
    "do you remember when I ordered 1000 kilos by accident?",
    "kenyan"
])  








#SOLUTION
# Define send_message()
def send_message(state, pending, message):
    print("USER : {}".format(message))
    response = chitchat_response(message)
    if response is not None:
        print("BOT : {}".format(response))
        return state, None
    
    # Calculate the new_state, response, and pending_state
    new_state, response, pending_state = policy_rules[(state, interpret(message))]
    print("BOT : {}".format(response))
    if pending is not None:
        new_state, response, pending_state = policy_rules[pending]
        print("BOT : {}".format(response))        
    if pending_state is not None:
        pending = (pending_state, interpret(message))
    return new_state, pending

# Define send_messages()
def send_messages(messages):
    state = INIT
    pending = None
    for msg in messages:
        state, pending = send_message(state, pending, msg)

# Send the messages
send_messages([
    "I'd like to order some coffee",
    "555-12345",
    "do you remember when I ordered 1000 kilos by accident?",
    "kenyan"
])  