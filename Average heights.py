student_height=input("Input a list of student heights: ").split()
for n in range(0,len(student_height)):
    student_height[n] = int(student_height[n])
# print(student_height)
total_height=0
for height in student_height:
    total_height += height
# print(total_height)
length_of_list=0
for length in student_height:
    length_of_list +=1
# print(length_of_list)
average_height=round(total_height/ length_of_list)
print(average_height)
