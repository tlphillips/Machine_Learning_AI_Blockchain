'''You can really improve the user experience of your bot by asking them simple yes or no questions. 
One easy way to handle these follow-ups is to define pending actions which get executed as soon as the user says "yes", and wiped if the user says "no".

In this exercise, you're going to define a policy function which takes the intent as it's sole argument, and returns two values: The next action to take, and a pending action. 
The policy function should return this value when a "yes" intent is returned, and should wipe the pending actions if a "no" intent is returned.

Here, the interpret(message) function has been defined for you such that if "yes" is in the message, "affirm" is returned, and if "no" is in the message, then "deny" is returned.'''
#TASK
# Define a function called policy which takes intent as its argument.
# If the intent is "affirm", return a "do_pending" action and None.
# If the intent is "deny", return a "Ok" action and None

# Define policy()
def ____(____):
    # Return "do_pending" if the intent is "affirm"
    if ____ == "____":
        return "____", None
    # Return "Ok" if the intent is "deny"
    if ____ == "____":
        return "____", None
    if intent == "order":
        return "Unfortunately, the Kenyan coffee is currently out of stock, would you like to order the Brazilian beans?", "Alright, I've ordered that for you!"





#SOLUTION
# Define policy()
def policy(intent):
    # Return "do_pending" if the intent is "affirm"
    if intent == "affirm":
        return "do_pending", None
    # Return "Ok" if the intent is "deny"
    if intent == "deny":
        return "Ok", None
    if intent == "order":
        return "Unfortunately, the Kenyan coffee is currently out of stock, would you like to order the Brazilian beans?", "Alright, I've ordered that for you!"
