# models.py
# Kartik Sastry
# 3/12/2022

# Description:
# Contains two functions per regression model:
# 1. train
# 2. predict

# Usage:
# Functions will be called in model_evaluation.py

# Inputs:
# - 

# Outputs:
# - 

################################################
#                 Libraries
################################################
# ml-project-env has Scikit-learn, TensorFlow, PyTorch, Keras
# If other modules are needed, remember to update ml-project-env
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.regularizers import l2

################################################
#                  evaluate
################################################
def evaluate(y_test, y_test_pred):
    """
    Function to evaluate regression model performance
    This is common to all models.

    Args:
        y_test: length N numpy array of ground truth values
        y_test_pred: length N numpy array predictions

    Return:
        metrics: list of error values
    """

    # calculate mean absolute error
    mae = np.mean(np.abs(y_test - y_test_pred))

    # calculate max absolute error
    max_error = np.max(np.abs(y_test - y_test_pred))

    # return a list of error values
    return [mae, max_error]

################################################
#                  Model 1
################################################
def model_1_train(X_train, y_train):
    """
    Function to train Regression Model 1.

    Args:
        X_train: N x D numpy array of feature values
            (where N is # observations and D is the dimensionality)
        Y_train: length N numpy array of temperature values
            * let us agree to force vectors into shape (N, ) instead of shape (N, 1) to avoid issues *

    Return:
        trained model object
    """

    # include a bias/intercept term; copy X so that it doesn't get overwritten
    model = linear_model.LinearRegression(fit_intercept=True, copy_X=True)

    # train model
    model.fit(X_train, y_train)

    # return trained model
    return model

def model_1_predict(model_object, X_test):
    """
    Function to predict using a trained Regression Model 1.

    Args:
        model_object: trained model object model_1_train
        X_test: N x D numpy array of feature values
            * N is # observations and D is the dimensionality *
    Return:
        Y_est: length N numpy array of temperature values
            * let us agree to use force vectors into shape (N, ) instead of shape (N, 1) to avoid issues *
    """

    # predict and return
    y_pred = model_object.predict(X_test)
    return y_pred

################################################
#                  Model 2
################################################
def model_2_train(X_train, y_train):
    """
    Function to train Regression Model 2.

    Args:
        X_train: N x D numpy array of feature values
            (where N is # observations and D is the dimensionality)
        Y_train: length N numpy array of temperature values
            * let us agree to force vectors into shape (N, ) instead of shape (N, 1) to avoid issues *

    Return:
        trained model object
    """

    # does the feature transformation. train it for later transforming
    scaler = preprocessing.StandardScaler().fit(X_train.copy())
    transformer = preprocessing.PolynomialFeatures(degree=2)

    # transform, making sure to not transform X_train
    X_train_poly = transformer.fit_transform(scaler.transform(X_train.copy()))

    # include a bias/intercept term; copy X so that it doesn't get overwritten
    model = linear_model.LinearRegression(fit_intercept=True, copy_X=True)

    # train model
    model.fit(X_train_poly, y_train)

    # return trained model
    return (scaler, transformer, model)

def model_2_predict(model_object, X_test):
    """
    Function to predict using a trained Regression Model 2.

    Args:
        model_object: trained model object model_1_train
        X_test: N x D numpy array of feature values
            * N is # observations and D is the dimensionality *
    Return:
        Y_est: length N numpy array of temperature values
            * let us agree to use force vectors into shape (N, ) instead of shape (N, 1) to avoid issues *
    """

    # unpack input
    scaler = model_object[0]
    transformer = model_object[1]
    model = model_object[2]

    # transform, making sure to not transform X_test. Use the pre-trained scaler
    X_test_poly = transformer.fit_transform(scaler.transform(X_test.copy()))

    # predict and return
    y_pred = model.predict(X_test_poly)
    return y_pred

################################################
#                  Model 3
################################################
def model_3_train(X_train, y_train, alpha=1.0):
    """
    Function to train Regression Model 3.

    Args:
        X_train: N x D numpy array of feature values
            (where N is # observations and D is the dimensionality)
        Y_train: length N numpy array of temperature values
            * let us agree to force vectors into shape (N, ) instead of shape (N, 1) to avoid issues *

    Return:
        trained model object
    """

    # does the feature transformation. train it for later transforming
    scaler = preprocessing.StandardScaler().fit(X_train.copy())
    transformer = preprocessing.PolynomialFeatures(degree=2)

    # transform, making sure to not transform X_train
    X_train_poly = transformer.fit_transform(scaler.transform(X_train.copy()))

    # include a bias/intercept term; copy X so that it doesn't get overwritten
    model = linear_model.Lasso(alpha, fit_intercept=True, copy_X=True)

    # train model
    model.fit(X_train_poly, y_train)

    # return trained model
    return (scaler, transformer, model)

def model_3_predict(model_object, X_test):
    """
    Function to predict using a trained Regression Model 3.

    Args:
        model_object: trained model object model_1_train
        X_test: N x D numpy array of feature values
            * N is # observations and D is the dimensionality *
    Return:
        Y_est: length N numpy array of temperature values
            * let us agree to use force vectors into shape (N, ) instead of shape (N, 1) to avoid issues *
    """

    # unpack input
    scaler = model_object[0]
    transformer = model_object[1]
    model = model_object[2]

    # transform, making sure to not transform X_test. Use the pre-trained scaler
    X_test_poly = transformer.fit_transform(scaler.transform(X_test.copy()))

    # predict and return
    y_pred = model.predict(X_test_poly)
    return y_pred

################################################
#                  Model 4
################################################
def model_4_train(X_train, y_train):
    """
    Function to train Regression Model 4.

    Args:
        X_train: N x D numpy array of feature values
            (where N is # observations and D is the dimensionality)
        Y_train: length N numpy array of temperature values
            * let us agree to force vectors into shape (N, ) instead of shape (N, 1) to avoid issues *

    Return:
        trained model object
        
    """
    #print(X_train.shape)
    #scaler = preprocessing.StandardScaler().fit(X_train.copy())
    #transformer = preprocessing.PolynomialFeatures(degree=2)

    # model = Sequential()
    # model.add(Dense(32, input_dim=11, activation='relu'))
    # model.add(Dense(16, activation='relu'))
    # model.add(Dense(4, activation='relu'))

    # model.add(Dense(1, activation='sigmoid'))

    # # compile the model
    # model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # model.fit(X_train, y_train, epochs=1, batch_size=12)

    model = Sequential()
    model.add(Dense(64, input_dim=11, activation='relu', kernel_regularizer=l2(0.01)))
    model.add(Dense(32, activation='relu', kernel_regularizer=l2(0.01)))
    model.add(Dense(1, activation='linear'))

# compile the model
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mse'])

# train the model
    model.fit(X_train, y_train, epochs=5, batch_size=32, verbose=0)

    return model

def model_4_predict(model_object, X_test):
    """
    Function to predict using a trained Regression Model 4.

    Args:
        model_object: trained model object model_1_train
        X_test: N x D numpy array of feature values
            * N is # observations and D is the dimensionality *
    Return:
        Y_est: length N numpy array of temperature values
            * let us agree to use force vectors into shape (N, ) instead of shape (N, 1) to avoid issues *
    """
    # scaler = model_object[0]
    # transformer = model_object[1]
    # model = model_object[2]
    # X_test_NN = transformer.fit_transform(scaler.transform(X_test.copy()))
    y_pred = model_object.predict(X_test)
    return y_pred

