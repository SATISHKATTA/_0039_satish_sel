"""
Python for Testers

1.Python is a high-level object-oriented programming language developed
in the late 1980s by Guido van Rossum.
2.Python is very popular,free and very widely used.
3.Python is interpreted.
4.Python is sample and easy to learn.

"""
# Python 3 program to counts Palindromic
# Subsequence in a given String using recursion

str = "S,N"

# Function return the total
# palindromic subsequence


def countPS(N, S):

    if(N > S):
        return 0

    if(dp[N][S] != -1):
        return dp[N][S]

    if(N == S):
        dp[N][S] = 1
        return dp[N][S]

    elif (str[N] == str[S]):
        dp[N][S] = (countPS(N + 1, S) +
                    countPS(N, S - 1) + 1)
        return dp[N][S]
    else:
        dp[N][S] = (countPS(N+ 1, S) +
                    countPS(N, S - 1) -
                    countPS(N + 1, N - 1))
        return dp[N][S]


# Driver code
if __name__ == "__main__":

    dp = [[-1 for x in range(1000)]
          for y in range(1000)]

    n = len(str)
    print("Total palindromic subsequence are :",
          countPS(0, n - 1))
"""
"""
from itertools import combinations
msg='satishbabukatta'.lower()

str2=[]
lst=[]
sub_strng=[]

for i in range(1,len(msg)+1):
    lst.append(list(combinations(msg, i)))
    # print(lst)
for i in lst:
    for item in i:
        sub_str=''.join(item)
        sub_strng.append(sub_str)
# print(sub_strng)
# print(sub_strng)
palindrome_stg=[]
for i in sub_strng:
    if i==i[::-1]:
        palindrome_stg.append(i)
print("Number of palindrome strings : ",len(set(palindrome_stg)))
print(set(palindrome_stg))
"""

import itertools

n = int(input("Enter size of string: "))
string = input("Enter string: ")
oplist = []
finallst = []

for i in range(1,n+1):
    result = list(itertools.combinations(string,i))
    # print(result)
    oplist.append(result)
#print(oplist)
for element in oplist:
    #print(element)
    for item in element:
        it = ''.join(item)
        finallst.append(it)
print(finallst)
count = 0
for element in finallst:
    if element == element[::-1]:
        count += 1
        print(element)
print("Total no. of palindrome subsequences are: ",count)

"""








