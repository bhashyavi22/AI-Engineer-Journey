import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[arr > 25])
print(arr[arr < 30])
print(arr[arr % 20 == 0])
print(arr[(arr >= 20) & (arr <= 40)])