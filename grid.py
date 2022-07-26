import random, time, os

def make2darray(length):
    counter = 0
    x = []
    for i in range(0, length):
        y = []
        for j in range(0, length):
            y.append(counter)
            counter += 1
        x.append(y)
    return x

def arrayLoop(array, pos):
    newArray = array
    #pos = random.randint(0, len(array))
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if array[i][j] == pos:
                newArray[i][j] = 'hello'
            else:
                  newArray[i][j] = '     '     
    return newArray 

#x = make2darray(3)

for j in [2, 4, 6]:
    x = make2darray(3)
    for i in arrayLoop(x, j):
        print(i, end="\n")
    os.system('clear')
    time.sleep(1)

#for row in x:
#    print(row)

#for i in range(0, len(x)):
#    print(x[i], end=' ')
#    print('\n')
