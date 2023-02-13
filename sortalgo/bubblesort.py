import time

def bubble_sort(data, drawData, timeTick):
    swapCount = 0
    for _ in range(len(data)-1):
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapCount += 1
                drawData(data, ['#2EFF4F' if x == i or x == i+1 else '#575E64' for x in range(len(data))], swapCount)
                time.sleep(timeTick)
    drawData(data, ['#5DFF41' for x in range(len(data))], swapCount)

info_BubbleSort='''DESCRIPTION:
Bubble Sort is an iterative sorting algorithm that imitates the movement of bubbles in sparkling water. The bubbles represents the 
elements of the data structure.

The bigger bubbles reach the top faster than smaller bubbles, and this algorithm works in the same way. It iterates through the data 
structure and for each cycle compares the current element with the next one, swapping them if they are in the wrong order.

COMPLEXITY:
Average Complexity	O(n^2)
Best Case	         O(n)
Worst Case	        O(n^2)
Space Complexity	  O(1)

STABILITY: YES

TYPE: QUADRATIC

MORE INFO: https://www.geeksforgeeks.org/bubble-sort/
'''