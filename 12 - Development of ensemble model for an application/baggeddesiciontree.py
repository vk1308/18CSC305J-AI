import pandas
from sklearn import model_selection
from sklearn.ensemble import BaggingClassifier from sklearn.tree import DecisionTreeClassifier

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/p ima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'ag e','class']
dataframe = pandas.read_csv(url, names=names)


array = dataframe.values X = array[:,0:8]
Y = array[:,8] seed = 7
kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffl e=True)
cart = DecisionTreeClassifier() num_trees = 100

model = BaggingClassifier(base_estimator=cart, n_estimators=num_tree s, random_state=seed)
results = model_selection.cross_val_score(model, X, Y, cv=kfold) print(results)

print(results.mean())
