arr=list(map(int,input("Enter numbers=").split()))
d=int(input("Number of positions="))
d=d%len(arr)
arr1=[]
arr2=[]
for i in range(d):
   arr1.append(arr[i])
for i in range(len(arr)-d):
   arr2.append(arr[i+d])
for i in arr1:
   arr2.append(i)
print(arr2)

#Another Approach
arr=list(map(int,input("Enter numbers=").split()))
d=int(input("Number of Positions"))
d=d%len(arr)
for i in range(d):
    first=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[-1]=first
print(*arr)