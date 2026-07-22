height=float(input("Enter your height in meters:"))
weight=float(input("Enter your weight in kg:"))
BMI=weight/(height*height)
if BMI >= 30:
    print("obesity")
elif BMI >= 25:
    print("overweight")
elif BMI >= 18.5:
    print("normal")
else:
    print("under weight")
 