import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
 from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
 dataset = pd.read_csv('diabetes.csv') 
print(dataset.head())
dataset = pd.read_csv('diabetes.csv') print(dataset.head())
dataset.head() 
def diagnosis(x):
if x=='M' :
 return 1
if x=='B' : 
return 0

dataset['DiabetesPedigreeFunction'] = dataset['DiabetesPedigreeFunction'].apply(diagnosis) print(dataset)
svc_classifier=SVC(kernel='rbf') svc_classifier
Y = dataset['DiabetesPedigreeFunction']
X = dataset.drop(columns=['DiabetesPedigreeFunction']) X_train, X_test, Y_train, Y_test = train_test_split(X, Y, 
test_size=0.2, random_state=9)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=9)

print('X train shape: ', X_train.shape) print('Y train shape: ', Y_train.shape) print('X test shape: ', X_test.shape) 
print('Y test shape: ', Y_test.shape) svc_classifier= SVC(kernel='poly')
