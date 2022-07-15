
#using the sort method 

list=['japan','korea','germany','australia','france']
print(list)
print(f'\nsorted list is {sorted(list)}')
print(f'\nthe original list is {list}')
print(f'\nthe reverse sorted list is {sorted(list,reverse=True)}')
print(f'\n the list is still the same {list}')
list.reverse()
print(f'\nthe list is now reversed {list}')
list.reverse()
print(f'\nthe list is now back to original {list}')
list.sort()
print(f'\nthe list is now in alphabetical order {list}')
list.sort(reverse=True)
print(f'\nthe list is now in reverse alphabetical order {list}')

print(f'\n the length is {len(list)}')


