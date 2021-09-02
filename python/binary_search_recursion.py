def binary_search (list,target):
    if len(list) == 1 : 
        return False
    
    mid = len(list)//2

    if list[mid] == target:
        return True
    else:
        if list[mid] < target:
            return binary_search(list[mid+1:],target) 
        else:
            return binary_search(list[:mid],target)

alist = [1,2,3,4,5,6,7,8]
target = 133
result = binary_search(alist,target)
if(result):
    print("target is found in list")
else:
    print("target is not found in list")
