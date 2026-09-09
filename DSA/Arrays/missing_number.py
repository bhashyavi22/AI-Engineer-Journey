def missing(arr):
    n=len(arr)+1
    xor_all=0
    xor_arr=0
    for i in range(1,n+1):
        xor_all^=i
    for j in arr:
        xor_arr^=j
    return xor_all^xor_arr
arr=list(map(int,input("Enter the numbers=").split()))
print(missing(arr))
