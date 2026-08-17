def sum_avg(arr):
    summ=0
    for i in arr:
        summ+=i
    return summ,summ/len(arr)
arr=list(map(int,input("Enter the Elements=").split()))
ans=sum_avg(arr)
print(f"sum={ans[0]}")
print(f"average={ans[1]}")