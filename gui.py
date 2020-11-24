from tkinter import *
from barchart import BarChart
from numpy import *
from algorithms import Algorithms

# CONFIGURATION
root = Tk()
root.title("Videc - Tot | NPUP")
root.state('zoomed')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.protocol("WM_DELETE_WINDOW", root.quit)
top_frame = Frame(root)
top_frame.pack()
middle_frame = Frame(root)
middle_frame.pack(side=BOTTOM)
bottom_frame = Frame(middle_frame)
bottom_frame.pack(side=BOTTOM)
btn = Button(bottom_frame, text="Start", command=lambda: click(btn), font=('Helvetica', '16'), padx=5)
btn["state"] = "disabled"
btn.pack(side=LEFT)
reset_btn = Button(bottom_frame, text="Reset", command=lambda: reset(btn), font=('Helvetica', '16'), padx=5)
reset_btn["state"] = "disabled"
reset_btn.pack(side=LEFT)

# CONSTANTS
low = 1
high = 100

# GLOBAL VARIABLES
algorithms_showing = []
counter = 0
n = 0


def ping_callback_after_sort_finished():
    global counter
    counter = counter + 1
    if counter == len(algorithms_showing):
        btn.configure(text="Start")
        reset_btn["state"] = "active"
        counter = 0


def click(btn):
    if btn['text'] == "Start":
        for barchart in algorithms_showing:
            barchart.start_animation()
        btn.config(text="Stop")
        reset_btn["state"] = "disabled"
    else:
        for barchart in algorithms_showing:
            barchart.stop_animation()
        btn.configure(text="Start")
        reset_btn["state"] = "active"


def reset(btn):
    if btn['text'] == "Start":
        global n
        new_data = random.randint(low, high, n)
        chosen_algorithms = []
        for algorithm_showing in algorithms_showing:
            chosen_algorithms.append(algorithm_showing.algorithm)
            algorithm_showing.pack_forget()
        algorithms_showing.clear()
        for i in range(len(chosen_algorithms)):
            if i < 3:
                barchart = BarChart(chosen_algorithms[i], new_data.copy(), top_frame, ping_callback_after_sort_finished)
            else:
                barchart = BarChart(chosen_algorithms[i], new_data.copy(), middle_frame, ping_callback_after_sort_finished)
            barchart.pack()
            algorithms_showing.append(barchart)


def create(listbox, add_window, e1):
    global n
    n = int(e1.get())
    data = random.randint(low, high, n)
    chosen_algorithms = [listbox.get(i) for i in listbox.curselection()]
    for algorithm_showing in algorithms_showing:
        algorithm_showing.pack_forget()
    algorithms_showing.clear()
    for i in range(len(chosen_algorithms)):
        if i < 3:
            barchart = BarChart(Algorithms.get(chosen_algorithms[i]), data.copy(), top_frame, ping_callback_after_sort_finished)
        else:
            barchart = BarChart(Algorithms.get(chosen_algorithms[i]), data.copy(), middle_frame, ping_callback_after_sort_finished)
        barchart.pack()
        algorithms_showing.append(barchart)
    if len(algorithms_showing) > 0:
        btn["state"] = "active"
        reset_btn["state"] = "active"
    else:
        btn["state"] = "disabled"
        reset_btn["state"] = "disabled"
    add_window.destroy()


def open_add_window():
    add_window = Toplevel(root)
    root.eval(f'tk::PlaceWindow {str(add_window)} center')
    add_window.title("Config")
    add_window.geometry("215x215")
    add_window.resizable(width=False, height=False)
    add_window.grab_set()
    l = Listbox(add_window, selectmode="multiple")
    Label(add_window, text="Choose sorts").grid(row=1, sticky=N)
    l.grid(row=1, column=1)
    x = [e.value for e in Algorithms]
    for each_item in range(len(x)):
        l.insert(END, x[each_item])
    e1 = Entry(add_window)
    e1.insert(0, 10)
    add_button = Button(add_window, text="Create", command=lambda: create(l, add_window, e1))
    Label(add_window, text="Array size").grid(row=0)
    e1.grid(row=0, column=1)
    add_button.grid(row=2, columnspan=2)


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Configure", command=open_add_window)
menubar.add_cascade(label="Options", menu=filemenu)
root.config(menu=menubar)
root.mainloop()




