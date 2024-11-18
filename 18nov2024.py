# p1. Write a Python function that prints out the first n rows of Pascal's triangle.

# def printpascalrow(number):
#     for i in range(0, number+1):
#         print (11**i,",")

# number = int(input())

# printpascalrow(number)
# ------------------------------------------------------------------------------

# p2. Write a Python function to check whether a string is a pangram or not.
# def ispangram(givenstring):
#     allalphabet = "abcdefghijklmnopqrstuvwxyz"
#     dict = {}
#     givenstring = givenstring.lower()
#     for character in givenstring:
        
#         if character.isalpha():
#             dict[character] = 1
#     for i in allalphabet:
#         if not i in dict:
#             return False

#     else:
#         return True

# print(ispangram("The quick brown fox jumps over the lazy dog"))
# ------------------------------------------------------------------------------

# p3.Write a Python function that checks whether a passed string is a palindrome or not.
# def ispalindrome(givenword):
#     counter = 0
#     reversecounter = len(givenword) - 1 

#     while counter != reversecounter:
#         if givenword[counter] != givenword[reversecounter]:
#             return False
#         counter += 1
#         reversecounter -= 1
#         if counter == len(givenword) - 1:
#             return True

#     else:
#         return True
    
# print(ispalindrome("1223"))

# p4. Write a Python program to print the even numbers from a given list
def evenornot(givenlist, emptylist):
    for number in givenlist:
        if number%2 == 0:
            emptylist.append(number)

    print(emptylist)
    
SampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
emptylist = []

evenornot(SampleList, emptylist)



