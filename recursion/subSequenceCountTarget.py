def main(a, target):
    def rec(index, stack):
        if index == len(a):
            if sum(stack) == target:
                return 1
            else:
                return 0
        
        stack.append(a[index])
        left = rec(index+1, stack)
        stack.pop()
        return rec(index+1, stack) + left
    
    return rec(0, [])

a = [2,1,2,5,2]
target = 4
print(main(a, target))

# 3
