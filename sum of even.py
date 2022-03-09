total_number=0
# method-1
for num in range(2,101,2):
    total_number+= num 
print(total_number)

#  method-2
total2=0
for num in range(2,101):
    if num%2 == 0:
        total2+=num
print(total2)