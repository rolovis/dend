import re

help_file = open('./text/help_text.txt', 'r').readlines()

def help_check(text):
    find = re.search(r'help \w*', text, re.I)
    if find:
        try:
            text_index = help_file.index(text + '\n') + 1
        except ValueError:
            return 'No help available.\n'

        help_string = '\n'
        while text_index < len(help_file) and \
                help_file[text_index] != 'END\n':
            help_string += help_file[text_index]
            text_index += 1
        return help_string

    return 'No help available.\n'

