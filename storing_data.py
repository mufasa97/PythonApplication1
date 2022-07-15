#storing data 1) json dump(),2) json.load()
#1)
import json
#numbers=[5,2,4,7,8,2]
#filename='numbers.json'
#with open(filename,'w') as f:
#    json.dump(numbers,f)

#2)
filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
    print(numbers)
