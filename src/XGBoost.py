################################################
#                 Libraries
################################################
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import pickle
import os
from models import evaluate

################################################
#     Relative Paths to Inputs/Outputs
################################################
path_to_figs_dir = '../figs/'
path_to_all_data_reduced = "../dataset/all_trips_reduced.csv"
XGBOOST_PICKLE = "pkl/xgboost.pkl"
BEST_XGBOOST_PICKLE = "pkl/best_xgboost.pkl"

# Read the data
with open(path_to_all_data_reduced, encoding="utf-8", errors="ignore") as f:
    data = pd.read_csv(f, delimiter=",")

# Drop trip_id column for
data = data.drop(columns=["trip_id"])

# Split data into features (X) and target (y). Temperature is the last column!
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

X.columns = X.columns.str.replace('[', '(').str.replace(']', ')').str.replace('<', '_').str.replace('>', '_')

################################################
#     Fetch or train grid search cv
################################################
def build_xgboost_params():
    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # create a Random Forest Regressor
    xgb_model = xgb.XGBRegressor(objective="reg:linear", random_state=42)

    # Define the search space
    params = {
        'min_child_weight': [5, 10, 15],
        'gamma': [0.2, 0.6, 1.0],
        'subsample': [0.6, 0.8, 1.0],
        'colsample_bytree': [1.0, 1.6, 2.0],
        'max_depth': [2, 5, 8]
    }

    # Performing 5-fold cross validation for hyperparameter tuning 

    cv = KFold(n_splits=5, shuffle=True, random_state=42)
    grid = GridSearchCV(
        estimator=xgb_model,
        param_grid=params,
        scoring="neg_mean_squared_error",
        n_jobs=-1,
        cv=cv,
    )
    grid.fit(X_train, y_train)

    # Save the state
    xg_boost_state = {
        "train_indices" : X_train.index,
        "test_indices"  : X_test.index,
        "xgboost_parameters" : grid
    }
    with open(XGBOOST_PICKLE, "wb") as f:
        pickle.dump(xg_boost_state, f)

    return X_train, y_train, X_test, y_test, grid

if os.path.exists(XGBOOST_PICKLE):
    # If pre-trained, take the values
    with open(XGBOOST_PICKLE, "rb") as f:
        xgboost = pickle.load(f)

    train_indices = xgboost["train_indices"]
    test_indices  = xgboost["test_indices"]
    grid_results  = xgboost["xgboost_parameters"]

    X_train       = X.iloc[train_indices]
    y_train       = y.iloc[train_indices]
    X_test        = X.iloc[test_indices]
    y_test        = y.iloc[test_indices]
else:
    # Train the random forest regressor
    X_train, y_train, X_test, y_test, grid_results = build_xgboost_params()


################################################
#     Fetch or train the best rf regressor
################################################
print('All results:', grid_results.cv_results_)
print("Best hyperparameters:", grid_results.best_params_)
print('Best estimator:', grid_results.best_score_)

if os.path.exists(BEST_XGBOOST_PICKLE):
    # If the best random forest model is saved, retreive
    with open(BEST_XGBOOST_PICKLE, "rb") as f:
        best_xgb = pickle.load(f)
else:
    # Else build it
    best_xgb = xgb.XGBRegressor(
        min_child_weight = grid_results.best_params_['min_child_weight'],
        gamma = grid_results.best_params_['gamma'],
        subsample = grid_results.best_params_['subsample'],
        colsample_bytree =  grid_results.best_params_['colsample_bytree'],
        max_depth = grid_results.best_params_['max_depth'],
        n_jobs = -1)

    best_xgb.fit(X_train, y_train)

    # Save it
    with open(BEST_XGBOOST_PICKLE, "wb") as f:
        pickle.dump(best_xgb, f)


################################################
#      Predict on data that is never seen
################################################
y_test_pred = best_xgb.predict(X_test)
mae, mape, max_error, r2, adj_r2 = evaluate(y_test, y_test_pred, X_test.shape[1])
print("Mean Absolute Error: ", mae)
print("Max Absolute Error: ", max_error)
print("R^2 Score: ", r2)
print("Adjusted R^2 Score: ", adj_r2)

################################################
#            Look At Error Histograms
################################################
errors = y_test - y_test_pred
plt.figure()
arr = plt.hist(errors, bins=10)
for i in range(10):
    plt.text(arr[1][i],arr[0][i],str(arr[0][i]))
plt.xlabel("Estimation Error [deg C]")
plt.ylabel("Count")
plt.title("XGBoost Regression")
plt.savefig(path_to_figs_dir + 'xgb_errplot.png', format='png', bbox_inches='tight')
plt.close()

################################################
#            Look At Residual Plots
################################################
plt.figure()
sns.residplot(x=y_test_pred, y=y_test, data=pd.concat([X_test, y_test], axis=1))
plt.xlabel("Estimated Temperature [deg C]")
plt.ylabel("Residuals")
plt.title("XGBoost Regression")
plt.savefig(path_to_figs_dir + 'xgb_residualplot.png', format='png', bbox_inches='tight')
plt.close()

################################################
#            Look At Residual Q-Q Plots
################################################

plt.figure()
sm.qqplot(errors, line='45')
plt.title("XGBoost Error Q-Q Plot")
plt.savefig(path_to_figs_dir + 'xgb_qqplot.png', format='png', bbox_inches='tight')
plt.close()