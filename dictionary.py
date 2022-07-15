

import types
from typing import Type, type_check_only


def intro(dictionary):
    for k,v in dictionary.items():
        print(f'the language is {k} and it is {v}')

languages={}
while True:
    language_name=input('enter the language name: ')
    type1=input('enter the type: ')
    languages[language_name]=type1
    another=input('you want another?(y/n): ')
    if another=='y':
        continue
    else:
        break
intro(languages)
    
    



