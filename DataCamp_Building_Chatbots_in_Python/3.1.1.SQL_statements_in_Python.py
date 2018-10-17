'''It's time to begin writing SQL queries! In this exercise, your job is to run a query against the hotels database to find all the expensive hotels in the south.
 The connection to the database has been created for you, along with a cursor c.

As Alan described in the video, you should be careful about SQL injection. Here, you'll pass parameters the safe way: As an extra tuple argument to the .execute() method. 
This ensures malicious code can't be injected into your query.'''
#TASK
# Define a tuple t of strings "south" and "hi" for the area and price.
# Execute the query using the cursor's .execute() method. You're looking for all hotels where the area is "south" and the price is "hi".
# Print the results using the cursor's .fetchall() method.

# Import sqlite3
import sqlite3

# Open connection to DB
conn = sqlite3.connect('hotels.db')

# Create a cursor
c = conn.cursor()

# Define area and price
area, price = "____", "____"
t = (____, ____)

# Execute the query
c.____('SELECT ____ FROM ____ WHERE ____=____ AND ____=____', ____)

# Print the results
print(____)


#SOLUTION
# Import sqlite3
import sqlite3

# Open connection to DB
conn = sqlite3.connect('hotels.db')

# Create a cursor
c = conn.cursor()

# Define area and price
area, price = "south", "hi"
t = (area, price)

# Execute the query
c.execute('SELECT * FROM hotels WHERE area=? AND price=?', t)

# Print the results
print(c.fetchall())

