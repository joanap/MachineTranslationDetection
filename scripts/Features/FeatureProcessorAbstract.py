import abc


class FeatureProcessor(object):
    """
    Abstract class for defining feature extraction
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        # adds the usual className()
        self._add_arguments_description()

    def _add_arguments_description(self, *args):
        """
        Changes self.description field with format <className(arg1, arg2,...,argn)>
        :param args: list of arguments
        """
        self.description = self.__class__.__name__ + "("
        for i in range(0, len(args)):
            self.description += str(args[i])
            if i != len(args) - 1:
                self.description += ", "

        self.description += ")"

    @abc.abstractmethod
    def process(self, sentence, len_sentence):
        """
        Return feature value as float
        :param sentence:
        :return: feature value float
        """
        return
