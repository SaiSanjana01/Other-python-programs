#To calculate body mass index

weight_of_user=float(input("what is your weight?(in kg):"))
height_of_user=float(input("what is your height?(in meters) :"))
bmi_value=weight_of_user/height_of_user**2
bmi=round(bmi_value,2) 
if bmi<18.5:
    print(f"your bmi is {bmi} ,you are underweight")
elif bmi < 25:
    print(f"your bmi is {bmi} ,you are normal weight")
elif bmi<30:
    print(f"your bmi is {bmi} ,you are over weight")
elif bmi < 35:
    print(f"your bmi is {bmi} ,you are obese")
else:
    print(f"your bmi is {bmi} ,you are clinically obese consult a doctor")
    
    



