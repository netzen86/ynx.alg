def inplaceqs(array, a, b):
    def swapElements(array, a, b):
        tmp = array[a]
        array[a] = array[b]
        array[b] = tmp
    if a >= b:
        print('the end') 
        return 'return the end'
    pivot = array[b] # select last element as pivot
    left = a
    right = b - 1
    while left <= right:
        while left <= right and array[left] <= pivot:  # find an element larger than the pivot
            left += 1   
        while left <= right and array[right] >= pivot: # find an element larger than the pivot
            right -= 1  
        if left < right: 
            swapElements(array, left, right)
    swapElements(array, left, b) # put the pivot its final place
    #recursice calls
    inplaceqs(array, a, left-1) 
    inplaceqs(array, left+1, b)

### Test
arr = [19,13,1,5,3,4,111,34,141,22,78,23,55]
print(inplaceqs(arr, 0, 12))
print(arr)
