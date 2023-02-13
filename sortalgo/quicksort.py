import time
swapCount = 0
colordata = []

def partition(data,low,high, drawData, timeTick):
    global swapCount
    i = ( low-1 )
    pivot = data[high]
    for j in range(low , high):
        if data[j] <= pivot:
            i = i+1
            data[i],data[j] = data[j],data[i]
            swapCount += 1

        for x in range(len(colordata)):
            if x == i:
                colordata[x] = '#FF4444'
            elif i < x < high:
                colordata[x] = '#F8FF41'
            elif x == high:
                colordata[x] = '#41CFFF'
            else:
                colordata[x] = '#575E64'

        drawData(data, colordata, swapCount)
        time.sleep(timeTick)

    data[i+1],data[high] = data[high],data[i+1]
    swapCount += 1
    return ( i+1 )

def quickSort(data,low,high, drawData, timeTick):
    if low < high:
        pi = partition(data,low,high, drawData, timeTick)
        quickSort(data, low, pi-1, drawData, timeTick)
        quickSort(data, pi+1, high, drawData, timeTick)

def quick_sort(data, drawData, timeTick):
    global swapCount
    swapCount = 0
    global colordata
    colordata = ['#575E64' for x in range(len(data))]
    quickSort(data, 0, len(data)-1, drawData, timeTick)
    drawData(data, ['#5DFF41' for x in range(len(data))], swapCount)

info_QuickSort = '''DESCRIPTION:
Quick Sort is a sorting algorithm based on splitting the data structure in smaller partitions and sort them recursively until the 
data structure is sorted.

This division in partitions is done based on an element, called pivot: all the elements bigger than the pivot get placed on the right 
side of the structure, the smaller ones to the left, creating two partitions. Next, this procedure gets applied recursively to the 
two partitions and so on.

COMPLEXITY:
Average Complexity	O(n × log n)
Best Case	         O(n × log n)
Worst Case	        O(n^2)
Space Complexity	  O(n)

STABILITY: NO

TYPE: LOGARITHMIC

MORE INFO: https://www.geeksforgeeks.org/quick-sort/
'''