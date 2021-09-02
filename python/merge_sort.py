# MERGE SORT USING RECURSION


def mergesort(arr):
    #IF LENGTH OF AN ARRAY IS LESSER OR EQUAL TO 1 RETURN THE LIST
    if len(arr) <= 1:
        return arr
    
    #finding mid point of an array
    mid = len(arr)//2
    
    #findind left and right using recursion 
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    
    #defining empty array to add sorted values
    sorted= []
    
    #i - index of left , j- index 0f right
    i=0
    j=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j+=1
    sorted += left[i:]
    sorted += right[j:]
    return sorted
print(mergesort([24,56,100,1,2,3,4]))

