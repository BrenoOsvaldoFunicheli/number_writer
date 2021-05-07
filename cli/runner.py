import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i","--input_file", type=str, help="input_file to get numbers to transform in text")
parser.add_argument("-o","--output_file", type=str, help="output file to send transformed texts")

parser.add_argument("-l","--language", type=str, help="specify the language of write number", default='pt')

args = parser.parse_args()
