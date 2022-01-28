# Linear Search Algorithm


from random import randint
from tkinter import N

# Linear Search Algorithm

def linSrch(numList, key):
    for i in range(len(numList)):
        if numList[i] == key:
            return i
    return -1


# Test the Search 
numList = [2, 4, 6, 8, 9, 10, 11, 12]

print('Please choose a number from below to find out its index')
print(str(numList))
key = int(input())
indexkey = linSrch(numList, key)
if indexkey == -1:
    print("number not found in list")
else:
    print("The index for", str(key), "is", str(indexkey) + '.')
