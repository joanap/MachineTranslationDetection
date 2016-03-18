#!/usr/bin/python
# -*- coding: utf-8 -*-

import LanguageModelCreator as n
import os, codecs
import numpy
import sys

class NGramProbability:

    def __init__(self, bigram_path, trigram_path):
         self.bigrams = self._load_n_gram(bigram_path)
         self.trigrams = self._load_n_gram(trigram_path)

    def _load_n_gram(self, path):
        count = dict()
        with codecs.open(path, "r", "utf-8") as f:
            for line in f:
                lst = line.rstrip().split('\t')
                count[lst[0]] = lst[1]

        return count

    def probability(self, sentence):
        sentence_trigrams =  n.countNGramsLine(dict(), sentence, 3).keys()

        result = []
        for trigram in sentence_trigrams:
            aux = trigram.split()[:-1]
            except_last_word = ""
            for s in aux:
                except_last_word += " " + s
            except_last_word = except_last_word.strip(" ")

            if trigram not in self.trigrams or except_last_word not in self.bigrams:
                return 0

            num = numpy.float64(self.trigrams[trigram])
            den = numpy.float64(self.bigrams[except_last_word])

            result.append(num*1.0/den)

        return result

    def probability_smoothed(self, sentence):
        sentence_trigrams =  n.countNGramsLine(dict(), sentence, 3).keys()

        num_bigrams = numpy.float64(len(self.bigrams) + 1)
        result = []
        for trigram in sentence_trigrams:
            aux = trigram.split()[:-1]
            except_last_word = ""
            for s in aux:
                except_last_word += " " + s
            except_last_word = except_last_word.strip(" ")

            num = None
            if trigram not in self.trigrams or except_last_word:
                return 1 / num_bigrams

            num = numpy.float64(self.trigrams[trigram]) + 1
            den = numpy.float64(self.bigrams[except_last_word]) + num_bigrams

            result.append(num*1.0/den)

        return result

def main():
    sentence = sys.argv[1].decode("utf-8").lower()

    n_gram_prob = NGramProbability("./data/output.bigram", "./data/output.trigram")

    probabilities = n_gram_prob.probability(sentence)
    probabilitiesNormalized = n_gram_prob.probability_smoothed(sentence)

    print "Probabilities for sentence: \n\t", sentence.encode("utf-8"), "\n\n"
    print "Probabilities: ", probabilities
    print "Probabilities with smoothing: ", probabilitiesNormalized


if __name__ == "__main__":
    main()