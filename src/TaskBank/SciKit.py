from sklearn.cluster import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.cluster
from sklearn.linear_model import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model
from sklearn.naive_bayes import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.naive_bayes
from sklearn.svm import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.svm
from sklearn.ensemble import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.ensemble
from sklearn.discriminant_analysis import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.discriminant_analysis
from sklearn.tree import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.tree
from sklearn.ensemble import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.ensemble
from sklearn import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
from sklearn import model_selection
import numpy as np
import os


def fit(model, x, y=None, **kwargs):
    return model.fit(x, y, **kwargs)


def predict(model, x, **kwargs):
    return model.predict(x, **kwargs)


def train_test_split(x, y, **kwargs):
    return model_selection.train_test_split(x, y, **kwargs)


# descriptive variables
def gini_index(array):
    # all values are treated equally, arrays must be 1d
    array = np.array(array).flatten().astype(float)
    if np.amin(array) < 0:
        array -= np.amin(array)  # values cannot be negative
    array += np.finfo(float).tiny  # values cannot be 0
    array = np.sort(array)  # values must be sorted
    index = np.arange(1, array.shape[0] + 1)  # index per array element
    n = array.shape[0]  # number of array elements
    return (np.sum((2 * index - n - 1) * array)) / (
        n * np.sum(array)
    )  # Gini coefficient
