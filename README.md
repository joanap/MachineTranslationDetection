# Description
[Unbabel](https://unbabel.com/) challenge: Identify whether a text was written by a human or if it is a product of a machine translation (e.g. google translate)

### Description of the ML features
In order to extract information either from training or testing sets, we select the following features:
- Length of sentence: the number of words in a sentence
- Number of stopwords: the number of stop words in a sentence, which are the ones that do not contain important significance to be used in search queries.
- Number of repeated words: the number of repeated words per category in a sentence. Thus, there are as many features as categories,
since a feature corresponding to a category.
Example of categories: Noun, adjective, preposition.
- Concordance between tags:
- Number of least frequent trigrams: the number of words' trigrams in a sentence which the probability to occur is less than a threshold of 0.75.

We would like to also deal with grammar and identify cases where in (translated in english) makes more sense "him" than 
"he" that still has gender and number accordance but it is not appropriate in the target language.

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
