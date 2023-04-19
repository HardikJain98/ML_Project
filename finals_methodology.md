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
