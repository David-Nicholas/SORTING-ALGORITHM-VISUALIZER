import time
swapCount = 0

def merge_sort(data, drawData, timeTick):
    global swapCount
    swapCount = 0
    merge_sort_alg(data, 0, len(data)-1, drawData, timeTick)

    drawData(data, ['#5DFF41' for x in range(len(data))],swapCount)
    time.sleep(timeTick)

def merge_sort_alg(data, left, right, drawData, timeTick):
    if left >= right:
        return
    middle = (left + right)//2

    merge_sort_alg(data, left, middle, drawData, timeTick)
    merge_sort_alg(data, middle+1, right, drawData, timeTick)
    merge(data, left, middle, right, drawData, timeTick)

def merge(data, left, middle, right, drawData, timeTick):
    global swapCount
    drawData(data, ['#575E64' for x in range(len(data))], swapCount)
    time.sleep(timeTick)

    leftPart = data[left:middle+1]
    rightPart = data[middle+1:right+1]
    
    leftIdx, rightIdx = 0,0

    for i in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[i] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[i] = rightPart[rightIdx]
                rightIdx += 1
        elif leftIdx < len(leftPart):
            data[i] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[i] = rightPart[rightIdx]
            rightIdx += 1
        swapCount += 1
        drawData(data, ['#41CFFF' if x == i else '#575E64' for x in range(len(data))], swapCount)
        time.sleep(timeTick)

info_MergeSort='''DESCRIPTION:
Merge Sort is a sorting algorithm based on the Divide et Impera technique, like Quick Sort. It can be implemented iteratively or 
recursively, using the Top-Down and Bottom-Up algorithms respectively. We represented the first one.

The algorithm divides the data structure recursively until the subsequences contain only one element. At this point, the subsequences 
get merged and ordered sequentially. To do so, the algorithm progressively builds the sorted sublist by adding each time the minimum 
element of the next two unsorted subsequences until there is only one sublist remaining. This will be the sorted data structure.

COMPLEXITY:
Average Complexity	O(n × log n)
Best Case	         O(n × log n)
Worst Case	        O(n × log n)
Space Complexity	  O(n)

STABILITY: YES

TYPE: LOGARITHMIC

MORE INFO: https://www.geeksforgeeks.org/merge-sort/
'''