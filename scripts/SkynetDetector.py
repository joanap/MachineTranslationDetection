#!/usr/bin/python
# -*- coding: utf-8 -

import sys

from DatasetSplitter import DatasetSplitter
from scripts.Features.Features import *
from Stats import Stats


class SkynetDetector:
    def __init__(self, features_processors):
        self._features = features_processors
        self._data_classes = []
        self._features_data = []
        self.stats = None

    def train(self, file_path):
        splitter = DatasetSplitter(line_callback=self._process_sentence)
        splitter.split(file_path)

    def _process_sentence(self, class_sentence, sentence):
        self._data_classes.append(class_sentence)
        self._features_data.append(self._process_features(sentence))

    def _process_features(self, sentence):
        feature_vector = []
        for feature in self._features:
            feature_vector.append(feature.process(sentence))

        return feature_vector

    def evaluate(self, expected_class_sentence, sentence):
        self.stats.add(expected_class_sentence, self.predict(sentence))

    def predict(self, sentence):
        # call SVM.predict with the sentence
        return 1

    def accuracy(self, file_path):
        self.stats = Stats()

        splitter = DatasetSplitter(line_callback=self.evaluate)
        splitter.split(file_path)

        return self.stats.accuracy()

if __name__ == "__main__":
    train_file = "../data/train_dataset.txt"
    test_file = "../data/test_dataset.txt"

    input_file_path = train_file
    if len(sys.argv) == 2:
        input_file_path = sys.argv[1]
    elif len(sys.argv) == 3:
        input_file_path, test_file = sys.argv[1], sys.argv[2]

    features = [Feature1(), Feature2(), Feature3()]

    a = SkynetDetector(features)
    print "Training..."
    a.train(input_file_path)

    print "Testing..."
    accuracy = a.accuracy(test_file)
    print accuracy
