print("Welcome to the Love calculator")
name1=input("what is your name?: ")
name2=input("what is their name?: ")
combined= name1+name2
lower_case=combined.lower()

t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")

true=t+r+u+e

l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")
e=lower_case.count("e")

love=l+o+v+e

score= int(str(true)+str(love))
if score < 10 or score > 90 :
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"your score is {score}, you are alright together.")
else:
    print(f"your score is {score},<3")