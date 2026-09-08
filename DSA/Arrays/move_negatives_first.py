def move_negatives(arr):
    i=0
    for j in range(len(arr)):
        if arr[j]<0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    return arr
arr=list(map(int,input("Enter the elements=").split()))
print(move_negatives(arr))