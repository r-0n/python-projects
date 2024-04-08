
def merge_sort(list):
    """
    sorts a list in ascending order
    returns a new sorted list

    divide: find the midpoint of the list and divide 
    into sublist

    conquer: recursively sort the sublist created 
    in the previous step

    combine: merge the sorted sublist created in the
    previous step

    time complexity: nlog(n)
    """

    
    if len(list)<=1: #base-case
        return list
    

    left_half, right_half = split(list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(list):
    """divide the unsorted list into sublist
    returns two sublists: left and right
    takes O(logn) time"""

    mid= len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left,right

def merge(left,right):

    """merges two lists sorting them in the process
    returns a new merged list
    
    runs in overall O(n) time"""

    l= []
    i=0
    j =0

    while i<len(left) and j < len(right):
        if left[i]<right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
    
    while i<len(left):
        l.append(left[i])
        i+=1

    while j<len(right):
        l.append(right[j])
        j+=1

    return l


def verify_sorted(list):
    n = len(list)
    if n==0 or n ==1:
        return True
    
    return list[0]< list[1] and verify_sorted(list[1:])



roro_list= [56,3,45,24,36,1,7,4,5,20]

l = merge_sort(roro_list)

print(verify_sorted(roro_list))
print(verify_sorted(l))