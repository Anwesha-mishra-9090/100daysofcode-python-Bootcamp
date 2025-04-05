from operator import length_hint

# len("Hello")
# print(type("123"))
# print(type(123))
# print(type(3.14))
# print(type(True))


# data type convertion
# print(int("123") + int("345"))

# int()
# float()
# str()
# bool()

user_name = input("Enter your name")
length_of_the_user =len(user_name)
print(type("Number of letters in your name:")) #str
print(type(length_of_the_user)) #int
print("Number of letters in your name: " + str(length_of_the_user) )
