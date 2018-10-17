'''An array X containing vectors describing each of the sentences in the ATIS dataset has been created for you, along with a 1D array y containing the labels. 
The labels are integers corresponding to the intents in the dataset. For example, label 0 corresponds to the intent atis_flight.

Now, you'll use the scikit-learn library to train a classifier on this same dataset. Specifically, you will fit and evaluate a support vector classifier.'''
#TASK
# Import the SVC class from sklearn.svm.
# Instantiate a classifier clf by calling SVC with a single keyword argument C with value 1.
# Fit the classifier to the training data X_train and y_train.
# Predict the labels of the test set, X_test.

# Import SVC
____

# Create a support vector classifier
clf = ____

# Fit the classifier using the training data
____

# Predict the labels of the test set
y_pred = ____

# Count the number of correct predictions
n_correct = 0
for i in range(len(y_test)):
    if y_pred[i] == y_test[i]:
        n_correct += 1

print("Predicted {0} correctly out of {1} test examples".format(n_correct, len(y_test)))



#SOLUTION
# Import SVC
from sklearn.svm import SVC

# Create a support vector classifier
clf = SVC(C=1)

# Fit the classifier using the training data
clf.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = clf.predict(X_test)

# Count the number of correct predictions
n_correct = 0
for i in range(len(y_test)):
    if y_pred[i] == y_test[i]:
        n_correct += 1

print("Predicted {0} correctly out of {1} test examples".format(n_correct, len(y_test)))
