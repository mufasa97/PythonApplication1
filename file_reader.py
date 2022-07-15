with open('pi_digits.txt') as file_object:
    contents = file_object.read() 
    print(contents.rstrip())
    #1-with open('text_files/filename.txt') as file_object: #used to look for the for a file 
    #if it is not on the same folder and used for text files

    #2-absolute file path
    #tell Python exactly where the file is on your computer regardless of where the 
    #program that’s being executed is stored


    #example:
    #file_path = '/home/ehmatthes/other_files/text_files/filename.txt' 
    #with open(file_path) as file_object:

    #there is a note on bakslash on phone




    #reading line by line code:
filename = 'pi_digits.txt'
 with open(filename) as file_object:
     for line in file_object:
         print(line.rstrip())#to have no empty lines and create te same output as above 


#Making a List of Lines from a File 
filename = 'pi_digits.txt'
with open(filename) as file_object:
     lines = file_object.readlines()
for line in lines:
     print(line.rstrip())

#Working with a File’s Contents after reading a file
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

#Large Files: One Million Digits 
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = '' 
for line in lines:
    pi_string += line.strip()
print(f"{pi_string[:51]}...")#print the first 50 digits
print(len(pi_string))


#Is Your Birthday Contained in Pi?
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
birthday = input("Enter your birthday, in the form mmddyy: ") 
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

        
#you can replace a word in a string like:
message = "I really like dogs."
message.replace('dog', 'cat')
#you can do it from code above by reading line by line and changing a word from it

