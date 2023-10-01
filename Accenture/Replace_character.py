'''7. The given function has a string (str) and two characters,
ch1 and ch2. Execute the function in such a way that str returns
to its original string, and all the events in ch1 are replaced
by ch2, and vice versa.
Replacecharacter(Char str1, Char ch1, Int 1, Char ch2)

Assumption

This string has only alphabets that are in lower case.

Example

Input:
str: apples
ch1: a
ch2: p

Output:
paales

Explanation
All the ‘a’ in the string is replaced with ‘p’.
And all the ‘p’s are replaced with ‘a’'''
def swap (user_input, str1, str2):

    result = ''

    if user_input != None:

        result = user_input.replace(str1, '*').replace(str2, str1).replace('*', str2)

        return result

    return 'Null'

user_input = input()

str1, str2 = map(str,input().split())

print(swap(user_input, str1, str2))
