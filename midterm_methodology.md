---
layout: page
title: Methods - Mid Term
permalink: /midterm_methodology
nav_order: 7
---

# Core Temperature Estimation of Electric Vehicle Battery Packs

## Methodology Employed for Mid-term submission
<br/>

<br/>
### Supervised Learning

### Common Model Evaluation Framework
A common model evaluation framework was developed to fairly compare the performance of all regression models developed in this project. Models will be evaluated using K-Fold cross-validation, and two interpretable error metrics. More specifically:
* The final dataset of 1,040,342 complete observations of 12 features is randomly shuffled and then partitioned into K=5 equally-sized groups (“folds“) of observations.
* For k = 1, 2, …, K, all models are trained on all folds except fold k, and then tested on fold k. Model performance on each test fold is recorded.
* Model performance on the test fold is assessed by four metrics: mean absolute error, maximum absolute error, mean absolute percentage error, and R square metrics. These error metrics are easily interpretable in the context of temperature estimation. Maximum absolute error has the added advantage of upper-bounding all other errors, but this comes at the cost of sensitivity to outliers. Adjusted R-square metrics can provide a more precise view of the correlation by also taking into account how many independent variables are added to a particular model and thus is used as well.
* A model’s performance is finally judged by averaging each performance metric across folds.

### Model 1: Linear Regression
As a first step, a simple linear regression model was employed for the temperature estimation task. The 11 features in [Table 3](feature_selection#summary-of-data-preprocessing) (barring battery temperature) were used as predictors of battery temperature, along with a bias term, for a total of 12 predictors.

### Model 2 and 3: Second-Order Polynomial Regression with Data Re-Scaling
Model 1 was refined by allowing quadratic terms. The 11 features in [Table 3](feature_selection#summary-of-data-preprocessing) (barring battery temperature), their squares, and their pairwise products (without duplicates) were used as predictors of battery temperature, along with a bias term, for a total of 78 predictors. Prior to squaring, the 11 features in [Table 3](feature_selection#summary-of-data-preprocessing) were re-scaled to have zero mean and unit variance. This was done because the feature values have different relative scales, and squaring tends to worsen such disparities (small numbers < 1 get smaller, large numbers get larger). Data re-scaling rules were defined at training time, stored, and applied to testing data at prediction time. As the number of predictors is larger, an l1-regularized (“LASSO”) variant of Model 2 was also constructed to encourage sparsity in the weight vector (i.e., reduce the number of predictors effectively used). We are calling this our Model 3.


### Unsupervised Learning
We employed Principal Component Analysis (PCA) to reduce the dimensions from 11 features described above. We choose 3 to begin with.

* Explained variance ratio shows:
    * Component 1: 77.22%
    * Component 2: 22.50%
    * Component 3: 0.13%

* This means, beyond component 3, there is insignificant contribution for the variance. So we re-run the model to limit the pca output dimensions to 2, to keep the complexity and running time lesser.
* The coefficients of both the dimensions given by components is as follows:
* Component 1: [-1.93379730e-01 -2.94246703e-04 -1.06438283e-02  3.06773061e-04 1.35455257e-03 -1.44453362e-03 -4.14592565e-03 -3.58048366e-04 9.81047184e-01 -8.21131820e-05 -3.99814896e-03]
* Component 2: [ 9.81070156e-01 -8.40771667e-04 -5.67068931e-04 -2.26316456e-03 -1.62558054e-03 -4.30653659e-03  3.38168875e-03 -7.79714308e-03 1.93374257e-01 -1.05513388e-04 -2.85717854e-03]
