# Create an Insertion Sorting Algorithm
def insrtSrt(numList):
    for i in range(1, len(numList)):
        j = i

        while(j > 0 and numList[j] < numList[j - 1]):
            temp = numList[j]
            numList[j] = numList[j - 1]
            numList[j - 1] = temp
            j -= 1
    return numList


# Test Insertion Sort Algorithm
wordL = [10, 2, 78, 4, 45, 32, 7, 11]
wordR = insrtSrt(wordL[:])
print("here is", wordL, 'sorted to', wordR)
