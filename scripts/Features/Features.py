from FeatureProcessorAbstract import FeatureProcessor
from Util.POSTagger import POSTagger
import nltk
from collections import Counter


class RepeatedSurfaceCounter(FeatureProcessor):
    def __init__(self, tagger):
        FeatureProcessor.__init__(self)
        self._add_arguments_description(str(tagger))
        self._tagger = tagger

    def process(self, sentence):
        category_map = self.group_words_by_category(sentence)
        self.repeated_surface(category_map)


    def count_repeated_words(self, category_map, category=None):

        if category is None:
            count = 0
            for cat in category_map:
                count += self._count_repeated_words_simple(category_map[cat])
            return count
        else:
            words = category_map[category] # or surfaces
            if words is not None:
                return self._count_repeated_words_simple(words)

        return 0

    def _count_repeated_words_simple(self, words):
        return len(words) - len(set(words))


    def group_words_by_category(self, sentence, pos_tags = None):
        category_map  = {}
        if pos_tags is None:
            pos_tags = tagger.tag_sentence(sentence)

        for pos_tag in pos_tags:
            surface = pos_tag[0]
            tag = pos_tag[1][0]
            if tag in category_map:
                category_map[tag] += [surface]
            else:
                category_map[tag] = [surface]
        return category_map


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
    sentence = "Esperamos que se llegues a celebrar volviendo a Walt Disney World de que nuevo !"
    sentenceLower = sentence.lower();
    tagger = POSTagger()
    #f = WordCounter()
    #f.process(sentenceLower)
    #f1 = StopWordsCounter()
    #f1.process(sentenceLower)
    f3 = RepeatedSurfaceCounter(tagger)
    tagged = [('esperamos', u'vmip1p0'), ('que', u'cs'), ('se', u'p0000000'), ('llegues', 'n'), ('se', u'p0000000'), ('a', u'sps00'), ('celebrar', u'vmn0000'), ('volviendo', u'vmg0000'), ('a', u'sps00'), ('walt', 'n'), ('disney', 'n'), ('world', 'n'), ('de', u'sps00'), ('que', u'cs'), ('nuevo', u'aq0ms0'), ('!', u'Fat')]

    grouped = f3.group_words_by_category(sentence, pos_tags=tagged)
    res = f3.count_repeated_words(grouped)
    print grouped
    print res