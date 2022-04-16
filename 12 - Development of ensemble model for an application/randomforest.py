import pandas
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier


url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/p ima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'ag e','class']
dataframe = pandas.read_csv(url, names=names)


array = dataframe.values X = array[:,0:8]
Y = array[:,8] seed = 7




num_trees = 100
max_features = 3




kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffl e=True)
model = RandomForestClassifier(n_estimators=num_trees, max_features= max_features)
results1 = model_selection.cross_val_score(model, X, Y, cv=kfold)

print(results1) print(results1.mean())
