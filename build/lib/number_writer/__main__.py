from rules import languages
from cli import args
from core import Processor, FileHandler

# get enviroment args
language = args.language
input_file = args.input_file
output_file = args.output_file

# check if there is some text
if not input_file or not output_file:
    raise Exception("You need pass input and output files")

# get rules to process text
language_rules = languages.get(language)

p = Processor(language_rules)

ext = [p.get_writted_number(number) for number in FileHandler.read_input("input.txt")]
    
FileHandler.write_output(ext)

print('successfully write !!!')
