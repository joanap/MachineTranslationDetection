from FeatureProcessorAbstract import FeatureProcessor
from Util.POSTagger import *


class ConcordanceFeature(FeatureProcessor):
    def __init__(self):
        FeatureProcessor.__init__(self)
        self._add_arguments_description()

    def process(self, sentence):
        tags = [x[1] for x in tagger.tag_sentence(sentence)]
        #tags = [u'pp1csn00', u'vmip3s0', u'ncfp000', u'sps00', u'pp3fs000', 'n', 'n', u'Fat'] # u"yo publica fotos de ella Crush Hombre !"

        concordance = 0
        not_according = 0
        for i in range(0, len(tags)):
            for j in range(i, len(tags)):
                if i == j:
                    continue

                if tagger.are_in_concordance(tags[i], tags[j]):
                    concordance += 1
                else:
                    not_according += 1

        return concordance, not_according

if __name__ == "__main__":
    tagger = POSTagger()

    f = ConcordanceFeature()
    print f.process(u"yo publica fotos de ella Crush Hombre !")