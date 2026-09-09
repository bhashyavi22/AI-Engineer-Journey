def bmi(weight,height):
    BMI=weight/(height**2)
    return BMI
def simple_interest(principal,time,rate):
    SI=(principal*time*rate)/100
    return SI
weight=float(input("Enter the value="))
height=float(input("Enter the value="))
print(f"BMI={bmi(weight,height)}")
principal=float(input("enter the value="))
time=float(input("Enter the value="))
rate=float(input("Enter the value="))
print(f"SIMPLE INTEREST={simple_interest(principal,time,rate)}")