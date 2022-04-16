import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
%matplotlib inline data=pd.read_csv('mall_customers.csv') print(data.head()) 
inVsout=data.iloc[:,[3,4]]
inVsout plt.scatter(inVsout.iloc[:0],inVsout.iloc[:,1]) kmeans=KMeans(n_clusters=5)
kmeans.fit(inVsout) plt.scatter(inVsout.iloc[:0],inVsout.iloc[:,1],c=kmeans.labels_,cmap='rain bow')
plt.show()
