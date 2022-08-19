Using Machine Learning to predict solar output generated by solar tracker (Powered by Dark Sky)

Training the model based on GradientBoosting Regression explained in: 
https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html

**Summary**

The project is split into three parts (PREPARE, TRAIN, PREDICT)

_preparer.py_: Collects weather data from Dark Sky's API. Selects only specific columns and formats to fit the csv. Collects solar output data from past year's project results. Combines the two.

_trainer.py_: Fits the data into Regression model. 

_predictor.py_: Gets current weather forecast and predicts solar output


**Other**

_weather.py_: Python module for reusable methods and variables

_CompareTrainers.py_: Compare the accuracy scores and plot the predicted values for different model

_angle_calculator.py_: Calculates the azimuth and zenith angle of the Sun