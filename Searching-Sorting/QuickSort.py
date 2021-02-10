def partition(array, start, end) -> int:
    pivot = array[start]
    count = 0
    for i in range(start, end+1):
        if array[i] < pivot:
            count = count+1
    array[start+ count], array[start] = array[start], array[start+count]
    pivotIndex = start+count

    i = start
    j = end

    while(i<j):
        if array[i]<pivot:
            i = i+1
        elif array[j]>= pivot:
            j =j-1
        else:
            array[i], array[j] = array[j], array[i]
            i = i+1
            j =j-1
    return pivotIndex

             




def quickSort(array, start, end) -> None:
    if start >= end:
        return
    pivot = partition(array, start, end)
    quickSort(array, start, pivot-1)
    quickSort(array, pivot+1, end)


arr = [1,2,3,90,41,600,1042,-20]
quickSort(arr,0,len(arr)-1)
print(arr)