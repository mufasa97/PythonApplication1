
import unittest
from test_course_exercise import Employee

class Employee(unittest.TestCase):


    def setUp(self):
       self.mustafa('mustafa','watheq',65000)
        

#make_pizza(13,'mushroom','cheese','onion')

#2-making a unlimted dictionary from from a function

def build_profile(first,last,**user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info


    def test_give_default_raise(self):
        self.mustafa.give_raise()
        self.my_salary.give_raise(self.mustafa.salary,70000)

        


    def test_give_custom_raise(self):
        self.mustafa.give_raise(10000)
        self.my_salary.give_raise(self.mustafa.salary,75000)


if __name__ == '__main__':
    unittest.main()

        
