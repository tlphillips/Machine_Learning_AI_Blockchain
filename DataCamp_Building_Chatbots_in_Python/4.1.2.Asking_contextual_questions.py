'''Sometimes your users need some help! They will have questions and expect the bot to help them.

In this exercise, you'll allow users to ask the coffee bot to explain the steps to them.
 Like before, the answer they get will depend on where they are in the flow.'''
#TASK
# Add two rules to your policy to handle the intent "ask_explanation" when in either of the states INIT or CHOOSE_COFFEE.
# Inside the send_messages() function, call the send_message() function with wih state and msg as arguments. Then, hit 'Submit Answer' to send the messages and see the bot's responses.

# Define the states
INIT=0 
CHOOSE_COFFEE=1
ORDERED=2

# Define the policy rules dictionary
policy_rules = {
    (____, "____"): (INIT, "I'm a bot to help you order coffee beans"),
    (____, "order"): (CHOOSE_COFFEE, "ok, Columbian or Kenyan?"),
    (____, "specify_coffee"): (ORDERED, "perfect, the beans are on their way!"),
    (____, "____"): (CHOOSE_COFFEE, "We have two kinds of coffee beans - the Kenyan ones make a slightly sweeter coffee, and cost $6. The Brazilian beans make a nutty coffee and cost $5.")    
}

# Define send_messages()
def send_messages(messages):
    state = INIT
    for msg in messages:
        state = send_message(state, msg)

# Send the messages
send_messages([
    "what can you do for me?",
    "well then I'd like to order some coffee",
    "what do you mean by that?",
    "kenyan"
])





#SOLUTION
# Define the states
INIT=0 
CHOOSE_COFFEE=1
ORDERED=2

# Define the policy rules dictionary
policy_rules = {
    (INIT, "ask_explanation"): (INIT, "I'm a bot to help you order coffee beans"),
    (INIT, "order"): (CHOOSE_COFFEE, "ok, Columbian or Kenyan?"),
    (CHOOSE_COFFEE, "specify_coffee"): (ORDERED, "perfect, the beans are on their way!"),
    (CHOOSE_COFFEE, "ask_explanation"): (CHOOSE_COFFEE, "We have two kinds of coffee beans - the Kenyan ones make a slightly sweeter coffee, and cost $6. The Brazilian beans make a nutty coffee and cost $5.")    
}

# Define send_messages()
def send_messages(messages):
    state = INIT
    for msg in messages:
        state = send_message(state, msg)

# Send the messages
send_messages([
    "what can you do for me?",
    "well then I'd like to order some coffee",
    "what do you mean by that?",
    "kenyan"
])
