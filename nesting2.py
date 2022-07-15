
fav_lang={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
    }
for name,languages in fav_lang.items():
    if len(languages)>1:

        print(f"\n{name.title()}'s favorite langauage are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite langauage is:\n\t {languages[0].title()}")
        