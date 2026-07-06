arr = list(map(int, input("Enter numbers = ").split()))

for i in range(len(arr)):
    found = False

    for j in range(i):
        if arr[i] == arr[j]:
            found = True
            break

    if found:
        continue

    count = 0

    for j in range(len(arr)):
        if arr[j] == arr[i]:
            count += 1

    print(f"{arr[i]} -> {count}")