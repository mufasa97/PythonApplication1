guest_name=input('enter your name please: ')
filename='guest.txt'
with open(filename,'w') as file_object:
    file_object.write(guest_name)

