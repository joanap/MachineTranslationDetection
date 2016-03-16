from FeatureProcessor import FeatureProcessor


class Feature1(FeatureProcessor):
    def __init__(self):
        FeatureProcessor.__init__(self)
        self._add_arguments_description("arg1", "arg2")

    def process(self, sentence):
        return 0.1


class Feature2(FeatureProcessor):
    def __init__(self):
        FeatureProcessor.__init__(self)

    def process(self, sentence):
        return 0.2


class Feature3(FeatureProcessor):
    def __init__(self):
        FeatureProcessor.__init__(self)

    def process(self, sentence):
        return 0.3