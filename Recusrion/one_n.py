# print number frm 1 to n using recursion

def print1ToN(n):
    if n == 0:
        return
    print1ToN(n - 1)
    print(n)


n = int(input("Enter the value of n"))
print1ToN(n)
