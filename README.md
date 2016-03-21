# Description
[Unbabel](https://unbabel.com/) challenge: Identify whether a text was written by a human or if it is a product of a machine translation (e.g. google translate)

### Description of the ML features
In order to extract information either from training or testing sets, we developed the following features:
- **Length of sentence:** the number of words in a sentence;
- **Number of Stop Words:** the number of stop words in a sentence, which are the ones that do not contain relevant semantic information to the sentence;
- **Number of repeated words per POS:** the number of repeated words per POS in a sentence. We add one feature per available POS tag; We exclude, e.g., nouns and punctuation. In our solution we are using the following tags from a tagger trained with the cess_esp (spanish) corpus: 'a', 'c', 'd', 'i', 'p', 'r', 's', 'v';
- **Concordance between POS:** the number of concordances between gender and number in a sentence using `n` neigbours around a target word. It analyses concordance between verbs, adjectives and personal pronouns. We obtained better results using 1 and 2 neighbour window as two separate features;
- **Number of least frequent trigrams:** the number of words' trigrams in a sentence which the probability to occur is less than a threshold of 0.85.

All the features were normalized by dividing by the length of the sentence.

What we did not have the opportunity to use:
- Use grammar features and identify incorrect bridge between phrases;
- Identify cases where in english makes more sense "him" than "he" which translation is lost in the target language;
- Indentify concordance between other POS categories;

### ML Classifier
With the features above we trained a SVM in order to decide if a sentence is human or machine translated. We used a radial basis funtion
kernel, as suggested by [Arase and Zhou](http://www.aclweb.org/anthology/P13-1157) with a gamma of 10. To accomplish that we used an implementation
of [scikit-learn](http://scikit-learn.org/stable/modules/svm.html#classification).

### Data Partitions
We split a Spanish labelled corpus with 20078 sentences to create a training set with 90% of the sentences and 10% for the testing set.

### Recommended reading: 
- [Machine Translation Detection From Monolingual Web-Text](http://www.aclweb.org/anthology/P13-1157)
- [Support Vector Machines (SVM)](http://scikit-learn.org/stable/modules/svm.html)

# Instalation

Dependencies:
* Tested using python 2.7
* Natural Language Toolkit (NLTK) for NLP
* scikit-learn for ML

Download and extract the repository zip.

# Usage

### Straightfoward python scripts:
- Evaluate the accuracy of the model [SkynetDetectorModelAccuracy.py](https://github.com/joanap/MachineTranslationDetection/blob/master/scripts/SkynetDetectorModelAccuracy.py):

```sh
python scripts/SkynetDetectorModelAccuracy.py data/train_dataset.txt data/test_dataset.txt
```

- Evaluate a input file [SkynetDetectorEvaluateToFile.py](https://github.com/joanap/MachineTranslationDetection/blob/master/scripts/SkynetDetectorEvaluateToFile.py):

```sh
python scripts/SkynetDetectorEvaluateToFile.py data/train_dataset.txt data/test_dataset.txt > output.txt
```

### Advanced Usage

The main class is SkynetDetector receives as arguments a classifier (instance of `ClassifierAbstract` defined in
[Classifiers folder](https://github.com/joanap/MachineTranslationDetection/tree/master/scripts/Classifiers)) and a list 
 features (instances of `FeatureProcessorAbstract` defined in 
[Features folder](https://github.com/joanap/MachineTranslationDetection/tree/master/scripts/Features)).

This class provides the following methods:
- Train the classifier given a input file:

```python
def train(self, file_path)
```
- Evaluate a file and print to the console the result:

```python
def evaluate_file(self, file_path)
```
- Returns the accuracy of the model given a test input file

```python
def accuracy(self, test_file_path)
```
- Returns the most plausible class for a given sentence

```python
def predict(self, sentence, print_to_console=True)
```

# Troubleshooting

### UTF-8 error message

Edit ~/.bash_profile` and reload as following:

```sh
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
source ~/.bash_profile
```

### Matplotlib is building the font cache using fc-list

Rerun with sudo
