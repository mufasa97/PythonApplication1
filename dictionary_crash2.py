
#looping through a dic and printing the key values that we want

fav_languages={'jen':'python','sarah':'c','edward':'ruby','phil':'python'}
friends=['phil','sarah']
for name in fav_languages.keys():
    print(name.title())
    if name in friends:
        language=fav_languages[name].title()
        print(f"\t{name.title()}, i see you love {language}")
#to loop through the dic in a particular order
#use
# for name in sorted(fav_languages.keys()):
    #print(f"{name.title()},thank you for taking the poll")    



