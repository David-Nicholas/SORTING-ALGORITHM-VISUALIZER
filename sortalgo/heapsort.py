import time
colordata = []  
swapCount = 0

def heapify(data, n, i, drawData, timeTick):
    global swapCount
    largest = i
    l = 2*i
    r = 2*i + 1

    if l < n and data[largest] < data[l]:
        largest = l

    if r < n and data[largest] < data[r]:
        largest = r
        
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        swapCount += 1
        drawData(data, ['#41CFFF' if x == i or x == largest else colordata[x] for x in range(len(data))], swapCount)
        time.sleep(timeTick)

        heapify(data, n, largest, drawData, timeTick)


def heap_sort(data, drawData, timeTick):
    global colordata
    global swapCount
    swapCount = 0
    colordata = ['#575E64' for x in range(len(data))]

    n = len(data)
    for i in range(n//2 - 1, -1, -1):
        heapify(data, n, i, drawData, timeTick)
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        swapCount += 1
        swapCount += 1
        drawData(data, ['#F8FF41' if x == i or x == 0 else colordata[x] for x in range(len(data))], swapCount)
        time.sleep(timeTick)

        heapify(data, i, 0, drawData, timeTick)

    drawData(data, ['#5DFF41' for x in range(len(data))], swapCount)

info_HeapSort ='''DESCRIPTION:
Heap Sort is an in-place iterative sorting algorithm based on auxiliary data structures called heap. It's less efficient than 
algorithm with the same time complexity and it's not suitable for data structures with few elements.

The heap is a data structure representable as a binary tree, where each node has a value bigger or equal to its children. 
Consequently, the root will hold the maximum value.

COMPLEXITY:
Average Complexity	O(n × log n)
Best Case	         O(n × log n)
Worst Case	        O(n × log n)
Space Complexity	  O(1)

STABILITY: NO

TYPE: LOGARITHMIC

MORE INFO: https://www.geeksforgeeks.org/heap-sort/
'''