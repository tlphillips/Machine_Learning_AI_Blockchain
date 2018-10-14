''''It can get a little boring hearing the same old answers over and over. 
In this exercise, you'll add some variation. If you ask your bot how it's feeling, it may equally well respond with "oh I'm great!" as with "I'm very sad today".

Here, you'll use the random module - specifically random.choice(ls) - which randomly selects an element from a list ls.

A dictionary called responses, which maps each message to a list of possible responses, has been defined for you.'''
#TASK
# Import the random module.
# Use random.choice() in the respond() function to choose one of the matching responses.

# Import the random module
____

name = "Greg"
weather = "cloudy"

# Define a dictionary containing a list of responses for each message
responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "default": ["default message"]
}

# Use random.choice() to choose a matching response
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return a random matching response
        bot_message = ____(____[____])
    else:
        # Return a random "default" response
        bot_message = ____.____(____["____"])
    return bot_message


#SOLUTION
# Import the random module
import random

name = "Greg"
weather = "cloudy"

# Define a dictionary containing a list of responses for each message
responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "default": ["default message"]
}

# Use random.choice() to choose a matching response
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return a random matching response
        bot_message = random.choice(responses[message])
    else:
        # Return a random "default" response
        bot_message = random.choice(responses["default"])
    return bot_message