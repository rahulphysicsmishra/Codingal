# function to count the frequency of each
# character in a string
def frequency(s):
    # creating a dictionary to store the frequency
    # of each character
    s = s.lower()  # ignoring case
    d = {}
    for i in range(len(s)):
        # checking if the character is already
        # in the dictionary
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    return d

# driver code
inp = input("Enter String: ")
print(frequency(inp))
