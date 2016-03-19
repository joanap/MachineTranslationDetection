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
from Features.CountLeastFrequentTrigrams import CountMostFrequentTrigrams
from Features.Util.ProbabilityCalculator import NGramProbability


def arange(x, y, jump=0.1):
  while x <= y:
    yield x
    x += jump


def benchmark(train_dataset, test_dataset, previous_tests_function):
    tagger = POSTagger()
    tagger.train()

    print "Getting ngram for words"
    ngram_words = NGramProbability("./data/output.bigram", "./data/output.trigram")

    print "Getting ngram for categories"
    ngram_categories = NGramProbability("./data/output_category_tags.bigram", "./data/output_category_tags.trigram")

    print "Getting ngram for cats and subcats"
    ngrams_cats_subcats = NGramProbability("./data/output_category_subtype_tags.bigram", "./data/output_category_subtype_tags.trigram")

    bsc = BestStrategiesCalculator()
    previous_tests_function(bsc, tagger, ngram_words, ngram_categories, ngrams_cats_subcats)


    #####################################
    # ADD TESTS BELOW
    #####################################

    available_classifiers = [SVMClassifier(kernel='rbf', gamma=10)]
    available_features = []


    print "Creating threeholds combinations"
    for threeshold in [0.25, 0.5, 0.75]:
        #available_features.append(CountMostFrequentTrigrams(tagger, threeshold, "words", ngram_words))
        available_features.append(CountMostFrequentTrigrams(tagger, threeshold, "categories", ngram_categories))
        #available_features.append(CountMostFrequentTrigrams(tagger, threeshold, "cats_subcats", ngrams_cats_subcats))

    available_features.append(RepeatedWordsCategory(tagger))
    available_features.append(WordCounter())
    available_features.append(StopWordsCounter())
    available_features.append(ConcordanceFeature(tagger, 1))
    available_features.append(ConcordanceFeature(tagger, 2))


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
    train_dataset_path = "./data/train_dataset.txt"
    test_dataset_path = "./data/test_dataset.txt"

    benchmark(train_dataset_path, test_dataset_path, bscpd.add_already_calculated)