def prime_checker(number):
    is_prime=True
    for i in range(2,number-1):
        if number%i == 0:
        #     print("It's not a prime number")
        # else:
        #     print("It's a prime number")
           is_prime = False
    if is_prime == True:
        print("It's a prime number")
    else:
        print("It's not a prime number")
n=int(input("check this number: "))
prime_checker(number=n)