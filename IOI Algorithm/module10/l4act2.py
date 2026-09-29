# Program to find lexicographically next string

def nextWord(s):

    # If the string is empty,
    if (s == ""):
        return "a"

    # Find the first character from the right
    # which is not z.
    i = len(s) - 1
    while (s[i] == 'z' and i >= 0):
        i -= 1

    # If all characters are 'z', append
    # an 'a' at the end.
    if (i == -1):
        s = s + 'a'

    # If there are some non-z characters
    # else:
    s = s.replace(s[i], chr(ord(s[i]) + 1), 1)

    return s

inp = input("Enter string: ")
print(nextWord(inp))