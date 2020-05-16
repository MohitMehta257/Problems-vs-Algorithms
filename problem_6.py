
import random

def mergesort(items):


    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged[0],merged[len(merged)-1]

def get_min_max(ints):
    tup=()
    result=mergesort(ints)
    tup.append(result[0])
    tup.append(result[1])
    return tup




s=[1,2,5,6,9,7,2,5,10,11]

print(mergesort(s))    #returns (1,11)
