invite=['noor','rania','aula']
print(f'welcome my friend,{invite[0]}')
print(f'welcome my old friend,{invite[1]}')
print(f'welcome my cousin,{invite[2]}')
not_available=invite.pop()

 
print(f'{not_available.title()} can not make it ')

invite.append('shahed')
print(f'welcome my friend you made it,{invite[0]}')
print(f'welcome my old friend you made it,{invite[1]}')
print(f'welcome my sister you made it,{invite[2]}')


