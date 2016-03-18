import sys, traceback
import BestStrategyCalculatorPreviousDevel as bscpd
from BestStrategyCalculatorHelpers.BestStrategyCalculator import BestStrategiesCalculator
from BestStrategyCalculatorHelpers.BestStrategyCalculator import Strategy
from Features.ConcordanceFeature import *
from Features.Util.POSTagger import POSTagger
from Features.WordCounter import WordCounter
from Features.StopWordsCounter import StopWordsCounter
from Features.RepeatedWordsCategory import RepeatedWordsCategory
from Classifiers.SVMClassifier import *
from itertools import permutations

def benchmark(train_dataset, test_dataset, previous_tests_function):
    tagger = POSTagger()
    tagger.train()

    bsc = BestStrategiesCalculator()
    previous_tests_function(bsc, tagger)

    #####################################
    # ADD TESTS BELOW
    #####################################

    available_classifiers = [SVMClassifier(kernel='rbf', gamma=10)]
    available_features = [RepeatedWordsCategory(tagger), WordCounter(), StopWordsCounter(), ConcordanceFeature(tagger, 1), ConcordanceFeature(tagger, 2)]

    for classifier in available_classifiers:
        for i in range(0, len(available_features)+1):
            for subset in permutations(available_features, i):
                if subset != ():
                    bsc.add_test(classifier, Strategy(*subset))

    error_status = 0
    try:
        bsc.determine_best_strategy(train_dataset, test_dataset, debug=True)
    except Exception:
        print "\nXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXX\n"
        traceback.print_exc(file=sys.stdout)
        print "\nXXXXXXXXXXXXXXX\nXXXXXXXXXXXXXXX\n"
        error_status = 1
    finally:
        print ""
        bsc.show_results()

    sys.exit(error_status)

if __name__ == "__main__":
    train_dataset_path = "../data/train_dataset.txt"
    test_dataset_path = "../data/test_dataset.txt"

    benchmark(train_dataset_path, test_dataset_path, bscpd.add_already_calculated)