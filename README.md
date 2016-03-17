# Description
[Unbabel](https://unbabel.com/) challenge: Identify whether a text was written by a human or if it is a product of a machine translation (e.g. google translate)

### Features
inser description here

### Short Description of Structure
The main file is SkynetDetector which is stored on `SkynetDetector` folder.

The class SkynetDetector receives as arguments a classifier (instance of `ClassifierAbstract` which are defined in the
`Classifiers` folder) and a list of used features (instances of `FeatureProcessorAbstract` which are defined in the 
`Features` folder.

SkynetDetector provides the following methods:

```python
def train(self, file_path):
def evaluate_file(self, file_path):
def accuracy(self, test_file_path):
def predict(self, sentence, print_to_console=True):
```

Usage examples can be found on `scripts/SkynetDetectorModelAccuracy.py` and `scripts/SkynetDetectorEvaluateToFile.py`

### Recommended reading: 
- [Machine Translation Detection From Monolingual Web-Text](http://www.aclweb.org/anthology/P13-1157)
- [Support Vector Machines (SVM)](http://scikit-learn.org/stable/modules/svm.html)

# Usage

## Dependencies
* Tested using python 2.7
* Natural Language Toolkit (NLTK) for NLP
* scikit-learn for ML

### Evaluate the accuracy of the model:

```sh
python scripts/SkynetDetectorModelAccuracy.py data/train_dataset.txt data/test_dataset.txt
```

### Evaluate a input file:

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

### Matplotlib is building the font cache using fc-list. This may take a moment Warning

Rerun with sudo