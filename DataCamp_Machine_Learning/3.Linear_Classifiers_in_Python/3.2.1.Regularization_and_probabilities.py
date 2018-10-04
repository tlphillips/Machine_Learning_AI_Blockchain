'''In this exercise, you will observe the effects of changing the regularization stength on the predicted probabilities. 
A 2D binary classification dataset is already loaded into the environment as X and y.'''

#TASK
# Compute the maximum predicted probability.
# Run the provided code and take a look at the plot.
# Create a model with C=0.1 and examine how the plot and probabilities change.

# Set the regularization strength
model = LogisticRegression(C=1)

# Fit and plot
model.fit(X,y)
plot_classifier(X,y,model,proba=True)

# Predict probabilities on training points
prob = model.predict_proba(X)
print("Maximum predicted probability", ____)


#SOLUTION

# Set the regularization strength
model = LogisticRegression(C=0.1)

# Fit and plot
model.fit(X,y)
plot_classifier(X,y,model,proba=True)

# Predict probabilities on training points
prob = model.predict_proba(X)
print("Maximum predicted probability", np.max(prob))