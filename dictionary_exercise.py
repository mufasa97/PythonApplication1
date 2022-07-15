#1-
#friend={'first_name':'mustafa','last_name':'watheq','age':24,'city':'amman'}
#print(f"name is: {friend['first_name']} {friend['last_name']}")
#print(f"age is: {friend['age']}, city is: {friend['city']}")

#2-
#rivers={'nile':'eygpt','amazon':'peru','tigirs':'turkey'}
#for river in rivers.keys():
#    country=rivers[river].title()
#    print(f'the {river} runs through {country}')
#print('\n')
#for river_only in rivers.keys():
#    print(f'the rivers are: {river_only}')
#print('\n')
#for country_only in rivers.values():
#    print(f'the countries are: {country_only}')

#3-
fav_language={'jen':'python','sarah':'c','edward':'ruby','phil':'python'}
poll_list=['phil','jen','alex']
for person in poll_list:
    if person in fav_language:
        print(f'thank you {person}, for participating in the poll')
    else:
        print(f'please go take the poll {person}')