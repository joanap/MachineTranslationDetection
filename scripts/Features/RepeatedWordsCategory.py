from FeatureProcessorAbstract import FeatureProcessor
from Util.POSTagger import POSTagger


class RepeatedWordsCategory(FeatureProcessor):
    def __init__(self, tagger, categories = None):
        FeatureProcessor.__init__(self)

        if categories is None:
            categories = [u'a', u'c', u'I', u'd', u'F', u'i', u'n', u'p', u's', u'r', u'W', u'v', u'Y', u'X', u'Z']

        self._add_arguments_description("tagger", categories)
        self.categories = categories
        self._tagger = tagger

    def process(self, sentence, len_sentence):
        category_map = self.group_words_by_category(sentence)

        res = []
        for cat in category_map:
            res.append(self.count_repeated_words(category_map, cat)*1.0/len_sentence)

        return res

    def count_repeated_words(self, category_map, category=None):
        if category in category_map:
            words = category_map[category]  # or surfaces
            return self._count_repeated_words_simple(words)

        return 0

    def _count_repeated_words_simple(self, words):
        return len(words) - len(set(words))

    def group_words_by_category(self, sentence):
        category_map = dict((el, []) for el in self.categories)
        pos_tags = self._tagger.tag_sentence(sentence)

        for pos_tag in pos_tags:
            surface = pos_tag[0]
            tag = pos_tag[1][0]

            if tag in category_map:
                category_map[tag].append(surface)

        return category_map


if __name__ == "__main__":
    sentence = "Esperamos que se llegues a celebrar volviendo a Walt Disney World de nuevo !"
    sentenceLower = sentence.lower()

    tagger = POSTagger()
    f3 = RepeatedWordsCategory(tagger)
    tagged = [('esperamos', u'vmip1p0'), ('que', u'cs'), ('se', u'p0000000'), ('llegues', 'n'), ('se', u'p0000000'),
              ('a', u'sps00'), ('celebrar', u'vmn0000'), ('volviendo', u'vmg0000'), ('a', u'sps00'), ('walt', 'n'),
              ('disney', 'n'), ('world', 'n'), ('de', u'sps00'), ('que', u'cs'), ('nuevo', u'aq0ms0'), ('!', u'Fat')]

    grouped = f3.process(sentence)
    print grouped
