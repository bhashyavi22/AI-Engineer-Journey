def frequency(arr):
    count = {}

    for num in arr:
        count[num] = count.get(num, 0) + 1

    return count


arr = list(map(int, input("Enter numbers: ").split()))

print(frequency(arr))