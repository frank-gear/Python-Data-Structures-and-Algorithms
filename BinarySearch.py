


# build the binary search
def binSrch(numList, key):
    high = len(numList) - 1
    mid = len(numList) // 2
    low = 0
    while (high >= low):
        mid = (high + low) // 2

        if numList[mid] > key:
            high = mid - 1
        elif numList[mid] < key:
            low = mid + 1
        else:
            return mid
    return -1


# Test the Search
numList = [2, 4, 6, 8, 9, 10, 11, 12]

print('Please choose a number from below to find out its index')
print(str(numList))
key = int(input())
indexkey = binSrch(numList, key)
if indexkey == -1:
    print("number not found in list")
else:
    print("The index for", str(key), "is", str(indexkey) + '.')
