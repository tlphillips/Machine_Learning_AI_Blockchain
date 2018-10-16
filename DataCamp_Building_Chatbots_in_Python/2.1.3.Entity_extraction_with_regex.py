'''Now you'll use another simple method, this time for finding a person's name in a sentence such as "hello, my name is David Copperfield".

You'll look for the keywords "name" or "call(ed)", and find capitalized words using regex and assume those are names.
 Your job in this exercise is to define a find_name() function to do this.'''
#TASK
# Use re.compile() to create a pattern for checking if "name" or "call" keywords occur.
# Create a pattern for finding capitalized words.
# Use the .findall() method on name_pattern to retrieve all matching words in message.
# Call your find_name() function inside respond() and then hit 'Submit Answer' to see how the bot responds to the provided messages.

# Define find_name()
def find_name(message):
    name = None
    # Create a pattern for checking if the keywords occur
    name_keyword = ____
    # Create a pattern for finding capitalized words
    name_pattern = ____
    if name_keyword.search(message):
        # Get the matching words in the string
        name_words = ____
        if len(name_words) > 0:
            # Return the name if the keywords are present
            name = ' '.join(name_words)
    return name

# Define respond()
def respond(message):
    # Find the name
    name = ____
    if name is None:
        return "Hi there!"
    else:
        return "Hello, {0}!".format(name)

# Send messages
send_message("my name is David Copperfield")
send_message("call me Ishmael")
send_message("People call me Cassandra")



#SOLUTION
# Define find_name()
def find_name(message):
    name = None
    # Create a pattern for checking if the keywords occur
    name_keyword = re.compile('name|call')
    # Create a pattern for finding capitalized words
    name_pattern = re.compile('[A-Z]{1}[a-z]*')
    if name_keyword.search(message):
        # Get the matching words in the string
        name_words = name_pattern.findall(message)
        if len(name_words) > 0:
            # Return the name if the keywords are present
            name = ' '.join(name_words)
    return name

# Define respond()
def respond(message):
    # Find the name
    name = find_name(message)
    if name is None:
        return "Hi there!"
    else:
        return "Hello, {0}!".format(name)

# Send messages
send_message("my name is David Copperfield")
send_message("call me Ishmael")
send_message("People call me Cassandra")