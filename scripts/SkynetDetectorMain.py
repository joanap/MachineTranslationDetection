#!/usr/bin/python
# -*- coding: utf-8 -

import sys
from scripts.SkynetDetector.SkynetDetector import SkynetDetector
from scripts.Features.Features import *
from Classifiers.SVMClassifier import *

if __name__ == "__main__":
    train_file = "../data/train_dataset.txt"
    test_file = "../data/test_dataset.txt"

    input_file_path = train_file
    if len(sys.argv) == 2:
        input_file_path = sys.argv[1]
    elif len(sys.argv) == 3:
        input_file_path, test_file = sys.argv[1], sys.argv[2]

    # best features
    classifier = SVMClassifier()
    features = [Feature1(), Feature2(), Feature3()]

    a = SkynetDetector(classifier, features)
    print "Training..."
    a.train(input_file_path)

    print "Testing..."
    accuracy = a.accuracy(test_file)
    print accuracy