'''You're about to take everything you've learned so far and implement it in a Pipeline that works with the real, DrivenData- https://www.drivendata.org/ budget line item data you've been exploring.

Surprise! The structure of the pipeline is exactly the same as earlier in this chapter:

the preprocessing step uses FeatureUnion to join the results of nested pipelines that each rely on FunctionTransformer to select multiple datatypes
the model step stores the model object
You can then call familiar methods like .fit() and .score() on the Pipeline object pl.'''

#TASK
# Complete the 'numeric_features' transform with the following steps:
    # get_numeric_data, with the name 'selector'.
    # Imputer(), with the name 'imputer'.
# Complete the 'text_features' transform with the following steps:
    # get_text_data, with the name 'selector'.
    # CountVectorizer(), with the name 'vectorizer'.
# Fit the pipeline to the training data.
# Hit 'Submit Answer' to compute the accuracy!



# Complete the pipeline: pl
pl = Pipeline([
        ('union', FeatureUnion(
            transformer_list = [
                ('numeric_features', Pipeline([
                    (____, ____),
                    (____, ____)
                ])),
                ('text_features', Pipeline([
                    (____, ____),
                    (____, ____)
                ]))
             ]
        )),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

# Fit to the training data
____

# Compute and print accuracy
accuracy = pl.score(X_test, y_test)
print("\nAccuracy on budget dataset: ", accuracy)]


#SOLUTION
# Complete the pipeline: pl
pl = Pipeline([
        ('union', FeatureUnion(
            transformer_list = [
                ('numeric_features', Pipeline([
                    ('selector', get_numeric_data),
                    ('imputer', Imputer())
                ])),
                ('text_features', Pipeline([
                    ('selector', get_text_data),
                    ('vectorizer', CountVectorizer())
                ]))
             ]
        )),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

# Fit to the training data
pl.fit(X_train, y_train)

# Compute and print accuracy
accuracy = pl.score(X_test, y_test)
print("\nAccuracy on budget dataset: ", accuracy)
