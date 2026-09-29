# function to reverse a string
def reverse(s):
    return s[::-1]

# function to check the string is a palindrome
def checkPalindrome(s):

    # ignoring case
    s = s.lower()

    rev_string = reverse(s)

    if s == rev_string:
        return True
    else:
        return False

# driver code
inp = input("Enter String: ")
print(checkPalindrome(inp))