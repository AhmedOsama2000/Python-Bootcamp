# OOP in Python
# classes is written in pascal case format ==> PrettyTable , BigCat , BlueCar ...
# practice with our created classes


# create the first class
class User:
    # pass  # pass keyword is used just to make a class/function/if statement ... empty
    # __init__ special method is used to initialize the attributes
    # self refers to the actual object been created
    # def __init__(self,attr1,attr2,....):
    # if you don't want to provide a value for a parameter of the init method, just give it a default value
    # adding a method def method1(self , param1, param2, ...)
    def __init__(self, username, user_id, followers=0, following=0):
        print("a new user has been created! ")
        self.username = username
        self.id = user_id  # id the attribute, user_id is the passed value to the class
        self.followers = followers  # == self.followers = 0 and delete the followers from the parameters list
        self.following = following

    def follow(self):
        self.followers += 1
        self.following += 1


user_1 = User("Ahmed", "001")

user_1.follow()

print(f"user name is {user_1.username}")
print(f"user's followers is {user_1.followers}")
print(f"user's following is {user_1.following}")


