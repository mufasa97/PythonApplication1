    
def build_person(first_name,last_name,age=None):
    '''return dic information about a person'''
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician=build_person('mustafa','watheq')
print(musician)
musician=build_person('mustafa','watheq',24)
print(musician)

#2- while loop with input and if to exit

#def get_formatted_name(first_name, last_name):
#    """return a full name, neatly formatted."""
#    full_name = f"{first_name} {last_name}" 
#    return full_name.title()
# while True:
#     print("\nplease tell me your name:") 
#     print("(enter 'q' at any time to quit)") 

#     f_name = input("first name: ")
#     if f_name == 'q':
#         break
     
#     l_name = input("last name: ")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nhello, {formatted_name}!")

# 3- list with function as an attribute

#def print_models(unprinted_designs, completed_models):
#    '''
#    simulate printing each design, until none are left
#    move each design to completed_models after printing.
#    '''
#    while unprinted_designs:
#        current_design = unprinted_designs.pop()
#        print(f"printing model: {current_design}")
#        completed_models.append(current_design)
        
#def show_completed_models(completed_models):
#    """show all the models that were printed."""
#    print("\nthe following models have been printed:")
#    for completed_model in completed_models:
#        print(completed_model)

#unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron'] 
#completed_models = []

#print_models(unprinted_designs, completed_models)
#show_completed_models(completed_models)

##to keep the original list just do this at the calling
#print_models(unprinted_designs[:],completed_models)