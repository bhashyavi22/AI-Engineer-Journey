def remove_duplicates(arr):
    if len(arr)<2:
        return len(arr)

    i=0
    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
           i+=1
           arr[i]=arr[j]
    return i+1
arr=list(map(int,input("Enter the Numbers=").split()))
k=remove_duplicates(arr)
print("Number of unique elements=",k)
print("Array after removing duplicates=",end=" ")
print(*arr[:k])