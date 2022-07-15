#writing an empty file
file_name='programming1.txt'
with open(file_name,'w') as file_object:#'w' mean to open the file in write mode
                                        #read mode is'I',append 'a',read and write 'I+'
    file_object.write("i love programming.\n")
    file_object.write("I love creating new games.\n")

# be careful opening a file in write mode ('w') because if the file does exist, 
# Python will erase the contents of the file before returning the file object. 
with open(file_name, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
