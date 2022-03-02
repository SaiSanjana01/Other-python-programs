import random
from unicodedata import name
test_seed=int(input("create a seed number:"))
random.seed(test_seed)

names=input("give me everybody's name,separated by commas:  ").split(", ")
# print(names)
person=len(names)
random_number=random.randint(0,person-1) # the range of numbers needed
# print(random_number)
person=names[random_number]
print(f'{person} is going to buy the meal today!!')

# method-2 with choices
person=random.choice(names)
print(f'{person} is going to buy the meal today!!')
