# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import cess_esp


class POSTagger:
    DEFAULT_TAG = "n"

    ARTICLE = "d"
    INDEFINITE_ARTICLE = "i" # second letter
    DEFINITE_ARTICLE = "a" # second letter

    PROPOSITIONS = "s"


    def __init__(self, tsents=cess_esp.tagged_sents()):
        """
        :param tsents: list of annotated sententeces
        """
        self.__corpus = tsents
        self.__is_trained = False
        self.__tagger = None

    def train(self):
        """
        Train the tagger
        """
        print "Training corpus ..."
        tsents = [[(w.lower(), self._simplify_tag(t)) for (w, t) in sent] for sent in self.__corpus if sent]
        train = tsents[:]

        tagger0 = nltk.DefaultTagger(self.DEFAULT_TAG)
        tagger1 = nltk.UnigramTagger(train, backoff=tagger0)
        self.__tagger = nltk.BigramTagger(train, backoff=tagger1)

        self.__is_trained = True
        print "Training complete!"

    def tag_sentence(self, sentence):
        """
        Tag the sentence given by argument

        :param sentence:
        """
        if not self.__is_trained:
            self.train()

        return self.__tagger.tag(nltk.word_tokenize(sentence))

    def _simplify_tag(self, t):
        if "+" in t:
            return t[t.index("+")+1:]
        else:
            return t

    def construct_sentence(self, list_pairs_token_tag):
        """
        Given a list of tokenized sentence, reconstruct the sentence
        :param list_pairs_token_tag:
        :return:
        """
        result = ""
        for el in list_pairs_token_tag:
            result += el[0] + " "
        return result

    def get_tag(self, word):
        """
        Returns the tag of the tuple
        :param word:
        :return: the tag
        """
        return word[1]

    def get_category(self, tag):
        return tag[0]

    def is_pronoun(self, tag):
        return self.get_category(tag)

    def are_in_concordance(self, tag1, tag2):
        """
        When applicable. Following http://www.ilc.cnr.it/EAGLES96/annotate/node17.html
        :param tag1:
        :param tag2:
        :return: True False or None (if not applicable)
        """

        #[('\xc3\xa9l', 'n'), ('gusta', u'vmip3s0')]
        #[('ellas', u'pp3fp000'), ('gustan', u'vmip3p0')]
        #[('ella', u'pp3fs000'), ('gusta', u'vmip3s0')]
        #[('ellos', u'pp3mp000'), ('gustan', u'vmip3p0')]
        #[('ellos', u'pp3mp000'), ('gustan', u'vmip3p0')]

        if tag1.startswith('n') or tag2.startswith('n'):
            return True
        if tag1.startswith('v') and tag2.startswith("pp"):
            number1, gender1 = self.number_from_verb(tag1), self.gender_from_verb(tag1)
            number2, gender2 = self.number_from_pronom(tag2), self.gender_from_pronom(tag2)

            # indefinite gender
            return number1 == number2 and gender1 == "i" or gender2 == "i" or gender1 == gender2
        else:
            return True

    def number_from_verb(self, tag):
        return tag[5]

    def gender_from_verb(self, tag):
        return tag[2]

    def number_from_pronom(self, tag):
        return tag[4]

    def gender_from_pronom(self, tag):
        return tag[3]


if __name__ == '__main__':
    tagger = POSTagger()



    print tagger.are_in_concordance(u'vmip3p0', u'pp3mp000')
    #yo         p | p | 1 | c | s | n
    #ella       p | p | 3 | f | s | 0
    #tú         p | p | 2 | c | s | n
    #ellas      p | p | 3 | f | p | 0
    #nosotros   p | p | 1 | m | p | 0
    #nosotras  nada
    #usted      p | p | 2 | c | s | 0

    # tipo | subtipo | pessoa | género | número | ?


    #guapa      a | q | 0 | f | s | 0

    #[('el', u'da0ms0'), ('la', u'da0fs0'), ('los', u'da0mp0'), ('las', u'da0fp0')]
    #[('un', u'di0ms0'), ('una', u'di0fs0'), ('unos', u'di0mp0'), ('unas', u'di0fp0')]

    #propositions
    #[('a', u'sps00'), ('con', u'sps00'), ('de', u'sps00'), ('por', u'sps00'), ('para', u'sps00')]


    #print tagger.tag_sentence("él gusta")
    #print tagger.tag_sentence("ellas gustan")
    #print tagger.tag_sentence("ella gusta")

    #print tagger.tag_sentence("ellos gustan")

    #print tagger.tag_sentence(u"yo publica fotos de ella Crush Hombre !")

