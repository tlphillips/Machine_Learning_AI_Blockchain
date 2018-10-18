'''You'll often need to briefly deviate from a flow, for example to authenticate a user, before returning.

In these cases, it's often simpler - and easier to debug - to save some actions/states as pending rather than adding ever more complicated rules.

Here, you're going to define a policy_rules dictionary, where the keys are tuples of the current state and the received intent, 
while the values are tuples of the next state, the bot's response, and a state for which to set a pending transition.'''

#TASK
# Complete the policy_rules dictionary by filling in the values. A user starts in the INIT state. They can only move to the AUTHED state by providing their phone number. If the user is in the INIT state and tries to place an order, you should ask for their number and create a pending transition to the AUTHED state. This is the only policy rule which creates a pending transition, so the others simply have a None value.
# The pending state has been added as the second argument of the send_message() function, which now returns the new state as well as the pending state. Call this send_message() function inside send_messages(), unpacking the output into the variables state and pending.

# Define the states
INIT=0
AUTHED=1
CHOOSE_COFFEE=2
ORDERED=3

# Define the policy rules
policy_rules = {
    (INIT, "order"): (____, "you'll have to log in first, what's your phone number?", ____),
    (INIT, "number"): (____, "perfect, welcome back!", None),
    (AUTHED, "order"): (____, "would you like Columbian or Kenyan?", None),    
    (CHOOSE_COFFEE, "specify_coffee"): (____, "perfect, the beans are on their way!", None)
}

# Define send_messages()
def send_messages(messages):
    state = INIT
    pending = None
    for msg in messages:
        state, pending = ____(____, ____, ____)

# Send the messages
send_messages([
    "I'd like to order some coffee",
    "555-12345",
    "kenyan"
])






#SOLUTION
# Define the states
INIT=0
AUTHED=1
CHOOSE_COFFEE=2
ORDERED=3

# Define the policy rules
policy_rules = {
    (INIT, "order"): (INIT, "you'll have to log in first, what's your phone number?", AUTHED),
    (INIT, "number"): (AUTHED, "perfect, welcome back!", None),
    (AUTHED, "order"): (CHOOSE_COFFEE, "would you like Columbian or Kenyan?", None),    
    (CHOOSE_COFFEE, "specify_coffee"): (ORDERED, "perfect, the beans are on their way!", None)
}

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
    "kenyan"
])
