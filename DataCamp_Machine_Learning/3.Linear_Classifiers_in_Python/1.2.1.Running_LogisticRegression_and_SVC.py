'''In this exercise, you'll apply logistic regression and a support vector machine to classify images of handwritten digits.'''

#TASK
# Apply logistic regression and SVM to the handwritten digits data set using the provided train/validation split.
# For each classifier, print out the training and validation accuracy.

from sklearn import datasets
digits = datasets.load_digits()
Xtrain, Xtest, ytrain, ytest = train_test_split(digits.data, digits.target)

# Apply logistic regression and print scores
lr = ____
lr.____
print(____)
print(____)

# Apply SVM and print scores
svm = ____
svm.____
print(____)
print(____)





#SOLUTION
from sklearn import datasets
digits = datasets.load_digits()
Xtrain, Xtest, ytrain, ytest = train_test_split(digits.data, digits.target)

# Apply logistic regression and print scores
lr = LogisticRegression()
lr.fit(Xtrain, ytrain)
print(lr.score(Xtrain, ytrain))
print(lr.score(Xtest, ytest))

# Apply SVM and print scores
svm = SVC()
svm.fit(Xtrain, ytrain)
print(svm.score(Xtrain, ytrain))
print(svm.score(Xtest, ytest))