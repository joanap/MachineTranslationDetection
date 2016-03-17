# Description
[Unbabel](https://unbabel.com/) challenge: Identify whether a text was written by a human or if it is a product of a machine translation (e.g. google translate)

Recommended reading: 
- [Machine Translation Detection From Monolingual Web-Text][http://www.aclweb.org/anthology/P13-1157]

# Usage

## Dependencies
* Tested using python 2.7
* Natural Language Toolkit (NLTK) for NLP
* scikit-learn for ML

### Evaluate the accuracy of the model:
```
> python scripts/SkynetDetectorMain.py data/train_dataset.txt data/test_dataset.txt
```

### Evaluate a input file:
```
> python scripts/SkynetDetectorEvaluateToFile.py data/train_dataset.txt data/test_dataset.txt > output.txt
```

# Troubleshooting

### UTF-8 error message

Edit ~/.bash_profile` and reload as following:

```
> export LC_ALL=en_US.UTF-8
> export LANG=en_US.UTF-8
> source ~/.bash_profile
```

### Matplotlib is building the font cache using fc-list. This may take a moment Warning

Rerun with sudo