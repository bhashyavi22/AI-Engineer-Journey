def prime(num):
    if num<=1:
        return "not a prime"
    for i in range(2,num):
        if num%i==0:
            return "not a prime"
    return "prime"
num=int(input("Enter="))
print(prime(num))

