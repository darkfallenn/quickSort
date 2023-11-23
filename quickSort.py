# Quicksort sorts an array of elements by separating them based on a pivot element (greater than or less than pivot). The separated
# halves are then sorted recursively and stored as a varaible. Finally, we return the sorted halves with the pivot in the middle.


def quickSort(arr):
    if len(arr) < 2: # If the array has one or zero elements, it's already sorted.
        return arr
    
    pivot = arr[-1] # Make any element a pivot
    less_than_pivot = [] 
    greater_than_pivot = [] 
    
    for item in arr[:-1]: # Iterate over everything except the pivot.
        if item < pivot: 
            less_than_pivot.append(item)
        else:
            greater_than_pivot.append(item) # Separates the elements according to pivot.
            
    less_than_sorted = quickSort(less_than_pivot)
    greater_than_sorted = quickSort(greater_than_pivot) # Recursively sort the two split halves and store them.
    
    return less_than_sorted + [pivot] + greater_than_sorted # The pivot will be in between the elements less than it and the elements greater than it. 