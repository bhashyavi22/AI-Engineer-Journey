def stocks(arr):
    minn=float('+inf')
    m_profit=0
    for i in range(len(arr)):
        if arr[i]<minn:
            minn=arr[i]
        c_profit=arr[i]-minn
        m_profit=max(c_profit,m_profit)
    return m_profit
arr=list(map(int,input("Enter the elements=").split()))
print(stocks(arr))