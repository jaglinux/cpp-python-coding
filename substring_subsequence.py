def substring(s, t):
    for i in range(len(s)- len(t)):
        for j in range(len(t)):
            if t[j] != s[j+i]:
                break
        else:
            return i
    else:
        return False

def subsequence(s, t):
    j=0
    for i in range(len(s)):
        if s[i] == t[j]:
            j+=1
        if j == len(t):
            return True
    else:
        return False


print(substring('geeksforgeeks', 'gor'))
print(subsequence('geeksforgeeks', 'gors'))
