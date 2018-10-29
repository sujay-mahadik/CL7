#!/usr/bin/env python
# coding: utf-8

# In[77]:


from sklearn import svm, datasets
import numpy as np
import matplotlib.pyplot as plt


# In[78]:


iris_dataset = datasets.load_iris()


# In[79]:


from sklearn.model_selection import train_test_split


# In[80]:


X_train, X_test, y_train, y_test = train_test_split(iris_dataset.data[:, :2], iris_dataset.target, test_size = 0.25, random_state = 107)


# In[81]:


print("Data Description: ", iris_dataset['DESCR'])


# In[82]:


print("Iris Data: ", iris_dataset['data'])


# In[83]:


print("Iris Target: ", iris_dataset['target'])


# In[84]:


def v_sepal():
    sepal_data = iris_dataset.data[:, :2]
    sepal_target = iris_dataset.target
    
    plt.scatter(sepal_data[:, 0], sepal_data[:, 1], c = sepal_target)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.show()

v_sepal()


# In[85]:


def v_petal():
    petal_data = iris_dataset.data[:, -2 :]
    petal_target = iris_dataset.target
    
    plt.scatter(petal_data[:, 0], petal_data[:, 1], c = petal_target)
    plt.xlabel('Petal length')
    plt.ylabel('Petal width')
    plt.show()

v_petal()


# In[86]:


clf = svm.SVC(kernel = 'linear', C = 1.0)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)


# In[90]:


from sklearn import metrics

print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))


# In[108]:


iris = datasets.load_iris()
X = iris_dataset.data[:, :2]
y = iris_dataset.target


h = .02 
 
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

title = 'SVM Liner Petal Sepal'

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha = 0.8)

plt.scatter(X[:, 0], X[:, 1], c = y)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())
plt.title(title)
plt.show()

