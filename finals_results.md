---
layout: page
title: Results - Finals
permalink: /finals_results
nav_order: 10
---

# Core Temperature Estimation of Electric Vehicle Battery Packs

## Results for Finals submission
<br/>

### Random Forest Regression Results

* Since, we had divided the entire dataset into 80:20 (Train:Test) split with 80% of data being used to train and cross validate, only 20% of unseen datapoint was used to evaluate the model.
* [Table 4](finals_results#random-forest-regression-results) captures the evaluation metrics of interest.
* It is patent that Random Forest Regression clearly improved on all aspects when compared to the previously used models of midterm submission:
    * Mean Absolute Error of **0.002** against **1.89** of Polynomial Regression (best in the category)
    * Max Absolute Error of **5.224** against **11.45** of Polynomial Regression with l1 penality (best in the category)
    * R^2 Score and adjusted R^2 score of **99.997%** against **89.91%** of Polynomial Regression (best in the category)

| Evaluation Metric   | Score   |
| -----------------   | -----   |
| Mean Absolute Error | 0.002   |
| Max Absolute Error  | 5.224   |
| R^2 Score           | 99.997% |
| Adjusted R^2 Score  | 99.997% |

<center> <b> Table 4: Various Metrics of evaluation for Random Forest Regression </b> </center>

* Figure 16 captures the distribution of residuals of random forest regression. It can be seen that the error distributions is centered at 0 with a slightly longer left tail however with a negligibly small standard deviation.
* Further examination of Figure 16 also reveals that for the random forest regression model, the maximum absolute error corresponds to rare scenarios, displaying the robustness of the model.

![image](figs/rf_errplot.png)
<center> <b> Figure 16: Error Distribution of Random Forest Regression </b> </center>

* Figure 17 shows the residuals spread across the predicted values of battery temperature, displaying constant and small variation of errors across the predicted values.

![image](figs/rf_residualplot.png)
<center> <b> Figure 17: Residual Plot of Random Forest Regression </b> </center>
