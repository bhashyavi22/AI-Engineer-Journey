arr = list(map(int, input("Enter numbers = ").split()))

for i in range(len(arr)):
    leader = True

    for j in range(i + 1, len(arr)):
        if arr[j] > arr[i]:
            leader = False
            break

    if leader:
        print(arr[i], end=" ")