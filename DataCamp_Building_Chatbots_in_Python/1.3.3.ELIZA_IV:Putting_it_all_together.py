'''Now you're going to put it all together and experience the magic! 
The match_rule(), send_message(), and replace_pronouns() functions have already been defined, and the rules dictionary is available in your workspace.

Your job here is to write a function called respond() with a single argument message which creates an appropriate response to be handled by send_message.'''
#TASK
# Get a response and phrase by calling match_rule() with the rules dictionary and message.
# Check if the response is a template by seeing if it includes the string '{0}'. If it does, use the replace_pronouns() function on phrase.
# Include the phrase by using .format() on response and overriding the value of response.
# Hit 'Submit Answer' to how the bot responds to the provided messages!

# Define respond()
def respond(message):
    # Call match_rule
    ____, ____ = ____
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = ____
        # Include the phrase in the response
        response = ____
    return response

# Send the messages
send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")




#SOLUTION
# Define respond()
def respond(message):
    # Call match_rule
    response, phrase = match_rule(rules, message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response

# Send the messages
send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")

