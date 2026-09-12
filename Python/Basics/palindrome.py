def pal(a):
    """Check whether a string is a palindrome."""
    if a[::-1] == a:
        return "Palindrome"
    return "Not a palindrome"


a = input("Enter the string = ")
print(pal(a))