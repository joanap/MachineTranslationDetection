import sys
import codecs
from nltk.corpus import cess_esp

# Counts the number of n grams in a file
def count_n_grams_corpus_unbabel(f, n):
    nGramDict = dict()

    for line in f:
        if isinstance(line, str): line = line.decode("utf-8")
        sentence_splitted = line.split("\t")

        print sentence_splitted[0]
        nGramDict = count_n_grams_line(nGramDict, line.split("\t")[0][0], n)

    return nGramDict

def count_n_grams_corpus(f, n):
    nGramDict = dict()

    sentence = ""
    for tag in f:
        sentence += tag[0][0:2] + " "
    sentence = sentence.strip(" ")

    nGramDict = count_n_grams_line(nGramDict, sentence, n)

    return nGramDict

# Counts the n-grams in a line and puts it in a dict
def count_n_grams_line(nGramDict, line, n):
    sentence = line.strip('\n').lower().split()
    sentence_size = len(sentence)
    for i in range(sentence_size):
        word = sentence[i]

        ngram_key = word
        size = 1
        for j in range(i+1, min(sentence_size, i+n)):
            front_word = sentence[j]
            ngram_key += " " + front_word
            size += 1

        ngram_key = ngram_key.strip(" ")

        if size == n:
            if ngram_key in nGramDict :
                nGramDict[ngram_key] += 1
            else:
                nGramDict[ngram_key] = 1

    return nGramDict

# save to file the n-gram count of nGramDict
def save(output, nGramDict):
    for k, v in sorted(nGramDict.iteritems(), key=lambda (k,v): (-v,k)):
        value = u"{0}\t{1}\n".format(k, v)
        output.write(value)

def simplify_tag(t):
    if "+" in t:
        return t[t.index("+")+1:]
    else:
        return t

def load_from_file():
    with codecs.open(sys.argv[3], "w", "utf-8") as o:
        n = int(sys.argv[2])
        with open(sys.argv[1], "r") as f:
            nGramDict = count_n_grams_corpus_unbabel(f, n)
            save(o, nGramDict)

def load_corpus(corpus):
    with codecs.open(sys.argv[3], "w", "utf-8") as o:
        n = int(sys.argv[2])
        f = [[simplify_tag(t) for (w, t) in sent] for sent in corpus if sent]
        nGramDict = count_n_grams_corpus(f, n)
        save(o, nGramDict)

if __name__ == "__main__":
    #load_from_file()
    load_corpus(cess_esp.tagged_sents())