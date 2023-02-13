import time
import sys
MAX_SIZE = sys.maxsize

def selection_sort(data, drawData, timeTick):
    swapCount = 0
    for i in range(len(data)-1):
        pos = i
        last = MAX_SIZE
        for j in range(i+1, len(data)):
            drawData(data, [('#F8FF41' if x == j else ('#41CFFF' if x == i else '#575E64')) for x in range(len(data))], swapCount)
            time.sleep(timeTick)

            if data[j] < data[i] and data[j] < last:
                pos = j
                last = data[j]

        drawData(data, [('#2EFF4F' if x == pos else ('#41CFFF' if x == i else '#575E64')) for x in range(len(data))], swapCount)
        time.sleep(timeTick)
        temp = data[i]
        data[i] = data[pos]
        data[pos] = temp
        swapCount += 1

    drawData(data, ['#5DFF41' for x in range(len(data))], swapCount)

info_SelectionSort='''DESCRIPTION:
Selection Sort is an iterative and in-place sorting algorithm that divides the data structure in two sublists: the ordered one, and 
the unordered one. The algorithm loops for all the elements of the data structure and for every cycle picks the smallest element of 
the unordered sublist and adds it to the sorted sublist, progressively filling it.

It's a really simple and intuitive algorithm that does not require additional memory, but it's not really efficient on big data 
structures due to its quadratic time complexity.

COMPLEXITY:
Average Complexity	O(n^2)
Best Case	O(n^2)
Worst Case	O(n^2)
Space Complexity	O(1)

STABILITY: NO

TYPE: QUADRATIC

MORE INFO: https://www.geeksforgeeks.org/selection-sort/
'''