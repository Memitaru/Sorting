# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        # loops over i to the length checking to see if each element is smaller than the current smallest
        # If j is smaller than the current smallest number, set smallest_index to the j (index of smallest)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap

        # Stores the number at current index
        # Moves the smallest number to the current index
        # Moves the number from storage to where the smallest number used to be
        swap = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = swap

    return arr


# TO-DO:  implement the Bubble Sort function below

# Bubble sort: checks two numbers against each other and puts them in the right order repeatedly until they are in order

def bubble_sort( arr ):
    # the first loop goes len(arr) times. Inner loop will loop based on i for the bubbling.
    for i in range(len(arr)):
        for j in range(0, (len(arr)-i-1)):
            # compare and swap if needed
            if arr[j] > arr[j+1]:
                store = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = store

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr