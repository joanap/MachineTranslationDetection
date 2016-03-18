class DatasetSplitter:
    def __init__(self, line_callback, parse_class=True):
        self._read_line_callback = line_callback
        self._separator = "\t"
        self._parse_class = parse_class

    def split(self, input_file_path):
        with open(input_file_path, 'r+') as training:
            for line in training:
                if line:
                    self.__process_line(line)

    def __process_line(self, line):
        split = line.split(self._separator, 2)

        if len(split) == 2:
            sentence_type = split[0]
            sentence = split[1]

            if isinstance(sentence, str): sentence = sentence.decode("utf-8")

            if self._parse_class:
                sentence_type = int(sentence_type)
                self._read_line_callback(sentence_type, sentence)
            else:
                self._read_line_callback(sentence)
