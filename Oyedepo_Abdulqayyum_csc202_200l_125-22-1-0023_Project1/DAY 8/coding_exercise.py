def paint_calc(height,width,cover):
    result=round(((test_h*test_w)/coverage))
    print(f"You will need {result} cans of paint")



test_h = int(input("Height of wall:"))
test_w = int(input("Width of wall:"))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#another way to round up decimal numbers

# first import math 
#math.ceil()
