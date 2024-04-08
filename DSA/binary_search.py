def binary_search(list, target):
    """
    Returns the position of target in the list
    """
    first =0
    last = len(list) -1

    while first<=last:
        midpoint = (first+last)//2

        if list[midpoint] ==target:
            return midpoint
        elif list[midpoint]<target:
            first = midpoint+1
        else: 
            last = midpoint-1

    return None

def verify(index):
    if index is not None:
        print("Target found at index: ",index)
    else:
        print("target not found in list")

numbers = [i for i in range(11)]

result = binary_search(numbers,4)

verify(result)

#time complexity: O(logn)