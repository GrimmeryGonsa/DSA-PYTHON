def summation(n):
    if n == 0 or n ==1:
        return n
    else:
        return n + summation(n-1)


n = int (input('Enter the number'))
print("sum of first "+ str(n) + " natural numbers is")
print(summation(n))