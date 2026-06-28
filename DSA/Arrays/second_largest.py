arr=list(map(int,input("Enter numbers=").split()))
largest=float('-inf')
second_largest=float('-inf')
for num in arr:
    if num>largest:
        second_largest=largest
        largest=num
    elif largest>num>second_largest:
        second_largest=num
    
if second_largest==float('-inf'):
    print("No second largest element")
else:
    print(second_largest)
