from random import randint
class Die:
    
    def __init__(self):
        self.sides=6
    
    def update_side(self,num_side):
        self.sides=num_side

    def roll_dice(self):
        list_num=[]
        for roll in range(1,11):
            
            roll=randint(1,self.sides)
            list_num.append(roll)
        return list_num  
    def print_side(self,rand_last):
        print(rand_last)

roll=Die()
list_call=roll.roll_dice()
roll.print_side(list_call)

roll.update_side(10)
list_call=roll.roll_dice()
roll.print_side(list_call)

roll.update_side(20)
list_call=roll.roll_dice()
roll.print_side( list_call)

#random lottery #to be continued
from random import choice
lottery=[5,'A',6,'D',7,8,'E',5,6,8,'U',9,1,3,'I']
winning_ticket=[]
print("let us see what is the winning ticket is

while len(winning_ticket)<4:
    pulled_item=choice(lottery)
    if pulled_item not in winning_ticket:
        print(f'we pulled a {pulled_item}')
        winning_ticket.append(pulled_item)


