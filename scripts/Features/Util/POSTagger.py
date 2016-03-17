# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import cess_esp


class POSTagger:
    DEFAULT_TAG = "n"

    ADJECTIVE = "a"

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
        :return: True or False
        """

        number1, gender1 = None, None
        if tag1.startswith('v'):
            number1, gender1 = self.number_from_verb(tag1), self.gender_from_verb(tag1)
        elif tag1.startswith('pp'):
            number1, gender1 = self.number_from_pronom(tag1), self.gender_from_pronom(tag1)
        elif tag1.startswith('a'):
            number1, gender1 = self.number_from_adjective(tag1), self.gender_from_adjective(tag1)
        else:
            return True

        number2, gender2 = None, None
        if tag2.startswith('v'):
            number2, gender2 = self.number_from_verb(tag2), self.gender_from_verb(tag2)
        elif tag2.startswith('pp'):
            number2, gender2 = self.number_from_pronom(tag2), self.gender_from_pronom(tag2)
        elif tag2.startswith('a'):
            number2, gender2 = self.number_from_adjective(tag2), self.gender_from_adjective(tag2)
        else:
            return True

        return number1 == number2 and (gender1 == "i" or gender2 == "i" or gender1 == gender2)

    def number_from_verb(self, tag):
        return tag[5]

    def gender_from_verb(self, tag):
        return tag[2]

    def number_from_pronom(self, tag):
        return tag[4]

    def gender_from_pronom(self, tag):
        return tag[3]

    def number_from_adjective(self, tag):
        return tag[4]

    def gender_from_adjective(self, tag):
        return tag[3]