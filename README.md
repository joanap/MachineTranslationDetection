# Description
[Unbabel](https://unbabel.com/) challenge: Identify whether a text was written by a human or if it is a product of a machine translation (e.g. google translate)

### Description of the ML features
inser description here

### Recommended reading: 
- [Machine Translation Detection From Monolingual Web-Text](http://www.aclweb.org/anthology/P13-1157)
- [Support Vector Machines (SVM)](http://scikit-learn.org/stable/modules/svm.html)

# Usage

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

Usage examples can be found on:
- `scripts/SkynetDetectorModelAccuracy.py`
- `scripts/SkynetDetectorEvaluateToFile.py`

# Instalation

Dependencies:
* Tested using python 2.7
* Natural Language Toolkit (NLTK) for NLP
* scikit-learn for ML

Download and extract the repository zip.

### Examples

- Evaluate the accuracy of the model:

```sh
python scripts/SkynetDetectorModelAccuracy.py data/train_dataset.txt data/test_dataset.txt
```

- Evaluate a input file:

```sh
python scripts/SkynetDetectorEvaluateToFile.py data/train_dataset.txt data/test_dataset.txt > output.txt
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
