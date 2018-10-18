'''Having defined your policy function, it's now time to write a send_message() function which takes both a pending action and a message as its arguments and leverages the policy function to determine the bot's response.

Your policy(intent) function from the previous exercise has been pre-loaded.'''
#TASK
# Define a function called send_message() which takes in two arguments - pending and message.
# Pass in interpret(message) as an argument to policy() and unpack the result into the variables action and pending_action.
# If the action is "do_pending" and pending is not None, print the pending response. Else, print the action.
# Inside the definition of the send_messages() function, call your send_message() function with pending and msg as arguments. Then, hit 'Submit Answer' to send the messages and see the results.


# Define send_message()
def ____(____, ____):
    print("USER : {}".format(message))
    ____, ____ = ____
    if ____ == "____" and pending is not None:
        print("BOT : {}".format(____))
    else:
        print("BOT : {}".format(____))
    return pending_action
    
# Define send_messages()
def send_messages(messages):
    pending = None
    for msg in messages:
        pending = ____

# Send the messages
send_messages([
    "I'd like to order some coffee",
    "ok yes please"
])




#SOLUTION
# Define send_message()
def send_message(pending, message):
    print("USER : {}".format(message))
    action, pending_action = policy(interpret(message))
    if action == 'do_pending' and pending is not None:
        print("BOT : {}".format(pending))
    else:
        print("BOT : {}".format(action))
    return pending_action
    
# Define send_messages()
def send_messages(messages):
    pending = None
    for msg in messages:
        pending = send_message(pending, msg)

# Send the messages
send_messages([
    "I'd like to order some coffee",
    "ok yes please"
])