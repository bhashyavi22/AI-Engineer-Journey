def two_sum(arr,target):
    seen={}
    for i in range(len(arr)):
        complement=target-arr[i]
        if complement in seen:
            return [seen[complement],i]
        seen[arr[i]]=i
    return [-1,-1]
arr=list(map(int,input("Enter the elements=").split()))
target=int(input("Enter the target element="))
print(two_sum(arr,target))