# -*- coding: utf-8 -*-

import sys
import traceback

import BestStrategyCalculatorPreviousDevel
from BestStrategyCalculator import BestStrategiesCalculator
from BestStrategyCalculator import Strategy
from POSTagger import POSTagger
from Features.Features import *


def arange(x, y, jump=0.1):
  while x <= y:
    yield x
    x += jump


def benchmark(data_set_file_path, previous_tests_function):
    tagger = POSTagger()
    tagger.train()

    bsc = BestStrategiesCalculator()
    previous_tests_function(bsc, tagger)

    #####################################
    # ADD TESTS BELOW
    #####################################

    bsc.add_test(Strategy(Feature2(), Feature3()))

    try:
        bsc.determine_best_strategy(data_set_file_path, debug=True)
    except Exception:
        print "\nXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXX\n"
        traceback.print_exc(file=sys.stdout)
        print "\nXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXX\n"
    finally:
        print ""
        bsc.show_results()


if __name__ == "__main__":
    data_set_file_path = "../data/training.txt"
    benchmark(data_set_file_path, BestStrategyCalculatorPreviousDevel.add_already_calculated)