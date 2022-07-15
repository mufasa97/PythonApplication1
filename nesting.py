#dic inside a list
aliens=[]
#making 30 aliens
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='medium'

#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created 
print(f'Total number of aliens: {len(aliens)}')


#2-list inside dic
# pizza = {'crust': 'thick',
#          'toppings': ['mushrooms','extra cheese'],    }
#print(f"You ordered a {pizza['crust']}-crust pizza "
#    "with the following toppings:")
#for topping in pizza['toppings']:    
#   print("\t" + topping)
