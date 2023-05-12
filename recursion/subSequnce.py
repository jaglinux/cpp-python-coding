def main(a):
    def rec(index, stack):
        if index == len(a):
            if len(stack):
                print(stack)
            else:
                print("{}")
        else:
            stack.append([a[index]])
            rec(index+1, stack)
            stack.pop()
            rec(index+1, stack)
    
    rec(0, [])
    
main([3,1,2])

# Time Complexity
# O(2 ** n)
# Space Complexity
# O(n)
# [[3], [1], [2]]
# [[3], [1]]
# [[3], [2]]
# [[3]]
# [[1], [2]]
# [[1]]
# [[2]]
# {}

# Reverse order
def main(a):
    def rec(index, stack):
        if index == len(a):
            if len(stack):
                print(stack)
            else:
                print("{}")
        else:
            rec(index+1, stack)
            stack.append([a[index]])
            rec(index+1, stack)
            stack.pop()
    
    rec(0, [])
    
main([3,1,2])

# {}
# [[2]]
# [[1]]
# [[1], [2]]
# [[3]]
# [[3], [2]]
# [[3], [1]]
# [[3], [1], [2]]
