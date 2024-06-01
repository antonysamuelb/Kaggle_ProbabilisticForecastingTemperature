
# Probabilistic forecasting.

## Get libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import QuantileRegressor

## Parameters
quantiles = [i * 0.025 for i in range(1, 40)] # probabilities for which we should predict.

## Get data 
train_df = pd.read_csv('data/train.csv')
test_df = pd.read_csv('data/test.csv')
sample_df = pd.read_csv('data/sample.csv')

## Convert data to model consumable format.
# Extract features (X) and target variable (y) from the DataFrame
X_train = train_df.drop(columns=["Temperature", "id"])  
y_train = train_df['Temperature']

X_test = test_df.drop(columns=["id"])  

# Convert DataFrame to numpy arrays
X_train_array = X_train.values
y_train_array = y_train.values

X_test_array = X_test.values

## create a linear regression model.
predictions = {}
# out_bounds_predictions = np.zeros_like(y_true_mean, dtype=np.bool_)
for quantile in quantiles:
    qr = QuantileRegressor(quantile=quantile, alpha=0, solver=solver)
    y_pred = qr.fit(X_train, y_train).predict(X)
    predictions[quantile] = y_pred

    if quantile == min(quantiles):
        out_bounds_predictions = np.logical_or(
            out_bounds_predictions, y_pred >= y_pareto
        )
    elif quantile == max(quantiles):
        out_bounds_predictions = np.logical_or(
            out_bounds_predictions, y_pred <= y_pareto
        )