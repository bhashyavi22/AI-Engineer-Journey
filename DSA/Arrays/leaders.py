def leaders(arr):
    l=[]
    maxx=float('-inf')
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>maxx:
            maxx=arr[i]
            l.append(maxx)
    l.reverse()
    return l
arr=list(map(int,input("enter the elements=").split()))
print(leaders(arr))