# -*- coding: utf-8 -*-

import sys
from SkynetDetector.SkynetDetector import SkynetDetector
from Classifiers.SVMClassifier import *
from Features.WordCounter import WordCounter

if __name__ == "__main__":
    train_file, test_file = None, None
    if len(sys.argv) == 2:
        train_file = sys.argv[1]
    elif len(sys.argv) == 3:
        train_file, test_file = sys.argv[1], sys.argv[2]
    else:
        print "Usage", __name__, "<train_file_dir>", "<test_file_dir"
        sys.exit(1)

    # best features
    classifier = SVMClassifier()
    features = [WordCounter()]

    # Evaluate the accuracy of the model
    a = SkynetDetector(classifier, features)
    print "Training..."
    a.train(train_file)

    print "Testing..."
    accuracy = a.accuracy(test_file)
    print accuracy

    sys.exit(0)