from FeatureProcessorAbstract import FeatureProcessor
from Util.POSTagger import *


class ConcordanceFeature(FeatureProcessor):
    def __init__(self, tagger, neighbors_window):
        """
        :param neighbors_window: int
        :return:
        """
        FeatureProcessor.__init__(self)
        self._add_arguments_description("tagger", neighbors_window)

        self._tagger = tagger
        self.neighbors_window = neighbors_window

    def process(self, sentence):
        tags = [x[1] for x in self._tagger.tag_sentence(sentence)]

        concordance = 0
        not_according = 0

        tags_len = len(tags)
        for i in range(0, len(tags)):
            for j in range(i+1, min(tags_len, i+self.neighbors_window+1)):
                if self._tagger.are_in_concordance(tags[i], tags[j]):
                    concordance += 1
                else:
                    not_according += 1

        return [concordance, not_according]



if __name__ == "__main__":
    tagger = POSTagger()

    #tags = [u'pp1csn00', u'vmip3s0', u'ncfp000', u'sps00', u'pp3fs000', 'n', 'n', u'Fat'] # u"yo publica fotos de ella Crush Hombre !"
    #tags = ["a", "b", "c", "d", "e", "f", "g", "h"]

    f = ConcordanceFeature(tagger, 1)
    print f.process(u"yo publica fotos de ella Crush Hombre !")
