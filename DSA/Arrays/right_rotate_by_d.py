arr = list(map(int, input("Enter the Numbers=").split()))
d = int(input("Enter the positions="))

d = d % len(arr)

for i in range(d):
    last = arr[-1]

    for j in range(len(arr)-1, 0, -1):
        arr[j] = arr[j-1]

    arr[0] = last

print(*arr)