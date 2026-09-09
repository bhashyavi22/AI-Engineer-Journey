
def largest(a,b,c):
    if a>=b and a>=c:
        print(f"Largest={a}")
    elif b>=a and b>=c:
        print(f"Largest={b}")
    else:
        print(f"Largest={c}")
a=float(input("Enter first number="))
b=float(input("Enter second number="))
c=float(input("Enter third number="))
largest(a,b,c)
