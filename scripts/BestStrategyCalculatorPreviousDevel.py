from Classifiers.SVMClassifier import SVMClassifier
from BestStrategyCalculator import Strategy
from Features.ConcordanceFeature import ConcordanceFeature
from Features.RepeatedWordsCategory import RepeatedWordsCategory
from Features.StopWordsCounter import StopWordsCounter
from Features.WordCounter import WordCounter

#bsc.add_test(SVMClassifier('rbf', 10),Strategy(RepeatedWordsCategory(tagger)), 0.527888446215) - sem normalizar


def add_already_calculated(bsc, tagger):
    bsc.add_test(SVMClassifier('rbf', 10),Strategy(RepeatedWordsCategory(tagger)), 0.506972111554)
    bsc.add_test(SVMClassifier('rbf', 10),Strategy(WordCounter()), 0.493525896414)
    bsc.add_test(SVMClassifier('rbf', 10),Strategy(StopWordsCounter()), 0.487549800797)
    bsc.add_test(SVMClassifier('rbf', 10),Strategy(ConcordanceFeature(tagger, 1)), 0.488545816733)
