def is_leap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    month_day=[31,28,31,30,31,30,31,31,30,31,30,31]
    #feb is for leap year ane only checking the condition and printing the months
    if is_leap(year) and month == 2:
        return 29 
    return month_day[month-1]

year=int(input("enter the year: "))
month=int(input("enter the month: "))
days=days_in_month(year,month)
print(days)

# The reason for adding -1 aftet the month is for the index if we mention the month as 2
# return month_day[month]#-1]

# o/p:
# enter the year: 2022
# enter the month: 2
# 31