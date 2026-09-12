def palindrome(a): 
    if a[::-1]==a:
        return "Palindrome"
    return "Not a palindrome"
a=input("Enter the string=")
print(palindrome(a))