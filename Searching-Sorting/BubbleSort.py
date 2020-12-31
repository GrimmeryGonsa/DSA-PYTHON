def BubbleSort(lis):
    i = len(lis)
    while i != 0:
        for j in range(0,i-1):
            if lis[j+1] < lis[j]:   #invert sign to sort in descending order...
                temp = lis[j+1]
                lis[j+1] = lis[j]
                lis[j] = temp
        i = i-1
    return lis



n =int(input("Enter the size of the list\n"))
lis = []
for i in range(0,n):
    print("Enter elemnt "+str(i))
    ele = int(input())
    lis.append(ele)

print('list u entered.....\n')
print(lis)

lis = BubbleSort(lis)
print("list after sorting through Bubble sort algorithm")
print(lis)
