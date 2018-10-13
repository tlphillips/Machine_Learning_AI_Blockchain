'''Similar to the sparse CountVectorizer created in the previous exercise, you'll work on creating tf-idf vectors for your documents. 
You'll set up a TfidfVectorizer and investigate some of its features.

In this exercise, you'll use pandas and sklearn along with the same X_train, y_train and X_test, y_test DataFrames and Series you created in the last exercise.'''
#TASK
# Import TfidfVectorizer from sklearn.feature_extraction.text.
# Create a TfidfVectorizer object called tfidf_vectorizer. When doing so, specify the keyword arguments stop_words="english" and max_df=0.7.
# Fit and transform the training data.


# Import TfidfVectorizer
____

# Initialize a TfidfVectorizer object: tfidf_vectorizer
tfidf_vectorizer = ____

# Transform the training data: tfidf_train 
tfidf_train = ____

# Transform the test data: tfidf_test 
tfidf_test = ____

# Print the first 10 features
print(____[:10])

# Print the first 5 vectors of the tfidf training data
print(____[:5])



#SOLUTION
# Import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize a TfidfVectorizer object: tfidf_vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

# Transform the training data: tfidf_train 
tfidf_train = tfidf_vectorizer.fit_transform(X_train)

# Transform the test data: tfidf_test 
tfidf_test = tfidf_vectorizer.transform(X_test)

# Print the first 10 features
print(tfidf_vectorizer.get_feature_names()[:10])

# Print the first 5 vectors of the tfidf training data
print(tfidf_train.A[:5])
