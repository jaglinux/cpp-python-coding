def func(a):
    b={}
    for i in a:
        if i in b:
            b[i]+=1
        else:
            b[i]=1

    c=sorted(b.items(), key=lambda x : x[1])
    if len(c) > 0:
        return c[0][0]

print(func('GeeksforGeeks'))
