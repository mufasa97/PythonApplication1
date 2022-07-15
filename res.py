class Tab:
    menu={'steak':10,
         'pasta':3,
         'chicken':2,
         'sprite':1,
         'pepsi':1,
         'desert':4,
         'salad':6,
    }
    def __init__(self):
        self.total=0
        self.items=[]



    def add(self,item):
        self.items.append(item)
        self.total +=self.menu[item]
    def print_bill(self,tax,tip):

        tax=(tax/100) *self.total
        tip=(tip/100) *self.total
        total=self.total+ tax+ tip
        for item in self.items:
            print(f'{item:20} ${self.menu[item]}')
        print(f'{"Total":20} ${total:.2f}')