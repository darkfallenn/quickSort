# This method of sorting involves the splitting of elements based on a pivot element.
# The split halves are then sorted recursively, with the final result putting the pivot
# in it's final sorted position.

def quickSort(arr):
    if len(arr) < 2: # If the array has one or zero elements, it's already sorted.
        return arr
    
    pivot = arr[-1] # Make any element a pivot, preferably the right most element.
    less_than_pivot = [] # For elements less than pivot.
    greater_than_pivot = [] # For elements greater than pivot.
    
    for item in arr[:-1]: # Iterate over everything except the pivot.
        if item < pivot: 
            less_than_pivot.append(item)
        else:
            greater_than_pivot.append(item) # Separates the elements according to pivot.
    
    # Recursively sort the two split halves.
            
    less_than_sorted = quickSort(less_than_pivot)
    greater_than_sorted = quickSort(greater_than_pivot)
    
    # Final sorted position:
    # The pivot will be after the elements less than it, and before the elements greater than it.
    
    return less_than_sorted + [pivot] + greater_than_sorted