import sys
from SkynetDetector.SkynetDetector import SkynetDetector
from Features.Features import *
from Classifiers.SVMClassifier import *

if __name__ == "__main__":
    input_file = "../data/to_evaluate.txt"
    train_file = "../data/train_dataset.txt"

    if len(sys.argv) == 2:
        input_file = sys.argv[1]
    elif len(sys.argv) == 3:
        input_file, train_file = sys.argv[1], sys.argv[2]
    else:
        print "Incorrect number of arguments"
        sys.exit(1)

    # best features
    classifier = SVMClassifier()
    features = [Feature1(), Feature2(), Feature3()]

    # Evaluate the accuracy of the model
    a = SkynetDetector(classifier, features)
    a.train(train_file)
    a.evaluate_file(input_file)

    sys.exit(0)

