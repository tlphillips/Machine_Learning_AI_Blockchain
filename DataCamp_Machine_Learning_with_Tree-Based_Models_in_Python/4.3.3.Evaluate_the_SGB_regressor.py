'''You have prepared the ground to determine the test set RMSE of sgbr which you shall evaluate in this exercise.

y_pred and y_test are available in your workspace.'''
#TASK
# Import mean_squared_error as MSE from sklearn.metrics.
# Compute test set MSE and assign the result to mse_test.
# Compute test set RMSE and assign the result to rmse_test.

# Import mean_squared_error as MSE
____

# Compute test set MSE
mse_test = ____

# Compute test set RMSE
rmse_test = ____

# Print rmse_test
print('Test set RMSE of sgbr: {:.3f}'.format(rmse_test))




#SOLUTION

# Import mean_squared_error as MSE
from sklearn.metrics import mean_squared_error as MSE

# Compute test set MSE
mse_test = MSE(y_test, y_pred)

# Compute test set RMSE
rmse_test = mse_test**0.5

# Print rmse_test
print('Test set RMSE of sgbr: {:.3f}'.format(rmse_test))
