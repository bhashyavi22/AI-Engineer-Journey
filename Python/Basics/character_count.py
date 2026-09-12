def char(a):
    seen={}
    for i in a:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1
    return seen
a=input("Enter=")
print(char(a))