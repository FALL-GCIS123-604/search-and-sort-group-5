#Group 5: Activity 3: Layan Zafer and Joudi Alkordi  
"""Importing modules to access their functionalities"""
import random
import time

#Phase 1
def generate_sorted_data(size):
    """Function to perform insertion sort on set of data
       by dividing into sorted and unsorted partitions"""

    small_data = [random.randint(1, 100) for _ in range(size)]
    sorted_array=[] #Creating the sorted partition
    unsorted=small_data #Creating unsorted partition

    while len(unsorted)> 0: #It will stop when there are no more elements in the unsorted partition
        first=unsorted[0] #The first element of the unsorted in every iteration
        unsorted.remove(first) #We remove the first element from the unsorted 
        for i in range(len(sorted_array)):
            if first < sorted_array[i]: #if the value of the first element of unsorted is greater than the current sorted
                sorted_array.insert(i, first) #Insert value of first in place of current one using its index
                break #Exit loop if it has been inserted in correct position
        else:
                sorted_array.append(first) #otherwise if it is not greater than any of the sorted elements, put it at the end
    return sorted_array #return sorted data set

#Phase 2
"""
This function searches for a target value in a sorted array using binary search
"""
def binary_search(array, target):
    left =0                #Start of the search range
    right =len(array) - 1    #End of the search range
    
    #Continue searching while there's a range to check
    while left <= right:
        middle = (left + right) // 2  # Find the middle index of the current array
        
        #If the middle element is the target, return its index
        if array[middle] == target:
            return middle
        #If the target is larger, ignore the left half and change left index
        elif array[middle] < target:
            left = middle + 1
        #If the target is smaller, ignore the right half and change right index
        else:
            right = middle - 1
    
    #Return None if the target is not found in the array
    return None

#Phase 3
def merge_sort(array):
    """Sorts data using merge sort using the divide and conquer strategy
       by dividing based on even and odd indexes and then sorting and merging"""
    if len(array) <= 1: #returns array when theres one or zero element 
        return array
    even_indexes = []
    odd_indexes = []
    for i in range(len(array)):
        if i%2 == 0: #If index is even add it to even indexes
            even_indexes.append(array[i])
        else:
            odd_indexes.append(array[i]) #if index is odd add it to odd indexes
    """Recursive calls to the function to further divide"""
    even_indexes=merge_sort(even_indexes)
    odd_indexes=merge_sort(odd_indexes)
    merged_array=[]
    e = o = 0 #e for even and o for odd
    #Merge sorted parts
    while e < len(even_indexes) and o < len(odd_indexes):
        if even_indexes[e] > odd_indexes[o]: #If even element is greater than odd element
            merged_array.append(odd_indexes[o]) #append odd first
            o += 1
        else: #If odd element is greater than even element
            merged_array.append(even_indexes[e]) #append even first
            e += 1
    #Add remaining elements
    while o < len(odd_indexes): #if there are remaning odd indexes elements
        merged_array.append(odd_indexes[o])
        o += 1
    while e < len(even_indexes): #if there are remaning even indexes elements
        merged_array.append(even_indexes[e])
        e += 1
    return merged_array #return merged-sorted array

#Phase 4
""" 
This function searches for a target value in an array by checking each element one by one
"""
def linear_search(array, target):
    #Loop through every element in the array
    for i in range(len(array)):
        #If we find the target, return its index
        if array[i] == target:
            return i
    #If we reach the end without finding it, return None
    return None

def main():
    """main function"""
    sorted_array = generate_sorted_data(random.randint(1, 100))
    print("Insertion sort result: ", sorted_array)
    large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for _ in range(990)]
    target1=input("Enter target 1 for binary search is: ")
    print("Binary search results for", int(target1), " : ", binary_search(sorted_array, int(target1)) )
    target2=input("Enter target 1 for binary search is: ")
    print("Binary search results for", int(target2), " : ", binary_search(sorted_array, int(target2) ))
    print("Merge sort result: ", (merge_sort(large_data)))
    start1 = time.perf_counter()                    #Record the start time
    linear_result = linear_search(sorted_array, 72) #Perform linear search
    end1 = time.perf_counter()                      # Record the end time
    linear_search_time = end1 - start1              # Calculate the elapsed time
    start2 = time.perf_counter()                    
    binary_result = binary_search(sorted_array, 72) # Perform binary search
    end2 = time.perf_counter()  
    binary_search_time = end2 - start2              # Calculate the elapsed time

    # Print the results for both searches
    print("Linear Search: Target found at index:", linear_result, "Time taken:", linear_search_time, "seconds")
    print("Binary Search: Target found at index:", binary_result, "Time taken:", binary_search_time, "seconds")

main()