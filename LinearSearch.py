#Linear Search Algorithm

#Search string for the letter A
def linSrch(word):
    count = 0;
    for x in word:
        if x == 'a' or x == 'A':
            count += 1;
    if count == 0:
        print("There is not a letter A in this string");
    else:
        print("The letter A count for this string is", str(count) + ".");

print("Please enter a string to search")
linSrch(input())        