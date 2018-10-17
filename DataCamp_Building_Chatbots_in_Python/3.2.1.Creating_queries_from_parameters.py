'''Now you're going to implement a more powerful function for querying the hotels database. 
The goal is to take arguments that can later be specified by other parts of your code.

Specifically, your job here is to define a find_hotels() function which takes a single argument - a dictionary of column names and values - and returns a list of matching hotels from the database.'''
#TASK
# Initialise a query string containing everything before the "WHERE" keyword.
# A filters list has been created for you. Join this list together with the strings " WHERE " and " and ".
# Create a tuple of the values of the params dictionary.
# Create a connection and cursor to "hotels.db" and then execute the query, just as in the previous exercise.

# Define find_hotels()
def find_hotels(params):
    # Create the base query
    query = 'SELECT * FROM hotels'
    # Add filter clauses for each of the parameters
    if len(params) > 0:
        filters = ["{}=?".format(k) for k in params]
        query += " ____ " + " ____ ".join(____)
    # Create the tuple of values
    t = tuple(____)
    
    # Open connection to DB
    conn = sqlite3.connect("____")
    # Create a cursor
    c = ____
    # Execute the query
    ____
    # Return the results
    ____



#SOLUTION
# Define find_hotels()
def find_hotels(params):
    # Create the base query
    query = 'SELECT * FROM hotels'
    # Add filter clauses for each of the parameters
    if len(params) > 0:
        filters = ["{}=?".format(k) for k in params]
        query += " ____ " + " ____ ".join(____)
    # Create the tuple of values
    t = tuple(____)
    
    # Open connection to DB
    conn = sqlite3.connect("____")
    # Create a cursor
    c = ____
    # Execute the query
    ____
    # Return the results
    ____
