'''It's time to put everything together everything you've learned in the course by combining the coffee ordering bot with the eliza rules from chapter 1.

To begin, you'll define a function called chitchat_response(), which calls the predefined function match_rule() from back in chapter 1. 
This returns a response if the message matched an eliza template, and otherwise, None.

The eliza rules are contained in a dictionary called eliza_rules.'''
#TASK
# Define a chitchat_response() function which takes in a message argument.
# Call the match_rule() function with eliza_rules and message as arguments. Unpack the output into response and phrase.
# If the response is "default", return None.
# If "{0}" is in the response, replace the pronouns of the phrase using replace_pronouns(), and then include the phrase in the response by using .format() on response.

# Define chitchat_response()
def chitchat_response(message):
    # Call match_rule()
    ____, ____ = ____
    # Return none is response is "default"
    if response == "____":
        return None
    if '{0}' in response:
        # Replace the pronouns of phrase
        phrase = ____
        # Calculate the response
        response = ____
    return response







#SOLUTION
# Define chitchat_response()
def chitchat_response(message):
    # Call match_rule()
    response, phrase = match_rule(eliza_rules, message) 
    # Return none is response is "default"
    if response == "default":
        return None
    if '{0}' in response:
        # Replace the pronouns of phrase
        phrase = replace_pronouns(phrase)
        # Calculate the response
        response =response.format(phrase)
    return response
