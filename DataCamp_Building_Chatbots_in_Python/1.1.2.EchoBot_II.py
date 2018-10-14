'''Having written your respond() function, you'll now define a function called send_message() with a single parameter message which logs the message and the bot's response.'''

#TASK
# Use the user_template string's .format() method to include the user's message into the user template, and print the result.
# Call the respond() function with the message passed in and save the result as response.
# Log the bot's response using the bot_template string's .format() method.
# Send the message "hello" to the bot.


# Define a function that sends a message to the bot: send_message
def ____(____):
    # Print user_template including the user_message
    print(____.format(____))
    # Get the bot's response to the message
    response = ____(____)
    # Print the bot template including the bot's response.
    print(____.format(____))

# Send a message to the bot
send_message("____")


#SOLUTIION
# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Send a message to the bot
send_message("hello")


