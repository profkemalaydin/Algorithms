#Bubblesort

def bubblesort(values):
    # Repeat until the array is sorted.
    not_sorted = True
    while (not_sorted):
        # Assume we won't find a pair to swap.
        not_sorted = False
        # Search the array for adjacent items that are out of order.
        for i in range(len(values)):
            # See if items i and i - 1 are out of order.
            if (values[i] < values[i - 1]):
                # Swap them.
                temp = values[i]
                values[i] = values[i - 1]
                values[i - 1] = temp
                # The array isn't sorted after all.
                not_sorted = True
    return values
    
print(bubblesort([1,3,2,6,4,7,5]))