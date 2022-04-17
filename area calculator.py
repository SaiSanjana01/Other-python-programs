import math
def paint_calc(height,width,coverage):
    area=height*width
    can_no=math.ceil(area/coverage)
    print(f"We need {can_no} cans of paint")
test_h=int(input("Height of wall? "))
test_w=int(input("Width of wall? "))
#coverage=5
paint_calc(height=test_h,width=test_w,coverage=5)