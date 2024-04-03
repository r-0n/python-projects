##Linear search implementation

def linear_search(list,target):
    """
    supposed to Returns the index position of 'target'

    """

    for i in range(0,len(list)):
        if list[i]==target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ",index)
    else:
        print("target not found in list")

numbers = [i for i in range(11)]

result = linear_search(numbers,4)

verify(result)
#time complexity: O(n)