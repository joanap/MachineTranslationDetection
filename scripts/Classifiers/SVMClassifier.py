from sklearn import datasets, svm
from ClassifierAbstract import *


class SVMClassifier(ClassifierAbstract):
    def __init__(self, kernel='rbf', gamma=10):
        ClassifierAbstract.__init__(self)
        self._add_arguments_description("'" + kernel + "'", gamma)
        self.classifier = svm.SVC(kernel=kernel, gamma=gamma)

    def train(self, feature_matrix, classes):
        self.classifier.fit(feature_matrix, classes)

    def predict(self, x):
        return self.classifier.predict(x)