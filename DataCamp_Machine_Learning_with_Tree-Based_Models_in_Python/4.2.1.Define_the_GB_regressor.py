'''You'll now revisit the Bike Sharing Demand dataset-https://www.kaggle.com/c/bike-sharing-demand that was introduced in the previous chapter. 
Recall that your task is to predict the bike rental demand using historical weather data from the Capital Bikeshare program in Washington, D.C.. 
For this purpose, you'll be using a gradient boosting regressor.

As a first step, you'll start by instantiating a gradient boosting regressor which you will train in the next exercise.'''
#TASK
# Import GradientBoostingRegressor from sklearn.ensemble.
# Instantiate a gradient boosting regressor by setting the parameters:  
    # max_depth to 4
    # n_estimators to 200

# Import GradientBoostingRegressor
____

# Instantiate gb
gb = ____(____=____, 
            ____=____,
            random_state=2)


#SOLUTION
# Import GradientBoostingRegressor
from sklearn.ensemble import GradientBoostingRegressor

# Instantiate gb
gb = GradientBoostingRegressor(max_depth=4, 
            n_estimators=200,
            random_state=2)