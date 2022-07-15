
#ZeroDivisionError
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:

        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("you can't divide by 0")
    else:
        print(answer)


#fileNotFoundError exception
filename = 'alice.txt'
try:

    with open(filename,encoding='utf-8') as f:
    contents=f.read()
except FileNotFoundError:
    print(f'sorry,the file {filename} does not exist')
#the split() function to split a string 
else:
    # Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


#Working with Multiple Files
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)