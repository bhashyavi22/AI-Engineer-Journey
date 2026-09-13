def maxx(a):
    maxi=a[0]
    for i in range(1,len(a)):
        if a[i]>maxi:
            maxi=a[i]
    return maxi
a=list(map(int,input("Enter=").split()))
print(maxx(a))