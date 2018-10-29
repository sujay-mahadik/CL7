#!/usr/bin/env python
# coding: utf-8

# In[78]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics


# In[79]:


iris_data = datasets.load_iris()
#print("Data: ", iris_data['data'])
#print("Target: ", iris_data['target'])


# In[80]:


X_train, X_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size = 0.3, random_state = 111)


# In[81]:


clf = svm.SVC(kernel = 'linear')
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)


# In[82]:


print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))


# In[84]:


def v_sepal():
    sepal_data = iris_data.data[:, :2]
    sepal_target = iris_data.target
    
    plt.scatter(sepal_data[:, 0], sepal_data[:, 1], c = sepal_target)
    plt.xlabel("Sepal length")
    plt.ylabel("Sepal width")
    plt.show
    
v_sepal()


# In[85]:


def v_petal():
    petal_data = iris_data.data[:, 2:]
    petal_target = iris_data.target
    
    plt.scatter(petal_data[:, 0], petal_data[:, 1], c = petal_target)
    plt.xlabel("Petal length")
    plt.ylabel("Petal width")
    plt.show
    
v_petal()


# In[100]:


iris = datasets.load_iris()

X = iris.data[:, :2]
y = iris.target

clfv = svm.SVC(kernel = 'linear', gamma = 'scale')
clfv.fit(X, y)

h = 0.02

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                    np.arange(y_min, y_max, h))

Z = clfv.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha = 0.3)

plt.scatter(X[:, 0], X[:, 1], c = y)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Speal SVM')
plt.show()


# In[ ]:




