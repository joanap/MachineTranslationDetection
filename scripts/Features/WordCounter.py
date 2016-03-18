from FeatureProcessorAbstract import FeatureProcessor

class WordCounter(FeatureProcessor):
    def __init__(self):
        FeatureProcessor.__init__(self)

    def process(self, sentence):
        words = sentence.split()
        return len(words)