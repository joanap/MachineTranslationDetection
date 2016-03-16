# -*- coding: utf-8 -*-

import hashlib
from SkynetDetector import SkynetDetector

class Strategy:
    """
    Just wraps a array of Feature processors
    """
    def __init__(self, *features):
        self.features = features
        self.description = "Strategy("
        for f in features:
            self.description = self.description + f.description + ","

        # remove last ,
        self.description = self.description.strip(",") + ")"


class BestStrategiesCalculator:
    """
    Test class for different combinations of Features
    """

    def __init__(self):
        self.__strategies = list()
        self.__strategies_map = {}
        self.__sorted_strategies = list()

    def add_test(self, strategy, accuracy=None):
        tp = self._create_tuple(strategy, accuracy)

        key = self.__key(strategy)
        if key not in self.__strategies_map:
            self.__strategies_map[key] = True # place holder
            self.__strategies.append(tp)

    def __key(self, strategy):
        return hashlib.md5(strategy.description)

    def determine_best_strategy(self, input_file, debug=False):
        """
        For every strategy provided in the constructor, determines the program accuracy and stores the information sorted
        in the variable __strategies_map

        """
        result = []

        try:
            for tupl in self.__strategies:
                strategy = tupl[0]
                accuracy = tupl[1]

                if accuracy is None:
                    if debug: print "bsc.add_test(" + strategy.description + ",",

                    skynet_detector = SkynetDetector(strategy.features)
                    skynet_detector.train(input_file)
                    accuracy = skynet_detector.evaluate("Holla gringo!")

                    if debug: print str(accuracy) + ")"

                result.append(self._create_tuple(strategy, accuracy))

        except KeyboardInterrupt:
            print ".... Stopping....."
        finally:
            # sort
            self.__strategies = list(result)
            self.__sorted_strategies = list(result)
            self.__sorted_strategies.sort(key=lambda tup: tup[1], reverse=True)

    def _create_tuple(self, strategy, accuracy):
        return (strategy, accuracy)

    def show_results(self):
        """
        Dump the results sorted by the most accurate strategy to the least accurate
        """

        if len(self.__sorted_strategies) == 0:
            print "Empty list of strategies"
            return

        print "========================================================================"
        print "======================== ACCURACY RESULTS =============================="
        print "="
        for tp in self.__sorted_strategies:
            print "= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ="
            print "= Features=", tp[0].description
            print "= ACCURACY=", str(tp[1]*100), "%"
        print "="
        print "========================================================================"

