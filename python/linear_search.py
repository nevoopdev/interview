def linear_search(list , target):

    n = len(list)-1
    if(n==0): return None

    for i in range(0,n):
        if list[i] == target:
            return i
    return None

alist = [1,2,4,5,6,7,8,9]
target = 2
result = linear_search(alist,target)
if(result != None):
    print("target is found at index of  %d" %result)
else:
    print("target is not found in list")

print(356/10)