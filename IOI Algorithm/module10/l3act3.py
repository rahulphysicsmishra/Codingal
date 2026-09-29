# function to count the number of words in a string

def countWords(s):
    count = 0
    # removing leading and trailing spaces from the string
    s = s.strip()
    for i in range(len(s)):
        if s[i] == " ":
            count += 1

    return count + 1 # +1 id for last word

# driver code
inp = input("Enter String: ")
print("Number of words: ", countWords(inp))