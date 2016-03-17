# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import cess_esp


class POSTagger:
    DEFAULT_TAG = 'n'

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

if __name__ == '__main__':
    tagger = POSTagger()
    print tagger.tag_sentence(u"Ella publica fotos de ella Crush Hombre !")
