def union_sorted(arr1, arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1

        elif arr1[i] > arr2[j]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1

        else:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1

    while j < len(arr2):
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1

    return result


arr1 = list(map(int,input("Enter the numbers=").split()))
arr2 = list(map(int,input("Enter the numbers=").spli()))

print(union_sorted(arr1, arr2))