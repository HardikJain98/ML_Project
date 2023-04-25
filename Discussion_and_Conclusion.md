---
layout: page
title: Discussion and Conclusion
permalink: /Discussion_and_Conclusion
nav_order: 11
---

# Core Temperature Estimation of Electric Vehicle Battery Packs

## Models Comparison and Discussion
<br/>

The table presents a comparison of the performance of different regression models (Linear, Polynomial and, Polynomial with L1 penalty), Random Forest, XGBoost, and a Neural Network.


|                     | Linear Regression | Polynomial Regression | Poly. Reg + L1 Penalty | Random Forest | XGBoost | Neural Network |   
| Mean Absolute Error | 2.342             | 1.879                 | 2.936                  | 0.02          | 0.107   | 1.39           |
| Max Abs error [°C]  | 13.19             | 17.41                 | 11.45                  | 5.224         | 4.369   | 13.46          |
| R^2 Score           | 84.47%            | 89.92%                | 74.73%                 | 99.997%       | 99.94%  | 92.89%         | 
| Adjusted R^2 Score  | 84.47%            | 89.91%                | 74.73%                 | 99.997%       | 99.94%  | 92.89%         |


We observe the following from the above comparison of the evaluation metrics:

* Random Forest and XGBoost outperform all other models with very low Mean Absolute Error (0.02 and 0.107 respectively) and high R^2 Score (99.997% and 99.94% respectively), indicating that they can accurately predict the target variable.
* The Neural Network model exhibits a relatively low Mean Absolute Error of 1.39 and a moderate R^2 Score of 92.89%, indicating that it has a reasonable level of predictive power. However, it is noteworthy that the model was only run on 5 epochs, and increasing the number of epochs can lead to a significant improvement in prediction performance. A neural network model trained on a higher number of epochs can potentially achieve a performance level closer to that observed in Random Forest and XGBoost models, which demonstrated highly accurate temperature prediction capabilities.
* The Linear and Polynomial Regression models perform the worst with higher Mean Absolute Error (2.342 and 1.879 respectively) and lower R^2 Score (84.47% and 89 92% respectively).
* The Polynomial Regression model with L1 penalty exhibits a slightly higher Mean Absolute Error of 2.936 and a lower R^2 Score of 74.73% compared to the other Polynomial Regression model as the model with L1 penalty only had 4 significant features. This suggests that the L1 penalty has limited the model's ability to capture the underlying relationship between the predictors and the target variable, leading to a less accurate prediction performance. 


## Conclusion
<br/>

Based on the results obtained from the different models, we can conclude that Random Forest and XGBoost models are the best choices for predicting the target variable accurately, while the Neural Network model can provide a reasonable level of prediction performance. This performance can be improved upon with higher training epochs.

The performance of XGBoost is particularly impressive, as demonstrated by its impressive performance on the Max Absolute error metric, especially when considering that the temperature data is rounded to the nearest degree. It is noteworthy that in the EV industry, achieving a worst-case temperature prediction error of less than 5 degrees is considered state-of-the-art, and the XGBoost model's performance is comparable to that standard.

On the other hand, Linear and Polynomial Regression models perform the worst in terms of prediction accuracy. Overall, the study highlights the potential of machine learning algorithms for accurate temperature prediction in the EV industry, with Random Forest and XGBoost being the most effective models.

In the electric vehicle industry, accurate temperature prediction is critical for optimizing bettery performance and extending battery life to avoid battery failure and preventing accidents. The results of this study indicate that machine learning algorithms like Random Forest and XGBoost with the given set of features, can provide highly accurate temperature predictions, which can lead to improved battery performance and longevity.