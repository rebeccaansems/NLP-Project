import pandas
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report
from sklearn import svm

#importing dataset
dataset = pandas.read_csv('Data.csv')

x = dataset.iloc[:, 8:10].values
y = dataset.iloc[:, 1].values

#spliting the dataset into training and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

clf = svm.SVC(kernel='rbf', C=1).fit(x_train, y_train)

print "CV Score: ",
print clf.score(x_test, y_test)

print "\nClassification Report:"
print classification_report(y, clf.predict(x))