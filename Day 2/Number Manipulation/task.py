# flooring a number
bmi = 84 / 1.65 ** 2
print(bmi)
# number manipulation
print(int(bmi))
print(round(bmi))
#rounding a number
print(round(bmi , 2))



#assignment operator(+=,-=,*=./=)
score = 0

# user scores a point
score+= 1
print(score)


# f-string
print("your score is " + str(score))



# or we can write this way
score=0
height=1.8
is_winning=True
print(f"your score is = {score} , your height is {height} , you are winning is {is_winning}")
