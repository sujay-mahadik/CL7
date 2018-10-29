#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import copy


# In[58]:


X = {}
Y = {}
for i in range(20):
    X[i] = np.random.randint(0, 80)
    Y[i] = np.random.randint(0, 80)


df = pd.DataFrame({
    'x' : X,
    'y' : Y
})
print(df)


# In[59]:


k = 3
centroids = {}
for i in range(k):
    centroids[i+1] = [np.random.randint(0,80), np.random.randint(0, 80)]

print(centroids)
plt.scatter(df['x'], df['y'])
colormap = { 1 : 'r', 2 : 'g', 3: 'b'}

for i in centroids.keys():
    plt.scatter(*centroids[i], color = colormap[i])


# In[60]:


col = []
for i in range(k):
    col.append('{}'.format(i+1))
print(col)
def assignment():
    for i in centroids.keys():
        df['{}'. format(i)] = np.sqrt((df['x'] - centroids[i][0]) ** 2 + (df['y'] - centroids[i][1]) ** 2 )
        df['closest'] = df.loc[:, col].idxmin(axis = 1)
        df['closest'] = df['closest'].map(lambda x : int(x))
        df['color'] = df['closest'].map(lambda x : colormap[x])
assignment()
print(df)


# In[61]:


plt.scatter(df['x'], df['y'], color = df['color'], alpha = 0.5)

for i in centroids.keys():
    plt.scatter(*centroids[i], color = colormap[i])


# In[62]:


def update():
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i] ['x'])
        centroids[i][1] = np.mean(df[df['closest'] == i] ['y'])
        
update()

print(centroids)


# In[63]:


while True:
    lastclosest = df['closest'].copy(deep = True)
    
    update()
    assignment()
    if lastclosest.equals(df['closest']):
        break


# In[64]:


plt.scatter(df['x'], df['y'], color = df['color'], alpha = 0.5)

for i in centroids.keys():
    plt.scatter(*centroids[i], color = colormap[i])

