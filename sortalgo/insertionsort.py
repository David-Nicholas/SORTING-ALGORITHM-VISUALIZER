import time

def insertion_sort(data, drawData, timeTick):
    swapCount = 0
    for i in range(1,len(data)):
        value = data[i]
        j = i
        while value <= data[j-1] and j != 0:
            drawData(data, ['#2EFF4F' if x == j else '#575E64' for x in range(len(data))], swapCount)
            time.sleep(timeTick)

            data[j],data[j-1] = data[j-1],data[j]
            swapCount += 1
            j -= 1

        drawData(data, ['#2EFF4F' if x == j else '#575E64' for x in range(len(data))], swapCount)
        time.sleep(timeTick)
    drawData(data, ['#5DFF41' for x in range(len(data))], swapCount)

info_InsertionSort ='''DESCRIPTION:
Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It's less performant than advanced
sorting algorithms, but it can still have some advantages: it's really easy to implement and it's efficient on small data structures 
almost sorted.

The algorithm divides the data structure in two sublists: a sorted one, and one still to sort. Initially, the sorted sublist is made 
up of just one element and it gets progressively filled. For every iteration, the algorithm picks an element on the unsorted sublist 
and inserts it at the right place in the sorted sublist.

COMPLEXITY:
Average Complexity	O(n^2)
Best Case	         O(n)
Worst Case	        O(n^2)
Space Complexity	  O(1)

STABILITY: YES

TYPE: QUADRATIC

MORE INFO: https://www.geeksforgeeks.org/insertion-sort/
'''