students = ['A', 'B', 'A', 'A', 'C', 'C', 'A', 'B', 'C', 'C', 'C']
h={}
result=[]

for student in students:
    if student not in h:
        h[student]=0
    h[student]+=1

print(h)
while len(h) >= 2:
    a = sorted(h.items(), key=lambda x:x[1], reverse=True)
    result.append(a[0][0])
    result.append(a[1][0])
    h[a[0][0]] -= 1
    h[a[1][0]] -= 1
    if not h[a[0][0]]:
        del h[a[0][0]]
    if not h[a[1][0]]:
        del h[a[1][0]]
    print(h)

for i in h:
    for _ in range(h[i]):
        result.append(i)

print(result)
#['C', 'A', 'C', 'A', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
