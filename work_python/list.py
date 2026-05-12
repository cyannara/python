arr = [1, 3, 5, 7, 9]
arr.append(11)
arr.extend([13,15])
del arr[0]

arr[0] = 2
print(arr[0])
print(len(arr))

arr2 = [10,11]
arr3 = arr - arr2
print(arr3)