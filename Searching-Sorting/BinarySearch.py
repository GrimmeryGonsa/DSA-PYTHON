def binary(lis, key):
    lo = 0
    hi = len(lis)-1
    mid = 0

    while lo<=hi:
        mid = (lo+hi)//2
        if lis[mid] == key:
            return True
        elif lis[mid] > key:
            hi = mid -1
        else :
            lo = mid +1
    
    return False





n =int(input("Enter the size of the list\n"))
lis = []
for i in range(0,n):
    print("Enter elemnt "+str(i))
    ele = int(input())
    lis.append(ele)

print('list u entered.....\n')
print(lis)

print("Enter the key to be searched...")
key =int(input())
lis.sort()

if binary(lis, key):
    print("List contains key")

else:
    print("Key not present :( ")

