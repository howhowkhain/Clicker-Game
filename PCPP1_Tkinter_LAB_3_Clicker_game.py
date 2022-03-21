"""
LAB

Estimated time
30-45 minutes

Level of difficulty
Medium

Objectives
Learn practical skills related to:

writing event handlers and assigning them to widgets using the bind() method,
managing widgets with the grid manager,
using the after() and after_cancel() methods.
Scenario
We want you to write a simple but challenging game, which can help many people to improve their perception skills and visual memory. We'll call the game The Clicker as clicking is what we expect from the player.

The Clicker's board consists of 25 buttons and each of the buttons contains a random number from range 1..999. Note: each number is different!

Below the board there is a timer which initially shows 0. The timer starts when the user clicks the board for the first time.

Here's how we imagine The Clicker's initial board state:

The Clicker - initial board's state


We expect the player to click all the buttons in the order imposed by the numbers - from the lowest to the highest one. Additional rules say that:

the properly clicked button changes the button's state to DISABLED (it greys the button out)
the improperly clicked button shows no activity,
the timer increases its value every second,
when all the buttons are greyed out (i.e., the player has completed his/her task) the timer stops immediately.
This is how the board looks when the game is finished:

The Clicker - final board's state


Hint: consider using the <Button-1> event instead of setting the command button property - it may simplify your code.

"""


import tkinter as tk
from random import randint
from tkinter import messagebox


# function for closing the application
def game_over():
    if messagebox.showinfo(title="Game Over", message=f"Game Over\nCompletion time: {count_seconds} seconds"):
        window.destroy()


# function for closing the application before game over
def closing_app():
    window.bell()
    if messagebox.askyesno(
            title="Exit!", message="Are you sure you\nwant to exit\nthis beautiful game?"):
        window.destroy()


# function for counting the chronometer seconds
def timer_count():
    global count_seconds, timer_label, id_label
    count_seconds += 1
    timer_label = "Timer: %.2d seconds" % (count_seconds)
    label_variable.set(timer_label)
    id_label = label.after(1000, timer_count)


# function to initialize chronometer
def start_timer():
    global id_label
    if count_seconds == 0:
        id_label = label.after(1000, timer_count)


# callback
def click(button, text):
    global index
    start_timer()
    if text == numbers_list[index]:
        button["state"] = tk.DISABLED
        button["background"] = "#90de00"
        index += 1
    if index == length_button_list:
        label.after_cancel(id_label)
        game_over()


# function used to create buttons
def buttons(row):
    for column in range(5):
        button = tk.Button(window, text=randint(0, 999),
                           width=7, height=2, state=tk.NORMAL, background="#f5f582", font=("Time New Roman", "18", "bold"), activebackground="#90de00", activeforeground="#de2900", borderwidth=3)
        number = button.cget('text')
        while number in numbers_list:
            button["text"] = randint(0, 999)
        numbers_list.append(number)
        object_button_list.append(button)
        button.grid(row=row, column=column)


# declaring different variables
count_seconds = 0
index = 0
id_label = 0
timer_label = "Timer: %.2d seconds" % (count_seconds)
numbers_list = []
object_button_list = []

# create the Main Window
window = tk.Tk(className="The Clicker")
window.title("The Clicker")
window.config(background="#f5f582")
window.geometry("685x550+200+100")
window.resizable(width=False, height=False)

# create buttons with random numbers
all_buttons = [(buttons(row)) for row in range(5)]
# binding click callback to Button-1 event
for button in object_button_list:
    button.bind("<Button-1>", lambda event=None,
                text=button.cget("text"), button=button: click(button, text))

# creat a string type observable variable for label widget
label_variable = tk.StringVar()
label_variable.set(timer_label)

# create a label widget
label = tk.Label(window, textvariable=label_variable,
                 font=("Times New Romans", "20", "bold"), justify="center", background="#f5f582", foreground="#de02bd")
label.grid(row=6, column=0, columnspan=5)

# sorting in ascending order the numbers in the list
numbers_list.sort()
print(numbers_list)

# getting the length of the button list after creation
length_button_list = len(object_button_list)

# update the main window with the latest changes so you can read window geometry info(for debugging purpose only)
# window.update()
# print("width: ", window.winfo_width())
# print("height:", window.winfo_height())

# closing the app before game over
window.protocol("WM_DELETE_WINDOW", closing_app)

# put main window in a continuous loop
window.mainloop()
