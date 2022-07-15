#toppings='\nenter the pizza toppings: '
#toppings += '\n(enter quit to exit)'
#while True:
#    pizza=input(toppings)
#    if pizza=='quit':
#        break
#    else:
#        print(f'i have added {pizza} ')

#print('\nyour pizza is ready')   

    
#2-moving items from one lst to another
un_users=['mustafa','mohammed','mohannad']
conf_users=[]
while un_users:

    current_user=un_users.pop()
    print(f'\nverifying user: {current_user.title()}')
    conf_users.append(current_user)

    print('\n\t the following users have been confirmed:')
    for conf_user in conf_users:
        print(conf_user.title())
       
        

