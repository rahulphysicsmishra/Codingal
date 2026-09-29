# Count how many times each letter comes in a word
def frequency(word):
    word = word.replace(" ", "").lower()  # remove spaces + make all letters small
    counts = {}

    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    return counts

# Check if two words are anagrams (same letters, same count)
def checkAnagrams(word1, word2):
    if frequency(word1) == frequency(word2):
        return True
    else:
        return False

# Driver code
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

print(checkAnagrams(word1, word2))