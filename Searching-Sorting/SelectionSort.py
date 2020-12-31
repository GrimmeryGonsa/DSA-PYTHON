def getMinIndex(lis, start):
    index = start
    for i in range (start,len(lis)):
        if lis[index] > lis[i]:  ##change sign to sort in descending order
            index = i
    return index


def selectionSort(lis):
    for i in range(0,len(lis)):
        min = getMinIndex(lis,i)
        temp = lis[min]
        lis[min] = lis[i]
        lis[i] = temp
    return lis


n =int(input("Enter the size of the list\n"))
lis = []
for i in range(0,n):
    print("Enter elemnt "+str(i))
    ele = int(input())
    lis.append(ele)

print('list u entered.....\n')
print(lis)

lis = selectionSort(lis)
print("list after sorting through selection sort algorithm")
print(lis)




