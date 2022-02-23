#in this program the exception of leap year is extinguished ie not considered for this program
# calculation of years and months and weeks remaining in theie life
age=int(input("what is your age?: "))
years_to_live=int(input("how much years you wish to live in earth?: "))
years=years_to_live - age
years_remaining=years*365
months_remaining=years*12
weeks_remainig=years*52
print(f"You have {years_remaining} days , {months_remaining} Months and {weeks_remainig} weeks left...")
