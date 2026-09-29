def sort(s):
    # code here
    li = []
    ans = ""
    for i in range(26):
        li.append(0)
    for i in range(len(s)):
        ind = ord(s[i]) - ord('a')
        li[ind] += 1
    for i in range(26):
        if li[i] >= 1:
            for j in range(li[i]):
                ans = ans + chr(ord('a') + i)
    return ans

print(sort("edba"))