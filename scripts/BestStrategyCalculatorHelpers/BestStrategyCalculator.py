from scripts.SkynetDetector.SkynetDetector import SkynetDetector


class Strategy:
    """
    Just wraps a array of Feature processors
    """
    def __init__(self, *features):
        self.features = sorted(features, key=lambda feature: feature.description)

        self.description = "Strategy("
        for f in self.features:
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

    def add_test(self, classifier, strategy, accuracy=None):
        tp = self._create_tuple(classifier, strategy, accuracy)

        key = self.__key(classifier, strategy)
        if key not in self.__strategies_map:
            self.__strategies_map[key] = True # place holder
            self.__strategies.append(tp)

    def __key(self, classifier, strategy):
        # we can do a md5 hash here...
        return classifier.description + "-" + strategy.description

    def determine_best_strategy(self, input_file, test_file, debug=False):
        """
        For every strategy provided in the constructor, determines the program accuracy and stores the information sorted
        in the variable __strategies_map

        """
        result = []

        try:
            for tupl in self.__strategies:
                classifier = tupl[0]
                strategy = tupl[1]
                accuracy = tupl[2]

                if accuracy is None:
                    if debug: print "bsc.add_test(" + classifier.description + "," + strategy.description + ",",

                    skynet_detector = SkynetDetector(classifier, strategy.features)
                    skynet_detector.train(input_file)
                    accuracy = skynet_detector.accuracy(test_file_path=test_file)

                    if debug: print str(accuracy) + ")"

                result.append(self._create_tuple(classifier, strategy, accuracy))

        except KeyboardInterrupt:
            print ".... Stopping....."
        finally:
            # sort
            self.__strategies = list(result)
            self.__sorted_strategies = list(result)
            self.__sorted_strategies.sort(key=lambda tup: tup[2], reverse=True)

    def _create_tuple(self, classifier, strategy, accuracy):
        return (classifier, strategy, accuracy)

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
            print "= Classifier", tp[0].description
            print "= Features=", tp[1].description
            print "= ACCURACY=", str(tp[2]*100), "%"
        print "="
        print "========================================================================"

