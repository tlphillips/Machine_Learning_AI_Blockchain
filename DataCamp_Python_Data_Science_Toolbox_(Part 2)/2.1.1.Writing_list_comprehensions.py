''''You now have all the knowledge necessary to begin writing list comprehensions! 
Your job in this exercise is to write a list comprehension that produces a list of the squares of the numbers ranging from 0 to 9.'''
#TASK
# Using the range of numbers from 0 to 9 as your iterable and i as your iterator variable, write a list comprehension that produces a list of numbers consisting of the squared values of i.

# Create list comprehension: squares
squares = [____ for ____ in ____]






#SOLUTION
# Create list comprehension: squares
squares = [i*i for i in range(0,10)]
print(squares)
