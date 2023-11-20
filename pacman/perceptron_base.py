import pandas as pd
import numpy as np
import random
from sklearn.preprocessing import StandardScaler

def read_data(filename):
    #reads in a csv and sements the data
    #randomizes the order of the data, then splits it into different sets
    #returns separate inputs (x) and outputs (y) for each of training and test
    #also returns a list of column names, with 'class' and 'class_name' removed
    #this may be useful for determining heavily weighted features
    df = pd.read_csv(filename)
    data = df.to_numpy()
    np.random.shuffle(data)
    x = data[:,1:-1]
    x = StandardScaler().fit_transform(x)
    y = data[:,0]
    test_size = int(0.2* data.shape[0])
    x_train = x[test_size:]
    y_train = y[test_size:]
    x_test = x[:test_size]
    y_test = y[:test_size]
    return x_train, y_train, x_test, y_test, df.columns.values[1:-1]

def compute_perceptron_error(x,y, weights, bias):
    #takes in a matrix of feature vectors x and a vector of class labels y
    #also takes a vector weights and a scalar bias for the classifier
    #returns the error on the data (x, y) of the perceptron classifier
    y_pred = np.sign(x.dot(weights) + bias)
    accuracy = (y == y_pred).sum()/len(y)
    return 1 - accuracy


def rank_features(weights, feats):
    #takes in a weight vector and an array of feature names
    #returns a sorted array of features, sorted from most negatively weighted to most positively weighted
    #note that feats MUST be a numpy array of the same length as weights
    #if feats[i] does not correspond to weights[i], this will not return accurate results
    imp = np.argsort(weights)
    return feats[imp]

x_train, y_train, x_test, y_test, feats = read_data('rice.csv') #read the data

w = np.random.rand(len(x_train[0])) #initialize weights randomly
b = random.random() #initialize bias randomly

def sig(x):
    if x<0:
        return -1
    elif x>0:
        return 1
    else:
        return 0


for x in range(0,5):
    for i in range(len(x_train)):
        xi = x_train[i]
        yi = y_train[i]

        if sig(xi.dot(w) + b) != yi:
            w += yi * xi
            b += yi


error = compute_perceptron_error(x_train, y_train, w, b)

while True:
    for i in range(len(x_train)):
        xi = x_train[i]
        yi = y_train[i]

        if sig(xi.dot(w) + b) != yi:
            w += yi * xi
            b += yi

    temp_error = compute_perceptron_error(x_train, y_train, w, b)
   
    if temp_error > error and error != 0:
        print("training is good enough")
        break

    error = temp_error

print(rank_features(w,feats))

print(error)

print(compute_perceptron_error(x_test, y_test, w, b))