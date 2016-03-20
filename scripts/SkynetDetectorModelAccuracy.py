# -*- coding: utf-8 -*-

import sys
from SkynetDetector.SkynetDetector import SkynetDetector
from Classifiers.SVMClassifier import *
from Features.WordCounter import WordCounter
from Features.CountLeastFrequentTrigrams import CountMostFrequentTrigrams
from Features.RepeatedWordsCategory import RepeatedWordsCategory
from Features.Util.POSTagger import POSTagger
from Features.Util.ProbabilityCalculator import NGramProbability
from Features.StopWordsCounter import *
from Features.ConcordanceFeature import *
from Features.WordCounter import *

if __name__ == "__main__":
    train_file, test_file = None, None
    if len(sys.argv) == 2:
        train_file = sys.argv[1]
    elif len(sys.argv) == 3:
        train_file, test_file = sys.argv[1], sys.argv[2]
    else:
        print "Usage", __name__, "<train_file_dir>", "<test_file_dir"
        sys.exit(1)

    tagger = POSTagger()
    tagger.train()

    print "Getting ngram for words"
    ngram_words = NGramProbability("./data/output.bigram", "./data/output.trigram")

    print "Getting ngram for categories"
    ngram_categories = NGramProbability("./data/output_category_tags.bigram", "./data/output_category_tags.trigram")


    # best features
    classifier = SVMClassifier()

    # 0.626494023904
    features = [WordCounter(), CountMostFrequentTrigrams(tagger, 0.85, 'words', ngram_words), RepeatedWordsCategory(tagger, [u'a', u'c', u'd', u'i', u'n', u'p', u's', u'r', u'v'])]

    #0.627490039841
    features = [CountMostFrequentTrigrams(tagger, 0.8, 'words', ngram_words),RepeatedWordsCategory(tagger, [u'a', u'c', u'd', u'i', u'p', u'r', u's', u'v'])]

    #0.629980079681
    features = [ConcordanceFeature(tagger, 1), CountMostFrequentTrigrams(tagger, 0.85, 'words', ngram_words),StopWordsCounter()]

    #0.630976095618
    features = [ConcordanceFeature(tagger, 1),ConcordanceFeature(tagger, 2), CountMostFrequentTrigrams(tagger, 0.85, 'words', ngram_words),StopWordsCounter()]

    #0.63296812749 -> Melhor
    features = [ConcordanceFeature(tagger, 1),ConcordanceFeature(tagger, 2), CountMostFrequentTrigrams(tagger, 0.85, 'words', ngram_words),RepeatedWordsCategory(tagger, [u'a', u'c', u'd', u'i', u'p', u'r', u's', u'v']), StopWordsCounter()]

    # Evaluate the accuracy of the model
    a = SkynetDetector(classifier, features)
    print "Training..."
    a.train(train_file)

    print "Testing..."
    accuracy = a.accuracy(test_file)
    print accuracy

    sys.exit(0)