def merger(lis1, lis2):
    i = 0
    j = 0
    solution = []
    while(i<len(lis1) and j<len(lis2)):
        if(lis1[i]<lis2[j]):
            solution.append(lis1[i])
            i = i+1
        else:
            solution.append(lis2[j])
            j = j+1
    while(i<len(lis1)):
        solution.append(lis1[i])
        i = i+1
    while(j<len(lis2)):
        solution.append(lis2[j])
        j = j+1
    
    return solution


n1 =int(input("Enter the size of the list-1\n"))
lis1 = []
for i in range(0,n1):
    print("Enter elemnt "+str(i))
    ele = int(input())
    lis1.append(ele)

print('list u entered.....\n')
print(lis1)

n2 =int(input("Enter the size of the list-2\n"))
lis2 = []

for i in range(0,n2):
    print("Enter elemnt "+str(i))
    ele = int(input())
    lis2.append(ele)

print('list u entered.....\n')
print(lis2)

solution = merger(lis1,lis2)
print(solution)