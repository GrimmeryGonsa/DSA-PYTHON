def towerOfHanoi(disk, source, destination, aux):
    if disk == 1:
        print("move disk 1 from " + source + " to " + destination)
        return
    else:
        print("enter")
        towerOfHanoi(disk - 1, source, aux, destination)
        print("move disk " + str(disk) + " from " +str(source) + " to " + str(destination))
        towerOfHanoi(disk - 1, aux, destination, source)


n = int(input("Enter the number of disks...\n"))
towerOfHanoi(n, 'A', 'B', 'C')
