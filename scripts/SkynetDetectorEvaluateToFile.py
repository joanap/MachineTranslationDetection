import sys
from SkynetDetector.SkynetDetector import SkynetDetector
from Classifiers.SVMClassifier import *
from Features.CountLeastFrequentTrigrams import *
from Features.ConcordanceFeature import *
from Features.RepeatedWordsCategory import *
from Features.StopWordsCounter import *
from Features.Util.POSTagger import POSTagger


if __name__ == "__main__":
    input_file = "./data/test_blind.txt"
    train_file = "./data/train_dataset.txt"

    if len(sys.argv) == 2:
        input_file = sys.argv[1]
    elif len(sys.argv) == 3:
        input_file, train_file = sys.argv[1], sys.argv[2]

    ngram_words = NGramProbability("./data/output.bigram", "./data/output.trigram")

    tagger = POSTagger()
    tagger.train()

    # best features
    classifier = SVMClassifier()
    features = [ConcordanceFeature(tagger, 1), ConcordanceFeature(tagger, 2), CountMostFrequentTrigrams(tagger, 0.85, 'words', ngram_words), RepeatedWordsCategory(tagger, [u'a', u'c', u'd', u'i', u'p', u'r', u's', u'v']), StopWordsCounter()]

    # Evaluate the accuracy of the model
    a = SkynetDetector(classifier, features)
    a.train(train_file)
    a.evaluate_file(input_file)

    sys.exit(0)
