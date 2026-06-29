arr=list(map(int,input("Enter numbers=").split()))
sorted_array=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        sorted_array=False
        break
if sorted_array:
    print("Sorted")
else:
    print("Not sorted")
