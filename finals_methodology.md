---
layout: page
title: Methods - Finals
permalink: /finals_methodology
nav_order: 9
---

# Core Temperature Estimation of Electric Vehicle Battery Packs

## Methodology Employed for Finals submission
<br/>

<br/>
### Supervised Learning

### Model 4: Random Forest Regression
* From our previous evaluation till mid-term submission, we found Polynomial Regression to be the best predictor with an R^2 score of ~89% and Mean Absolute Error of 1.8°C.
* Despite these results being up to par, Polynomial Regression's worst case performance took a hit with a Max Absolute Error of 17.41°C. Since the application, we are targeting is mission critical with human lives at stake, such worst case prediction was simply not unacceptable.
* Thus, we explored other models that are robust with a primary goal of minimizing Max Absolute Error.
* We started of with Random Forest Regression, which is an ensemble based model that employs random sampling of features and data points to construct multiple trees.
* We expected the bootstrapping process, where in, data points could be potentially selected multiple times and others may not be selected at all, to reduce the variance of the model and make it more robust to over-fitting.
* The data set was divided in the ratio of 80:20 (Train:Test) and only 80% of the dataset was used for training the regression model with cross validation in this method.
* For hyper parameter tuning, we employed Grid search cross-validation (Grid Search CV) with the following search space:
    * "n_estimators": [2, 5, 10, 20, 50, 75, 100]
    * "max_depth": [None, 2, 3, 4, 5]
    * "max_features": ["sqrt", "log2", None]
    * "min_samples_split": [12, 15, 17]
    * "min_samples_leaf": [4, 6, 8]
* Post fitting the search space, we got the following parameter as the best fit hyper-parameters:
    * Best hyper-parameters: {'max_depth': None, 'max_features': None, 'min_samples_leaf': 4, 'min_samples_split': 12, 'n_estimators': 75, 'random_state': 42}


### Model 5: XGBoost Regression
* We observed great results with the Random Forest Regression. To validate these results, we tried another ensemble model named XGBoost (extra gradient boosting). 
* We have managed to improve the Maximum absolute error in temperature prediction and bring it down from 17.41°C in Polynomial Regression to 5.22°C using Random Forest. Our primary objective to use XGBoost is to try and further bring down this Max Absolute error.
* XGBoost uses built-in regularization techniques to prevent overfitting which is not explicitly present in Random Forest. It being a boosting algorithm which would mean that it builds trees in a sequential manner with each tree correcting the errors of the previous ones.  
* The data set was divided in the ratio of 80:20 (Train:Test) and only 80% of the dataset was used for training the regression model with cross validation included in this method.
* For hyper parameter tuning, we employed Grid search cross-validation (Grid Search CV) with the following search space:
    * 'min_child_weight': [5, 10, 15],
    * 'gamma': [0.2, 0.6, 1.0],
    * 'subsample': [0.6, 0.8, 1.0],
    * 'colsample_bytree': [1.0, 1.6, 2.0],
    * 'max_depth': [2, 5, 8]
* Post fitting the search space, we got the following parameter as the best fit hyper-parameters:
    * Best hyper-parameters: {'min_child_weight': 5, 'gamma': 0.2, 'subsample': 1.0, 'colsample_bytree': 1.0, 'max_depth': 8, 'random_state': 42}
