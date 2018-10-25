'''In this exercise you'll compare the test set accuracy of dt_entropy to the accuracy of another tree named dt_gini. 
The tree dt_gini was trained on the same dataset using the same parameters except for the information criterion which was set to the gini index using the keyword 'gini'.

X_test, y_test, dt_entropy, as well as accuracy_gini which corresponds to the test set accuracy achieved by dt_gini are available in your workspace.'''
#TASK
# Import accuracy_score from sklearn.metrics.
# Predict the test set labels of dt_entropy and assign the result to y_pred.
# Evaluate the test set accuracy of dt_entropy and assign the result to accuracy_entropy.
# Review accuracy_entropy and accuracy_gini.

# Import accuracy_score from sklearn.metrics
from ____.____ import ____

# Use dt_entropy to predict test set labels
____= ____.____(____)

# Evaluate accuracy_entropy
accuracy_entropy = ____(____, ____)

# Print accuracy_entropy
print('Accuracy achieved by using entropy: ', accuracy_entropy)

# Print accuracy_gini
print('Accuracy achieved by using the gini index: ', accuracy_gini)





#SOLUTION
# Import accuracy_score from sklearn.metrics
from sklearn.metrics import accuracy_score

# Use dt_entropy to predict test set labels
y_pred = dt_entropy.predict(X_test)

# Evaluate accuracy_entropy
accuracy_entropy = accuracy_score(y_pred, y_test)

# Print accuracy_entropy
print('Accuracy achieved by using entropy: ', accuracy_entropy)

# Print accuracy_gini
print('Accuracy achieved by using the gini index: ', accuracy_gini)