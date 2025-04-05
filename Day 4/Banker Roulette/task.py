import random


friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
 # choice1
 # choice = random.choice(["Alice", "Bob", "Charlie", "David", "Emanuel"])
#print(choice)
# or
# choice2
# print(random.choice(friends))

# choice3
random_index = random.randint(0,4)
print(friends[random_index])