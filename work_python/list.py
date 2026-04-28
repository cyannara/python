arr = [1, 3, 5, 7, 9]
arr.append(11)
arr.extend([13,15])
del arr[0]

arr[0] = 2
print(arr[0])
print(len(arr))