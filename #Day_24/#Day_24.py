## 
"""
it's better using with open() as ..: instead of just using open() only
read() ==> return the contents of the file as a string
paths: relative vs. absolute
1) absolute: give the full path of the folder
2) relative: give the path of the folder with respect to the current folder directory
(.\) -> current directory , (../ previous directory) , (/file) goes to specific folder
"""
file_name = "my_file.txt"
# with open(file_name) as file:   # open the file, return an object holding the file
#     contents = file.read()  # return the content of the file as a string
#     # file.close()  

# print(contents)
"""
you should close the file after finishing the work, 
to save some resources, despite python closes the file 
automatically when finihsing working with it {when "with" is finished}
"""
# "w" ==> used for writing in file, removing previos data, creates a file when it doesn't exist
# "a" ==> append in the file without overriting
# "r" ==> read the file {default mode}

with open(file_name, "a") as file:
    file.write("My university is fayoum university")