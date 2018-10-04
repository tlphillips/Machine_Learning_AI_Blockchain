'''In this exercise, you will observe the effects of changing the coefficients of a linear classifer. 
A 2D dataset is already loaded into the environment as X and y, along with a linear classifier object model.'''

#TASK
# Explore the effects of changing the two coefficients and the intercept.
# Set the coefficients and intercept so that the model makes no errors.


# Set the coefficients
model.coef_ = np.array([[0,1]])
model.intercept_ = np.array([0])

# Plot the data and decision boundary
plot_classifier(X,y,model)

# Print the number of errors
num_err = np.sum(y != model.predict(X))
print("Number of errors:", num_err)


#SOLUTION
# Set the coefficients
model.coef_ = np.array([[-1,1]])
model.intercept_ = np.array([-3])

# Plot the data and decision boundary
plot_classifier(X,y,model)

# Print the number of errors
num_err = np.sum(y != model.predict(X))
print("Number of errors:", num_err)