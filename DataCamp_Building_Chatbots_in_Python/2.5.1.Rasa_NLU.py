'''In this exercise you'll use Rasa NLU to create an interpreter, which parses incoming user messages and returns a set of entities.
 Your job is to train an interpreter using the MITIE entity recognition model in rasa NLU.'''
#TASK
# Create a dictionary called args with a single key "pipeline" with value "spacy_sklearn".
# Create a config by calling RasaNLUConfig() with the single argument cmdline_args with value args.
# Create a trainer by calling Trainer() using the configuration as the argument.
# Create a interpreter by calling trainer.train() with the training_data.

# Import necessary modules
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

# Create args dictionary
args = ____

# Create a configuration and trainer
config = ____
trainer = ____

# Load the training data
training_data = load_data("./training_data.json")

# Create an interpreter by training the model
interpreter = ____

# Try it out
print(interpreter.parse("I'm looking for a Mexican restaurant in the North of town"))





#SOLUTION
# Import necessary modules
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

# Create args dictionary
args = {"pipeline": "spacy_sklearn"}

# Create a configuration and trainer
config = RasaNLUConfig(cmdline_args=args)
trainer = Trainer(config)

# Load the training data
training_data = load_data("./training_data.json")

# Create an interpreter by training the model
interpreter = trainer.train(training_data)

# Try it out
print(interpreter.parse("I'm looking for a Mexican restaurant in the North of town"))
