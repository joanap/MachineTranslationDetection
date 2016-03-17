# -*- coding: utf-8 -*-

from scripts.BestStrategyCalculatorHelpers.BestStrategyCalculator import Strategy
from scripts.Features.Features import *
from scripts.Classifiers.SVMClassifier import *

def add_already_calculated(bsc, tagger):
    bsc.add_test(SVMClassifier('rbf', 10),Strategy(Feature1(),Feature2()), 0.508964143426)
    bsc.add_test(SVMClassifier('rbf', 10),Strategy(Feature2(),Feature3()), 0.508964143426)
