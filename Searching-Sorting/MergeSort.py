def getMid(arr):
    return len(arr)//2
def merge(right, left, real):
    i = 0
    j = 0
    k = 0
    while i < len(right) and j < len(left):
        if right[i]<left[j]:
            real[k] = right[i]
            i = i+1
            k = k+1
        else:
            real[k] = left[j]
            k = k+1
            j = j+1
    while i < len(right):
        real [k] = right[i]
        i = i+1
        k = k+1
    while j <len(left):
        real[k] = left[j]
        j =j+1
        k =k+1
    

def mergeSort(arr):
    if len(arr) <= 1:
        return 
    
    mid = getMid(arr)
    smallList1 = []
    smallList2 = []
    for i in range (mid):
        smallList1.append(arr[i]) ##smallList1 = arr[0:mid]
    for i in range (mid, len(arr)):
        smallList2.append(arr[i])##smallList2 = arr[mid:]
    mergeSort(smallList1)
    mergeSort(smallList2)
    merge(smallList1, smallList2, arr)



arr = [1,2,3,90,41,600,1042]
mergeSort(arr)
print(arr)