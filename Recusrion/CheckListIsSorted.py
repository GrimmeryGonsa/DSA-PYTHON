def isSorted(arr, i):
    if len(arr) == 1:
        return True
    if i == 1:
        return arr[1] > arr[0]
    if arr[i] > arr[i - 1]:
        return isSorted(arr, i - 1)
    return False


n = int(input("Enter the list's length"))
arr = []
for i in range(n):
    arr.append(int(input("Enter element " + str(i))))

sol = isSorted(arr, n - 1)
if sol:
    print("Sorted")
else:
    print("not sorted")
