def SearchFirstPos(a, x, si):
    if len(a) == si:
        return -1
    if a[si] == x:
        return si
    return SearchFirstPos(a, x, si + 1)


li = []
n = int(input("Enter the sizze of list..\n"))
print("Enter the elements now")
for i in range(n):
    li[i] = int(input())
key = int(input("enter the key"))
print(SearchFirstPos(li, key, 0))
