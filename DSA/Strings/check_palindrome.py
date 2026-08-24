def check_palindrome(s):
    ans=s
    s=list(s)
    i=0
    j=len(s)-1
    while i<=j:
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
    if ans=="".join(s):
        return "Palindrome"
    return "Not a palindrome"
s=input("Enter=")
print(check_palindrome(s))