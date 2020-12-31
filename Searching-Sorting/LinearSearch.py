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
found = False
for i in lis:
    if i == key:
        print("found key at index "+ str(i))
        found = True

if found == False:
    print("key was not there :(") 