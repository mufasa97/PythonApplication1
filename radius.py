
def area(radius):
    return 3.14*radius*radius
def vol(area,length):
    print(area*length)


radius=int(input('enter the radius:'))
length=int(input('enter the length:'))

area_ans=area(radius)
vol(area_ans,length)
from hello import hello1