def replace(input):
    n = len(input)
    i=0
    while True:
       if input[i] == 'a':
            input[i] = 'd'
            if i+1 >= n:
                input.append('d')
            else:
                input.insert(i+1, 'd')
            i+=2
       elif input[i] == 'b':
            if i+1 >= n:
                input.pop()
                return
            else:
                input.pop(i)
       else:
           i+=1

       if i >= n:
           return



input=['a', 'c', 'd', 'b', 'b', 'c', 'a']
replace(input)
print(input)

//less time complexity but more space complexity
def replace_1(input):
    output=[]
    for i in input:
        if i == 'a':
            output.append('d')
            output.append('d')
        elif i != 'b':
            output.append(i)
    return output

input=['a', 'c', 'd', 'b', 'b', 'c', 'a']
output = replace(input)
print(input)
print(output)
