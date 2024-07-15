# Kaggle_ProbabilisticForecastingTemperature
Kaggle probabilistic-forecasting-i-temperature attempts repo.

Competition link: https://www.kaggle.com/competitions/probabilistic-forecasting-i-temperature/data

#### Done
1. Vanilla Linear regression with all available features.
2. FFT based time series.
3. Catboost model with temporal features.
4. Cat boost with FFT.
5. Cat boost with FFT. CV on FFT.
6. Cat boost with FFT. CV on Catboost and FFT.
7. Cylcic encoding of temporal features. But it doesnt give the improvement that I hoped for. It is unable to account for the trend.
8. Tried MSTL with TS. But it doesnt help as expected. It helps capture the recent trend a bit, but the seasonality is not captured properly.
9. Checked out VM's notebook and we have month seasonality too! Add that and try. Doesn't help that much. Perhaps passing TS as input to CB is not helping much. 
10. Instead of passing TS, pass the seasonality and trend directly and their projections directly. 2nd best score so far. (1.7001)
11. Remove date_int. This might not be relevant as trend, seasonality is being passed. Best so far (1.6730). We are still not capturing the month right.
12. Pass the day of the month as an input to the feature. (1.6274) New best!!!
13. Use MSTL to get monthly seasonality from the residual of the current multi seasonal decomposition function. - 5.9250, this obviously doesnt work!
14. Feature removal on top of v12. All features open for removal except for 'day of the year'. New best (1.5921)
15. Create output based on latest data. We should have two sets of outputs so that the public leaderboard is not given the fitted data.
16. TODO: Conformal predictions.
17. TODO: Correct data issues identified.

#### Didn't work
1. Use MSTL to get monthly seasonality 

#### Misc
1. Understand CRPS better
