student_score=input("Input of list of student score: ").split()
for n in range(0,len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)
highest_score=0
for score in student_score:
    if score > highest_score:
        highest_score = score
print(f'The highest score of the student is: {highest_score}')

