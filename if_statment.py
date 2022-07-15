
#course exercise (Alien's colors)
#1-alien_color='green'
#if alien_color=='red':
#    print('player earned 5 points')
#else:
#    print('the player earned 10 points')

#2-favorite fruit

#fruits=['orange','apple','pear','pineapple']
#if 'orange' in fruits:
#    print('orange not bad')
#if 'apple' in fruits:
#    print('apple is good')
#if 'pear' in fruits:
#    print('pear is nice')
#if 'pineapple' in fruits:
#    print('pineapple is great')


#3-multiple lists
available=['cheese','meat','onion']
requests=[]
while True:
    requested=input('enter you requests: ')
    requests.append(requested)
    another=input('do you want another? (y/n):')
    if another=='y':
        continue
    else:
        break
for request in requests:
    if request in available:
        print(f'adding {request} to pizza')
    else:
        print(f'sorry we dont have {request}')
print('your pizza is finished')

