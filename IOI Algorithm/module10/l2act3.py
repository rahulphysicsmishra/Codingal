def removeVowels(s):
    result = ""
    # list containing vowels
    li = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)):
        # checking the presence of vowels in the string
        if s[i] in li:
            # removing vowels
            result = result + " "
        else:
            result = result + s[i]
    return result

# driver code
inp = input("Enter String: ")
print("Result:", removeVowels(inp))