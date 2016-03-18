from FeatureProcessorAbstract import FeatureProcessor
from Util.POSTagger import POSTagger
import nltk




class WordCounter(FeatureProcessor):
    def __init__(self):
        FeatureProcessor.__init__(self)

    def process(self, sentence):
        words = sentence.split()
        return len(words)

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

if __name__ == "__main__":
    sentence = "Esperamos que se llegues a celebrar volviendo a Walt Disney World de nuevo !"
    sentenceLower = sentence.lower()
    tagger = POSTagger()

    f3 = RepeatedSurfaceCounter(tagger)
    tagged = [('esperamos', u'vmip1p0'), ('que', u'cs'), ('se', u'p0000000'), ('llegues', 'n'), ('se', u'p0000000'), ('a', u'sps00'), ('celebrar', u'vmn0000'), ('volviendo', u'vmg0000'), ('a', u'sps00'), ('walt', 'n'), ('disney', 'n'), ('world', 'n'), ('de', u'sps00'), ('que', u'cs'), ('nuevo', u'aq0ms0'), ('!', u'Fat')]

    grouped = f3.process(sentence)
    print grouped
