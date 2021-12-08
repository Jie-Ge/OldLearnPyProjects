import pandas as pd
from sklearn import tree

dataSet = [[1, 1, 'yes'],
           [1, 1, 'yes'],
           [1, 0, 'no'],
           [0, 1, 'no'],
           [0, 1, 'no']]
dataSet = pd.DataFrame(data=dataSet, columns=['x1', 'x2', 'label'])
model = tree.DecisionTreeClassifier(criterion='entropy')
model.fit(dataSet.iloc[:, :-1], dataSet.iloc[:, -1])
print(model.predict([[1,0]]))