import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

#load iris data
iris = datasets.load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

#20% - 80% Test Training data split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

#LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(X_test, y_pred).transform(X)
plt.figure()
colors = ['green', 'black', 'red']
lw = 2

#Plot graph
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], alpha=.8, color=color,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA of IRIS dataset')
plt.show()