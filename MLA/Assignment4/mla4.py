from copy import deepcopy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data set is given below
df = pd.DataFrame({
'x': [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
'y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
})
# generate random numbers
np.random.seed(200)
k = 3
#centroids[i] = [x, y]
# Return random integers
centroids = {
i+1:[np.random.randint(0, 80), np.random.randint(0, 80)]
for i in range(k)
}
print("Centroid=",centroids)

plt.scatter(df['x'], df['y'], color='BLACK')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in centroids.keys(): #represent color centroid ..
 plt.scatter(*centroids[i], color=colmap[i]) # .keys() returns a view object that displays a list of all the keys.

plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

def assignment(df, centroids):
 for i in centroids.keys():
# start from 1 to 3 everytimes
 # sqrt((x1 - x2)^2 + (y1 - y2)^2)
  df['distance_from_{}'.format(i)] =( np.sqrt( (df['x'] - centroids[i][0]) ** 2 +(df['y'] - centroids[i][1]) ** 2 ))
  centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
  #.idmin)
  #finding the nearest data in the dataframe
  df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
  df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
  df['color'] = df['closest'].map(lambda x: colmap[x])
 return df
df = assignment(df, centroids)
print(df)

plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
 plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

import copy
old_centroids = copy.deepcopy(centroids) # create bindings between a target and an object.
def update(k):
 for i in centroids.keys():
  centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
  centroids[i][1] = np.mean(df[df['closest'] == i]['y'])
 return k
centroids = update(centroids)
print("Updated centroids ", centroids)

plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.3) # alpha value for intensity
for i in centroids.keys():
 plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()


