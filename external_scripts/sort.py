from random import randint

# Implementing QuickSort to Test Myself lol
def quickSort(list,start,end): # Average runtime: O(nlog(n)), Spatial complexity: O(1), Worst Case: 
	if (start < end): # as long as our starting index is less than our ending one
		pIndex = partition(list,start,end) # Partition the list such that elements less than pivot on left side and elements greater than or equal to pivot on right
		quickSort(list,start,pIndex-1) # Sort the left half
		quickSort(list,pIndex+1,end) # Sort the right half
	else: # Base case, do nothing
		pass

def partition(list,start,end):
	pivot = randint(start,end) # randomly choose a pivot to maximize effecientcy
	list[pivot],list[end] = list[end],list[pivot] # swap selected pivot to the end of the list
	p = int(start) # initialize variable for new pivot index
	for i in range(start,end): # For every element in the list between start and end elements
		if list[i] <= list[end]: # If the element is less than the pivot
			list[i],list[p] = list[p],list[i] # Swap the element with the new pivot location
			p = p + 1 # Increment the new pivot location
	list[p],list[end] = list[end],list[p] # Finally, we return the pivot to it's rightful spot in the list
	return p