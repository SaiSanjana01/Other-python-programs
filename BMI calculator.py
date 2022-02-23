#To calculate body mass index

weight_of_user=float(input("what is your weight?(in kg):"))
height_of_user=float(input("what is your height?(in meters) :"))
bmi_value=weight_of_user/height_of_user**2
#method-1
bmi=round(bmi_value,2)

#method-2 => using f strings
bmi=f'{bmi_value:.2f}'
print(bmi)

