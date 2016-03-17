# -*- coding: utf-8 -*-

import sys, traceback

import BestStrategyCalculatorPreviousDevel as bscpd
from BestStrategyCalculatorHelpers.BestStrategyCalculator import BestStrategiesCalculator
from BestStrategyCalculatorHelpers.BestStrategyCalculator import Strategy
from Features.Features import *
from Features.Util.POSTagger import POSTagger
from Classifiers.SVMClassifier import *

def arange(x, y, jump=0.1):
  while x <= y:
    yield x
    x += jump


def benchmark(train_dataset, test_dataset, previous_tests_function):
    tagger = POSTagger()
    tagger.train()

    bsc = BestStrategiesCalculator()
    previous_tests_function(bsc, tagger)

    #####################################
    # ADD TESTS BELOW
    #####################################

    bsc.add_test(SVMClassifier(), Strategy(Feature2(), Feature3()))

    try:
        bsc.determine_best_strategy(train_dataset, test_dataset, debug=True)
    except Exception:
        print "\nXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXX\n"
        traceback.print_exc(file=sys.stdout)
        print "\nXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXX\n"
    finally:
        print ""
        bsc.show_results()


if __name__ == "__main__":
    train_dataset_path = "../data/train_dataset.txt"
    test_dataset_path = "../data/test_dataset.txt"

    benchmark(train_dataset_path, test_dataset_path, bscpd.add_already_calculated)