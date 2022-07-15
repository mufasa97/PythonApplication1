
names=['mustafa','mohammed','rami']
del names[0]#to delete items and not use it again
names.append('chris')
names.insert(0,'mustafa')

names.insert(1,'noor')
names.remove('chris')#to remove the a specfic item from the list
last_owned=names.pop()#to delete items and  use it again
print(f'the last name is {last_owned.title()}')
print(names)