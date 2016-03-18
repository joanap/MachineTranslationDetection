from FeatureProcessorAbstract import FeatureProcessor
import nltk


class StopWordsCounter(FeatureProcessor):
    def __init__(self):
        FeatureProcessor.__init__(self)

    def process(self, sentence):
        return self.count_stop_words(sentence)

    def count_stop_words(self, sentence, list_words_to_remove = nltk.corpus.stopwords.words('spanish')):
        """
        Remove stop words of a sentence
        :param sentence:
        :param list_words_to_remove: default is the list from nltk corpus for portuguese language.
        :return: sentence with the stop words removed
        """
        number_stop_words = 0
        for word in sentence.split():
            if word in list_words_to_remove:
                number_stop_words += 1
        return number_stop_words