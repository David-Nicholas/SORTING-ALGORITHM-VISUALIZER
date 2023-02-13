import time
import math
swapCount = 0

def stooge_sort(data, drawData, timeTick):
    global swapCount
    swapCount = 0
    def stooge_rec(data, i, j):
        global swapCount
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]
            swapCount += 1
            drawData(data, ['#2EFF4F' if x == j or x == i else '#575E64' for x in range(len(data))], swapCount)
            time.sleep(timeTick)
        if (j - i + 1) > 2:
            t = math.floor((j - i + 1) / 3)
            stooge_rec(data, i, j-t)
            stooge_rec(data, i+t, j)
            stooge_rec(data, i, j-t)

    stooge_rec(data, 0, len(data)-1)
    drawData(data, ['#5DFF41' for x in range(len(data))], swapCount)

info_StoogeSort ='''DESCRIPTION:
Stooge Sort is a recursive sorting algorithm, known for its terrible time complexity. It is based on comparisons.

The algorithm first checks the first element of the data structure and the last, swapping them if they are in the 
wrong order. If there are more than 3 elements, it calls itself recursively on the initial 2/3 of the list, on the 
final 2/3 of the list and again on the initial 2/3 of the list, until all the list is sorted.

Its complexity is almost cubic, making it worse than Selection Sort or Insertion Sort.

COMPLEXITY:
Average Complexity O(nlog 3 / log 1.5)   O(n^2.7095...)
Best Case	        O(nlog 3 / log 1.5)  O(n^2.7095...)
Worst Case	       O(nlog 3 / log 1.5)  O(n^2.7095...)
Space Complexity	 O(n)

STABILITY: NO

TYPE: WEIRD

MORE INFO: https://www.geeksforgeeks.org/stooge-sort/
'''