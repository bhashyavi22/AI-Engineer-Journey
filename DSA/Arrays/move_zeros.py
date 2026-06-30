arr=list(map(int,input("Enter numbers=").split()))
zero_count=0
new_arr=[]
for num in arr:
    if num!=0:
        new_arr.append(num)
    else:
        zero_count+=1
for i in range(zero_count):
    new_arr.append(0)
print(new_arr)