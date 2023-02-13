import time

def shell_sort(data, drawData, timetick):
    swapCount = 0
    n = len(data)
    interval = n//2
    while interval > 0:
        for i in range(interval, n):
            temp = data[i]
            j = i
            while j >= interval and data[j-interval] > temp:
                drawData(data, ['#F8FF41' if x == j or x == j-interval else '#575E64' for x in range(n)], swapCount)
                time.sleep(timetick)
                data[j] = data[j-interval]
                swapCount += 1
                j -= interval

            drawData(data, ['#F8FF41' if x == j else '#575E64' for x in range(n)], swapCount)
            time.sleep(timetick)
            data[j] = temp
        interval //= 2
    drawData(data, ['#5DFF41' for x in range(n)], swapCount)

info_ShellSort='''DESCRIPTION:
Shell Sort is one of the oldest sorting algorithms and it's an extension of the Insertion Sort. This algorithm is fast and easy to 
implement, but it's hard to measure its performances.

Unlike Insertion Sort, Shell Sort starts by comparing the elements distant from each other by a certain gap that gets progressively 
decreased. By starting with the most distant elements, it can optimize performances as it's not limited by just comparing two adjacent
elements.

COMPLEXITY:
Average Complexity	O(n^1.25)  O(n × log n)
Best Case	         O(n × log n)
Worst Case	        O(n^2)
Space Complexity	  O(1)

STABILITY: NO

TYPE: WEIRD

MORE INFO: https://www.geeksforgeeks.org/shellsort/
'''