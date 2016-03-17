#!/usr/bin/python
# -*- coding: utf-8 -

from scripts.Classifiers.SVMClassifier import *
from DatasetSplitter import *
from Stats import *


class SkynetDetector:
    def __init__(self, classifier, features_processors):
        self._features = features_processors
        self._data_classes = []
        self._features_data = []
        self.stats = None
        self.classifier = classifier

    def train(self, file_path):
        splitter = DatasetSplitter(line_callback=self._process_sentence)
        splitter.split(file_path)

        # provide data to train svm
        self.classifier.train(self._features_data, self._data_classes)

    def predict(self, sentence):
        feature_vector = self._process_features(sentence)
        return self.classifier.predict([feature_vector])

    def accuracy(self, file_path):
        self.stats = Stats()

        splitter = DatasetSplitter(line_callback=self._evaluate)
        splitter.split(file_path)

        return self.stats.accuracy()

    def _process_sentence(self, class_sentence, sentence):
        self._data_classes.append(class_sentence)
        self._features_data.append(self._process_features(sentence))

    def _process_features(self, sentence):
        feature_vector = []
        for feature in self._features:
            feature_vector.append(feature.process(sentence))

        return feature_vector

    def _evaluate(self, expected_class_sentence, sentence):
        predicted_class = self.predict(sentence)
        self.stats.add(expected_class_sentence, predicted_class)