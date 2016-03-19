# -*- coding: utf-8 -*-

from FeatureProcessorAbstract import FeatureProcessor
from Util.POSTagger import *
from Util.ProbabilityCalculator import NGramProbability

class CountMostFrequentTrigrams(FeatureProcessor):
    def __init__(self, tagger, threeshold, type, ngram):
        FeatureProcessor.__init__(self)
        self.threeshold = threeshold
        self._tagger = tagger
        self.ngram_prob = ngram

        if type == "words":
            if ngram is None:
                print "Allocating space for words ngrams"
                self.ngram_prob = NGramProbability("./data/output.bigram", "./data/output.trigram")

            self._add_arguments_description("tagger", threeshold, "'" + type + "'", r"ngram_words")
            self._pre_process = self._filter_words
        elif type == "categories":
            if ngram is None:
                print "Allocating space for categories ngrams"
                self.ngram_prob = NGramProbability("./data/output_category_tags.bigram", "./data/output_category_tags.trigram")

            self._add_arguments_description("tagger", threeshold, "'" + type + "'", r"ngram_categories")
            self._pre_process = self._filter_category
        elif type == "tags":
            if ngram is None:
                print "Allocating space for tags ngrams"
                self.ngram_prob = NGramProbability("./data/output_tags.bigram", "./data/output_tags.trigram")

            self._add_arguments_description("tagger", threeshold, "'" + type + "'", r"ngram_words")
            self._pre_process = self._filter_tags
        elif type == "cats_subcats":
            if ngram is None:
                print "Allocating space for words cats_subcats"
                self.ngram_prob = NGramProbability("./data/output_category_subtype_tags.bigram", "./data/output_category_subtype_tags.trigram")

            self._add_arguments_description("tagger", threeshold, "'" + type + "'", r"ngram_cats_subcats")
            self._pre_process = self._filter_cat_subcasts


    def _filter_category(self, sentence):
        pos_tags = self._tagger.tag_sentence(sentence)
        result = ""
        for pos_tag in pos_tags:
            tag = pos_tag[1][0]
            result += tag + " "

        return result.strip(" ")


    def _filter_cat_subcasts(self, sentence):
        pos_tags = self._tagger.tag_sentence(sentence)
        result = ""
        for pos_tag in pos_tags:
            tag = pos_tag[1][0:2]
            result += tag + " "

        return result.strip(" ")

    def _filter_tags(self, sentence):
        pos_tags = self._tagger.tag_sentence(sentence)
        result = ""
        for pos_tag in pos_tags:

            tag = pos_tag[1]
            result += tag + " "

        return result.strip(" ")

    def _filter_words(self, sentence):
        return sentence

    def process(self, sentence, len_sentence):
        sentence = self._pre_process(sentence)
        probs = self.ngram_prob.probability(sentence)

        count = 0
        for prob in probs:
            if prob > self.threeshold:
                count += 1

        return count*1.0/len_sentence

if __name__ == "__main__":
    tagger = POSTagger()
    tagger.train()

    clft = CountMostFrequentTrigrams(tagger, 0.2, "words")
    clft2 = CountMostFrequentTrigrams(tagger, 0.2, "categories")
    clft3 = CountMostFrequentTrigrams(tagger, 0.2, "tags")
    clft4 = CountMostFrequentTrigrams(tagger, 0.2, "cats_subcats")

    human = u"Los proveedores de salud a menudo no sabían que decirme ." # 1
    robot = u"Echa un vistazo a quién más en Hollywood tiene un gran vacío en sus dientes !" # 0

    print clft.process(human, len(human.split(" ")))
    print clft.process(robot, len(robot.split(" ")))

    print clft2.process(human, len(human.split(" ")))
    print clft2.process(robot, len(robot.split(" ")))

    print clft3.process(human, len(human.split(" ")))
    print clft3.process(robot, len(robot.split(" ")))

    print clft4.process(human, len(human.split(" ")))
    print clft4.process(robot, len(robot.split(" ")))
