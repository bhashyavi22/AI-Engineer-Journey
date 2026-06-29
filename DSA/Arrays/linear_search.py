arr=list(map(int,input("Enter numbers=").split()))
target=int(input("Enter target="))
found=False
for i in range(len(arr)):
    if arr[i]==target:
        print(f"Found at index {i}")
        found=True
        break
if not found:
    print("Not Found")
    