from tkinter import *
from tkinter import ttk 
import random
from sortalgo.bubblesort import bubble_sort
from sortalgo.selectionsort import selection_sort
from sortalgo.insertionsort import insertion_sort
from sortalgo.mergesort import merge_sort
from sortalgo.quicksort import quick_sort
from sortalgo.heapsort import heap_sort
from sortalgo.shellsort import shell_sort
from sortalgo.stoogesort import stooge_sort
from sortalgo.quicksort import info_QuickSort
from sortalgo.bubblesort import info_BubbleSort
from sortalgo.mergesort import info_MergeSort
from sortalgo.selectionsort import info_SelectionSort
from sortalgo.insertionsort import info_InsertionSort
from sortalgo.heapsort import info_HeapSort
from sortalgo.shellsort import info_ShellSort
from sortalgo.stoogesort import info_StoogeSort

def DrawData(data,colorArray,swCount):
    canvas.delete('all')
    canvas_height= 450
    canvas_width= 1070
    x_width=  canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_rect = 10
    normalised_data = [i/ max(data) for i in data]

    for i, height in enumerate(normalised_data):
        x0 = i * x_width + offset + spacing_bet_rect
        y0 = canvas_height - height * 400

        x1 = (i+1) * x_width
        y1 = canvas_height
 
        if (i < len(colorArray)):
            canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        else:
            canvas.create_rectangle(x0,y0,x1,y1,fill= "#0078D7")
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    swap_count_label = Label(canvas,text = 'Swap Count: '+str(swCount),font= ("Arial", 12), bg= "#B4B4B4", fg = "#000000", width= 15)
    swap_count_label.place(x= 934, y= 4)

    root.update_idletasks()  

def Generate():
    global data

    minvalue = int(min_value_scale.get())
    maxvalue = int(max_value_scale.get())
    sizevalue = int(size_value_scale.get())
    
    data = []

    for _ in range(sizevalue):
        data.append(random.randrange(minvalue, maxvalue  + 1))
    swapCount = 0
    DrawData(data, ["#494945" for x in range(len(data))], swapCount)

def Start():
    global data
    if not data:
        return 
    if algorithm_combobox.get() == 'Quick Sort':
        quick_sort(data, DrawData, speed_scale.get())
    elif algorithm_combobox.get() == 'Bubble Sort':
        bubble_sort(data, DrawData, speed_scale.get())
    elif algorithm_combobox.get() == 'Merge Sort':
        merge_sort(data, DrawData, speed_scale.get())
    elif algorithm_combobox.get() == 'Selection Sort':
        selection_sort(data, DrawData, speed_scale.get())
    elif algorithm_combobox.get() == 'Heap Sort':
        heap_sort(data, DrawData, speed_scale.get())
    elif algorithm_combobox.get() == 'Insertion Sort':
        insertion_sort(data, DrawData, speed_scale.get())
    elif algorithm_combobox.get() == 'Shell Sort':
        shell_sort(data, DrawData, speed_scale.get())
    elif algorithm_combobox.get() == 'Stooge Sort':
        stooge_sort(data, DrawData, speed_scale.get())

def Info():
    rootInfo= Tk()
    rootInfo.title('INFO')
    rootInfo.wm_iconbitmap('images/INFO.ico')
    rootInfo.geometry('1100x600+200+80')
    rootInfo.config(bg="#FFFFFF")

    text = Text(rootInfo, width= 134, height= 36, bg = "#808080")
    text.place(x= 12, y= 12)

    if algorithm_combobox.get() == 'Quick Sort':
        text.pack(expand=True)
        text.insert('end', info_QuickSort)
        text.config(state='disabled')
    elif algorithm_combobox.get() == 'Bubble Sort':
        text.pack(expand=True)
        text.insert('end', info_BubbleSort)
        text.config(state='disabled')
    elif algorithm_combobox.get() == 'Merge Sort':
        text.pack(expand=True)
        text.insert('end', info_MergeSort)
        text.config(state='disabled')
    elif algorithm_combobox.get() == 'Selection Sort':
        text.pack(expand=True)
        text.insert('end', info_SelectionSort)
        text.config(state='disabled')
    elif algorithm_combobox.get() == 'Heap Sort':
        text.pack(expand=True)
        text.insert('end', info_HeapSort)
        text.config(state='disabled')
    elif algorithm_combobox.get() == 'Insertion Sort':
        text.pack(expand=True)
        text.insert('end', info_InsertionSort)
        text.config(state='disabled')
    elif algorithm_combobox.get() == 'Shell Sort':
        text.pack(expand=True)
        text.insert('end', info_ShellSort)
        text.config(state='disabled')
    elif algorithm_combobox.get() == 'Stooge Sort':
        text.pack(expand=True)
        text.insert('end', info_StoogeSort)
        text.config(state='disabled')
    rootInfo.mainloop()


root= Tk()
root.title('SORTING ALGORITHM VISUALIZER')
root.wm_iconbitmap('images/SAV.ico')
root.geometry('1100x600+200+80')
root.config(bg="#FFFFFF")

selected_algorithm = StringVar()
data = []

main_lable = Label(root, text= "Algorithm:", font= ("Arial", 16), bg= "#B4B4B4", width= 10, fg = "#000000")
main_lable.place(x= 4, y= 4)

algorithm_combobox = ttk.Combobox(root, width= 15, font= ("Arial", 16), state= "readonly",textvariable= selected_algorithm, values=['Bubble Sort','Heap Sort','Insertion Sort','Merge Sort','Quick Sort','Selection Sort','Shell Sort','Stooge Sort']) 
algorithm_combobox.place(x= 145, y= 4)
algorithm_combobox.current(0)

random_generate_button = Button(root, text= "Generate", bg= "#B4B4B4", font= ("Arial", 16), activebackground= "#0078D7", activeforeground= "#000000", command= Generate)
random_generate_button.place(x= 750, y= 20)

start_button = Button(root, text= "Start", bg= "#B4B4B4", font= ("Arial", 16), activebackground= "#0078D7", activeforeground= "#000000", command= Start)
start_button.place(x= 865, y= 20)

start_button = Button(root, text= "Info", bg= "#B4B4B4", font= ("Arial", 16), activebackground= "#0078D7", activeforeground= "#000000", command= Info)
start_button.place(x= 936, y= 20)


speed_scale = Scale(root, label= "Speed [s]:",from_= 0.2, to = 2.0, resolution= 0.2, digits= 2, length=200, orient= HORIZONTAL, font= ("Arial", 16), width= 10)
speed_scale.place(x= 4, y= 40)

size_value_scale = Scale(root, label= "Size:", from_= 5, to = 30, resolution= 1, orient= HORIZONTAL, font= ("Arial", 16), width= 10)
size_value_scale.place(x= 225, y= 40)

min_value_scale = Scale(root, label= "Min:", from_= 1, to = 10, resolution= 1, orient= HORIZONTAL, font= ("Arial", 16), width= 10)
min_value_scale.place(x= 345, y= 40)

max_value_scale = Scale(root, label= "Max:", from_= 10, to = 100, resolution= 1, orient= HORIZONTAL, font= ("Arial", 16), width= 10)
max_value_scale.place(x= 465, y= 40)


canvas = Canvas(root, width= 1075, height= 457, bg = "#808080")
canvas.place(x= 10, y= 130)

root.mainloop()