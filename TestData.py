import pandas
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import svm

#importing dataset
dataset = pandas.read_csv('Data.csv')

x = dataset.iloc[:, 9:10].values
y = dataset.iloc[:, 1].values

#spliting the dataset into training and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

clf = svm.SVC().fit(x_train, y_train)
print clf.score(x_test, y_test)