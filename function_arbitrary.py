#1- making unlimted attribute for toppings
#def make_pizza(size,*toppings):
#    print(f'\n making a {size}-inch pizza with following toppings')
#    for topping in toppings:
#        print(f'-{topping}')

#make_pizza(16,'pepperoni')
#make_pizza(13,'mushroom','cheese','onion')

#2-making a unlimted dictionary from from a function

def build_profile(first,last,**user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

user_profile=build_profile('mustafa','watheq',
                           location='amman',
                           field='engineering')
print(user_profile)