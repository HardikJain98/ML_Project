################################################
#                 Libraries
################################################
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import statsmodels.api as sm
import os
from models import evaluate

################################################
#     Relative Paths to Inputs/Outputs
################################################
path_to_figs_dir = '../figs/'
path_to_all_data_reduced = "../dataset/all_trips_reduced.csv"
RANDOM_FOREST_PICKLE = "pkl/random_forest.pkl"
BEST_RANDOM_FOREST_PICKLE = "pkl/best_random_forest.pkl"

# Read the data
with open(path_to_all_data_reduced, encoding="utf-8", errors="ignore") as f:
    data = pd.read_csv(f, delimiter=",")

# Drop trip_id column for
data = data.drop(columns=["trip_id"])

# Split data into features (X) and target (y). Temperature is the last column!
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

################################################
#     Fetch or train grid search cv
################################################
def build_random_forest_params():
    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # create a Random Forest Regressor
    rfr = RandomForestRegressor( n_jobs=-1)

    # Define the search space
    param_grid = {
        "n_estimators": [2, 5, 10, 20, 50, 75, 100],
        "max_depth": [None, 2, 3, 4, 5],
        "max_features": ["sqrt", "log2", None],
        "min_samples_split": [12, 15, 17],
        "min_samples_leaf": [4, 6, 8],
        "random_state": [42]
    }

    # Perform grid search with 5 fold cross validation
    grid_search = GridSearchCV(estimator=rfr, param_grid=param_grid, cv=5, scoring="neg_mean_squared_error")
    grid_search.fit(X_train, y_train)

    # Save the state
    random_forest = {
        "train_indices" : X_train.index,
        "test_indices"  : X_test.index,
        "grid_search"   : grid_search
    }
    with open(RANDOM_FOREST_PICKLE, "wb") as f:
        pickle.dump(random_forest, f)

    return X_train, y_train, X_test, y_test, grid_search

if os.path.exists(RANDOM_FOREST_PICKLE):
    # If pre-trained, take the values
    with open(RANDOM_FOREST_PICKLE, "rb") as f:
        random_forest = pickle.load(f)

    train_indices = random_forest["train_indices"]
    test_indices  = random_forest["test_indices"]
    grid_search   = random_forest["grid_search"]

    X_train       = X.iloc[train_indices]
    y_train       = y.iloc[train_indices]
    X_test        = X.iloc[test_indices]
    y_test        = y.iloc[test_indices]
else:
    # Train the random forest regressor
    X_train, y_train, X_test, y_test, grid_search = build_random_forest_params()


################################################
#     Fetch or train the best rf regressor
################################################
print("Best hyperparameters:", grid_search.best_params_)
print("Best mean squared error score:", -grid_search.best_score_)

if os.path.exists(BEST_RANDOM_FOREST_PICKLE):
    # If the best random forest model is saved, retreive
    with open(BEST_RANDOM_FOREST_PICKLE, "rb") as f:
        best_rf = pickle.load(f)
else:
    # Else build it
    best_rf = RandomForestRegressor(
            max_depth = grid_search.best_params_["max_depth"],
            max_features = grid_search.best_params_["max_features"],
            min_samples_leaf = grid_search.best_params_["min_samples_leaf"],
            min_samples_split = grid_search.best_params_["min_samples_split"],
            n_estimators = grid_search.best_params_["n_estimators"],
            random_state = grid_search.best_params_["random_state"],
            n_jobs = -1)

    best_rf.fit(X_train, y_train)

    # Save it
    with open(BEST_RANDOM_FOREST_PICKLE, "wb") as f:
        pickle.dump(best_rf, f)


################################################
#      Predict on data that is never seen
################################################
y_test_pred = best_rf.predict(X_test)
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
plt.title("Random Forest Regression")
plt.savefig(path_to_figs_dir + 'rf_errplot.png', format='png', bbox_inches='tight')
plt.close()

################################################
#            Look At Residual Plots
################################################
plt.figure()
sns.residplot(x=y_test_pred, y=y_test, data=pd.concat([X_test, y_test], axis=1))
plt.xlabel("Estimated Temperature [deg C]")
plt.ylabel("Residuals")
plt.title("Random Forest Regression")
plt.savefig(path_to_figs_dir + 'rf_residualplot.png', format='png', bbox_inches='tight')
plt.close()
