#!/usr/bin/python
# -*- coding: utf-8 -

import sys
from DatasetSplitter import DatasetSplitter
import Features

class SkynetDetector:
    def __init__(self, features):
        self._features = features
        self._data_classes = []
        self._features_data = []

    def train(self, file_path):
        splitter = DatasetSplitter(line_callback=self._process_sentence, end_file_callback=self._process_end_file)
        splitter.split(file_path)

    def _process_sentence(self, class_sentence, sentence):
        self._data_classes.append(class_sentence)
        self._features_data.append(self._process_features(sentence))

    def _process_features(self, sentence):
        feature_vector = []
        for feature in self._features:
            feature_vector.append(feature.process(sentence))

        return feature_vector

    def evaluate(self, sentence):
        return 0.5

    def _process_end_file(self):
        pass

if __name__ == "__main__":
    DEFAULT_INPUT_PATH = "../data/training.txt"

    input_file_path = DEFAULT_INPUT_PATH
    if len(sys.argv) == 2:
        input_file_path = sys.argv[1]

    features = [Features.Feature1(), Features.Feature2(), Features.Feature3()]

    a = SkynetDetector(features)
    print "Splitting..."
    a.train(input_file_path)
    print "Separated successfully the files"
