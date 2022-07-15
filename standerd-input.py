
#age=int(input('enter your age:'))
#if age<10:
#    print('you are young')
#elif age>50:
#    print('you are old')
        
     

#elif 10<age<50:
        
#        print('you are an adult')
   

def name_enter():
    input('enter you name')

    
 
def trial():

    while True:
        name_enter()
        another=input('do you want to input another name? (y/n):')
        if another=='y':

            continue
        elif another=='n':
            break
        else:
            print('\n\fthis is an invalid input ')


trial()
  
     

    


            


