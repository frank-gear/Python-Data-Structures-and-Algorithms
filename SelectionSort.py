# Create a Selection Sort Algorithm

def SelctSort(wordList):
    for x in range(len(wordList) - 1):
        smllstIndx = x

        for y in range(x + 1, len(wordList)):
            if wordList[smllstIndx] > wordList[y]:
                smllstIndx = y

        temp = wordList[x]
        wordList[x] = wordList[smllstIndx]
        wordList[smllstIndx] = temp
    return wordList


# create test
wordL = [10, 2, 78, 4, 45, 32, 7, 11]
wordR = SelctSort(wordL[:])
print("here is", wordL, 'sorted to', wordR)
