import random
test_seed=int(input("create a seed  numer: "))
random.seed(test_seed)
side_of_coin= random.randint(0,1)
if side_of_coin == 1:
    print("Heads")
else:
    print("Tails")
