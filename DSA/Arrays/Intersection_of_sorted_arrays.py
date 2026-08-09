def intersection(arr1,arr2):
    i=0
    j=0
    result=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]==arr2[j]:
            result.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
    return result

arr1=list(map(int,input("Enter the Elements of array1=").split()))
arr2=list(map(int,input("Enter the Elements of array2=").split()))
ans=intersection(arr1,arr2)
print(*ans)
