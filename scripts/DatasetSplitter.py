#!/usr/bin/python
import sys

class DatasetSplitter:
    MT_FILE_NAME = "mt.txt"
    HUMAN_FILE_NAME = "human.txt"

    def split_to_files(self, input_file_path, output_dir):
        try:
            machine_file_path = output_dir + self.MT_FILE_NAME
            human_file_path = output_dir + self.HUMAN_FILE_NAME

            training = open(input_file_path, 'r+')
            machine_output_file = open(machine_file_path, 'w+')
            human_output_file = open(human_file_path, 'w+')

            for line in training:
                if line:
                    if line.startswith('0'):
                        machine_output_file.write(line)
                    elif line.startswith('1'):
                        human_output_file.write(line)
                    else:
                        print 'invalid line for training'
                else:
                    print 'invalid line for training'
        except NameError:
            print 'there is no file to output results'
        except IOError as e:
            print 'cannot open file', e.filename
        finally:
            machine_output_file.close()
            human_output_file.close()


if __name__  == "__main__":
    DEFAULT_INPUT_PATH = "../data/training.txt"
    DEFAULT_OUTPUT_PATH = "../data/"

    input_file_path = DEFAULT_INPUT_PATH
    output_dir = DEFAULT_OUTPUT_PATH
    if len(sys.argv) == 2:
        input_file_path = sys.argv[1]
    elif len(sys.argv) == 3:
        output_dir = sys.argv[2]

    a = SplitDatasets()
    print "Splitting..."
    a.split_to_files(input_file_path, output_dir)
    print "Separated successfully the files"
