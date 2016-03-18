import sys
import codecs

# Counts the number of n grams in a file
def countNGrams(f, n):
    nGramDict = dict()

    for line in f:
        if isinstance(line, str): line = line.decode("utf-8")
        nGramDict = countNGramsLine(nGramDict,line.split("\t")[1], n)

    return nGramDict

# Counts the n-grams in a line and puts it in a dict
def countNGramsLine(nGramDict, line, n):
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

def main():
    with open(sys.argv[1], "r") as f:
        n = int(sys.argv[2])
        with codecs.open(sys.argv[3], "w", "utf-8") as o:
            nGramDict = countNGrams(f, n)
            save(o, nGramDict)

if __name__ == "__main__":
    main()