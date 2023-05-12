def main(a, target):
    def rec(index, stack):
        if index == len(a):
            if sum(stack) == target:
                print("target found ", stack)
                return True
            else:
                return False;
        stack.append(a[index])
        if rec(index+1, stack) == True: return True
        stack.pop()
        return rec(index+1, stack)
    
    return rec(0, [])

a = [2,1,2]
target = 3
ret = main(a, target)
if not ret:
    print('Target not found ')
    
# target found  [2, 1]
