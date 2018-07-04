def sequentialSearch(alist, item):
	pos = 0
	found = False # Flags

	while pos < len(alist) and not found:
	    if alist[pos] == item:
	        found = True
	    else:
	        pos = pos+1
	
	return found
	
testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
#print(sequentialSearch(testlist, 3))
#print(sequentialSearch(testlist, 13))

"""
def binarySearch(alist, item):
	first = 0
	last = len(alist)-1
	found = False
	
	while first<=last and not found:
	    midpoint = (first + last)//2
	    if alist[midpoint] == item:
	        found = True
	    else:
	        if item < alist[midpoint]:
	            last = midpoint-1
	        else:
	            first = midpoint+1
	
	return found
also_list = sorted([1, 2, 32, 8, 17, 19, 42, 13, 0])
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

#print(binarySearch(also_list, 13))
"""
def bubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

################################################

""" July 3rd HW solutions"""

class Stack:
    def __init__(self):
        self.items = []
        

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        # Stack.push()

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1] # 

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []
        

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1] # 

    def size(self):
        return len(self.items)


