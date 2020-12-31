def InsertionSort(lis):
    for i in range(1,len(lis)):
        anchor = lis[i]
        j = i-1
        while j >= 0 and anchor < lis[j]:
             lis[j+1] = lis[j]
             j = j-1
        lis[j+1] = anchor
    return lis



n =int(input("Enter the size of the list\n"))
lis = []
for i in range(0,n):
    print("Enter elemnt "+str(i))
    ele = int(input())
    lis.append(ele)

print('list u entered.....\n')
print(lis)

lis = InsertionSort(lis)
print("list after sorting through Insertion sort algorithm")
print(lis)



