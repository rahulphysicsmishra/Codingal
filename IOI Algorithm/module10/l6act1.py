def smallest_largest_words(str1):
    word = ""
    all_words = []
    str1 = str1 + " "

    for i in range(0, len(str1)):
        if str1[i] != ' ':
            word = word + str1[i]
        else:
            if word != "":
                all_words.append(word)
            word = ""

    small = large = all_words[0]

    # Find the smallest and largest word in the str1
    for k in range(0, len(all_words)):
        if len(small) > len(all_words[k]):
            small = all_words[k]
        if len(large) < len(all_words[k]):
            large = all_words[k]

    return small, large


# Driver code
s = input("Enter a sentence: ")
small, large = smallest_largest_words(s)
print("Smallest word:", small)
print("Largest word:", large)