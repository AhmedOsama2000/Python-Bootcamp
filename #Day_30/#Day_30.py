"""
1) Errors and Exceptions in python:
try: something that might cause an exception
except: do this if there were an exception
else: do this instead if no exception
finally: do this no matter what happens


2) JSON (JavaScript Object Notation): Most popular format to transfer data over the internet
easier to deal with than text files
JSON Methods:
a) json.dump(): to write data into json file
b) json.load(): to read data from a json file
c) json.update(): to update the data of a json file
"""
#
# try:
#     with open("file1.txt","w") as file:
#         file.write("ahmed")
#
# except FileNotFoundError:
#     print("there's no such a file")
#     # You can do anything when the error happens, e.g. create the file itself
#     # but note that, the execpt will ignore the rest of the errors
#     # then we have to provide the type of the error itself
#     # we can add multiple execptions
# # except KeyError:
#
# else:
#     print("the file exists")
#
# finally:
#     print("this code executes no matter what happens")
#     raise TypeError("I have made this error")


# raise:  # used to raise our own exceptions