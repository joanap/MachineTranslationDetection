from FeatureProcessorAbstract import FeatureProcessor
from Util.POSTagger import *
from Util.ProbabilityCalculator import NGramProbability


class CountLeastFrequentTrigrams(FeatureProcessor):
    def __init__(self, tagger, threeshold):
            FeatureProcessor.__init__(self)
            self._add_arguments_description("tagger", threeshold)
            self.NGramProbability("./data/output.bigram", "./data/output.trigram")
            self.threeshold = threeshold
            self._tagger = tagger

    def process(self, sentence):
        probs = self.NGramProbability.probability(sentence)

        count = 0
        for prob in probs:
            if prob < self.threeshold:
                count += 1

        return count