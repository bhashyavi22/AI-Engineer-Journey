def SingleElement(arr):
    result=0
    for i in arr:
        result=result^i
    return result
arr=list(map(int,input("Enter the Numbers=").split()))
print(SingleElement(arr))