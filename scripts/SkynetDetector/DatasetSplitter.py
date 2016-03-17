#!/usr/bin/python
# -*- coding: utf-8 -


class DatasetSplitter:
    def __init__(self, line_callback):
        self._read_line_callback = line_callback

    def split(self, input_file_path):
        with open(input_file_path, 'r+') as training:
            for line in training:
                if line:
                    split = line.split("\t", 2)
                    if len(split) != 2: continue

                    sentence_type = int(split[0])
                    sentence = split[1]

                    self._read_line_callback(sentence_type, sentence)