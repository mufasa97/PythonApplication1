while True:
    name=input('enter you name : ')
    print(f'hello {name},we are glad to have you here')
    with open('guest_book.txt','a') as file_object:
        file_object.write(f'\n{name.rstrip()} arrived at the party')
    another=input('did another guest arrive? (y/n): ')
    if another=='y':
        continue
    else:
        break
print('all the guests have arrived')



    
