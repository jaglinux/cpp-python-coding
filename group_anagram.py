words = [ "eat","tea","tan","ate","nat","bat"]
h = {}
result=[]

for word in words:
    s_word = ''.join(sorted(word))
    if s_word not in h:
        h[s_word] = []
    h[s_word].append(word)

for v in h.values():
    result.append(v)

print(result)
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# words = [ "eat","tea","tan","ate","nat","bat"]
# h = {}
# result=[]

# for word in words:
#     s_word = tuple(sorted(word))
#     if s_word not in h:
#         h[s_word] = []
#     h[s_word].append(word)

# for v in h.values():
#     result.append(v)

# print(result)
