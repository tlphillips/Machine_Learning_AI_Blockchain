'''Here, you're going to put your find_hotels() function into action! 
Recall that it accepts a single argument, params, which is a dictionary of column names and values.'''
#TASK
# Create the params dictionary with the column names (keys) "area" and "price", with corresponding values "south" and "lo".
# Use the find_hotels() function along with your params dictionary to find all inexpensive hotels in the South.

# Create the dictionary of column names and values
params = ____

# Find the hotels that match the parameters
print(____)

#SOLUTION
# Create the dictionary of column names and values
params = {"area": "south", "price": "lo"}

# Find the hotels that match the parameters
print(find_hotels(params))


