def majority_element(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    major=arr[0]
    for i in freq:
        if freq[i]>freq[major]:
            major=i
    return major
arr=list(map(int,input("enter the elements=").split()))
print(majority_element(arr))