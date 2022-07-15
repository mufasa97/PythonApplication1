class Planet:
    def __init__(self):
        self.name='hoth'
        self.radius=50000
        self.gravity=5.5
        self.system='hoth system'
    def orbit(self):
        return f'{self.name} is in the {self.system}'


    @classmethod
    def common(cls):
        return f'all planets are {cls.shape} bcause of gravity'

    @staticmethod
    def spin(speed='2000 miles per hour'):
        return f'the planet spins and spins at speed'


    

hoth=Planet()
print(f'name is: {hoth.name}')
print(f'radius is: {hoth.radius}')
print(f'gravity is: {hoth.gravity}')
print(hoth.orbit())

planetx=Planet()