import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data=pd.read_csv("headbrain.csv")
#print(data)
#Let us divide data set in training and testing data sets
X_train =data[:200]
X_test =data[200:]

#print("Training data set as follows") #print(X_train) #print("Testing data set as follows") #print(X_test)

X = X_train['Head Size(cm^3)'].values
Y = X_train['Brain Weight(grams)'].values
mean_x = np.mean(X)
mean_y = np.mean(Y)

#print(X) #print(Y)

print("Printing mean x")
print(mean_x)
print("Printing mean y")
print(mean_y)

m = len(X)
print("Number of samples in training set")
print(m)
numer = 0
denom = 0
for i in range(m):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2

b1 = numer / denom
b0 = mean_y - (b1 * mean_x)
print("Coefficient and bias is as follows")
print(b1, b0)

# Plotting Values and Regression Line
max_x = np.max(X)
min_x = np.min(X)

# Calculating line values x and y
x = np.linspace(min_x, max_x)
y = b0 + b1 * x

# Ploting Line
plt.plot(x, y, color='YELLOW', label='Regression Line')

# Ploting Scatter Points
plt.scatter(X, Y, c='GREEN', label='Scatter Plot headsize vs brain wt')

plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()

# Calculating Root Mean Squares Error
sse = 0
for i in range(m):
    y_pred = b0 + b1 * X[i]   #y_pred i.e brain wt= bo=b1* head size
    sse += (Y[i] - y_pred) ** 2    #Y[i] means brain weight

print("Mean sqaure error of brain wt  of train data",sse)
mse = sse/m
rmse = np.sqrt(mse)
print("Root Mean sqaure error is",rmse)

# Score of determination starts here #The coefficient of determination (denoted by R2) is a key output of regression analysis
# The coefficient of determination is the square of the correlation (r) between predicted y scores and actual y scores; #thus, it ranges from 0 to 1.
ss_t = 0
ss_r = 0
for i in range(m):
    y_pred = b0 + b1 * X[i]
    ss_t += (Y[i] - mean_y) ** 2
    ss_r += (Y[i] - y_pred) ** 2
scorer2 = 1 - (ss_r/ss_t)
print("R^2 score for training data is",scorer2)
