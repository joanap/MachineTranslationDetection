from DatasetSplitter import *
from Stats import *


class SkynetDetector:
    def __init__(self, classifier, features_processors):
        self._features = features_processors
        self._data_classes = []
        self._features_data = []
        self.stats = None
        self.classifier = classifier

    def train(self, file_path):
        splitter = DatasetSplitter(line_callback=self._process_sentence)
        splitter.split(file_path)

        # provide data to train svm
        self.classifier.train(self._features_data, self._data_classes)

    def evaluate_file(self, file_path):
        splitter = DatasetSplitter(line_callback=self.predict, parse_class=False)
        splitter.split(file_path)

    def predict(self, sentence, print_to_console=True):
        feature_vector = self._process_features(sentence.lower())
        prediction = self.classifier.predict([feature_vector])[0]

        if print_to_console:
            print str(prediction) + "\t" + sentence.strip("\n")

        return prediction

    def accuracy(self, test_file_path):
        self.stats = Stats()

        splitter = DatasetSplitter(line_callback=self._evaluate)
        splitter.split(test_file_path)

        #check http://stats.stackexchange.com/questions/92101/prediction-with-scikit-and-an-precomputed-kernel-svm
        return self.stats.accuracy()

    def _process_sentence(self, class_sentence, sentence):
        self._data_classes.append(class_sentence)
        feature_vector = self._process_features(sentence)
        self._features_data.append(feature_vector)

    def _process_features(self, sentence):
        feature_vector = []
        for feature in self._features:
            len_sentence = len(sentence.split(" "))
            value = feature.process(sentence, len_sentence)

            if isinstance(value, list):
                feature_vector.extend(value)
            else:
                feature_vector.append(value)

        return feature_vector

    def _evaluate(self, expected_class_sentence, sentence):
        predicted_class = self.predict(sentence, print_to_console=False)
        self.stats.add(expected_class_sentence, predicted_class)