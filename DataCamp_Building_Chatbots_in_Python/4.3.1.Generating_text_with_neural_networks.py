'''In this final exercise of the course, you're going to generate text using a neural network trained on the scripts of every episode of The Simpsons. 
Specifically, you'll use a simplified version of the sample_text() function that Alan described in the video.

It takes in two arguments, seed, and temperature. 
The seed argument is the initial sequence that the network uses to generate the subsequent text, while the temperature argument controls how risky the network is when generating text. 
At very low temperatures, it just repeats the most common combinations of letters, and at very high temperatures it generates complete gibberish. 
In order to ensure fast runtimes, the network in this exercise will only work for the subset of temperature values.

After you finish this exercise, be sure to check out this tutorial- https://www.datacamp.com/community/tutorials/facebook-chatbot-python-deploy by Alan in which he walks you through how to connect a chatbot to Facebook Messenger!'''
#TASK
# Set the seed to be "i'm gonna punch lenny in the back of the".
# For each of the riskiness values [0.2, 0.5, 1.0, 1.2], call the sample_text() function with the arguments seed and temperature.

# Feed the 'seed' text into the neural network
seed = "i'm gonna punch lenny in the back of the"

# Iterate over the different temperature values
for temperature in [0.2, 0.5, 1.0, 1.2]:
    print("\nGenerating text with riskiness : {}\n".format(temperature))
    # Call the sample_text function
    print(____)








#SOLUTION
# Feed the 'seed' text into the neural network
seed = "i'm gonna punch lenny in the back of the"

# Iterate over the different temperature values
for temperature in [0.2, 0.5, 1.0, 1.2]:
    print("\nGenerating text with riskiness : {}\n".format(temperature))
    # Call the sample_text function
    print(sample_text(seed, temperature))

