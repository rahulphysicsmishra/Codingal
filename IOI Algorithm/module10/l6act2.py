# Checks if s1 is a substring of s2
def isSubstring(s1, s2):
    if s1 in s2:
        return s2.index(s1)
    return -1

# Driver Code
if __name__ == "__main__":
    s1 = "welcome"
    s2 = "welcome to codingal"
    result = isSubstring(s1, s2)
    if result == -1 :
        print("Not present")
    else:
        print("Present at index " + str(result))