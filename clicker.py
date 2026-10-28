import tkinter as tk
import datetime

root = tk.Tk()
root.title("Simple Windows")
root.geometry("800x600+200+35")

bomb = 100
score = 0
press_return = True

label = tk.Label(root, text="Press [Enter] to start the game", font=("Arial", 20))
label.pack()

fuse_label = tk.Label(root, text=f"Fuse: {bomb}", font=("Arial", 20))
fuse_label.pack()

score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 20))
score_label.pack()

img_1 = tk.PhotoImage(file="1.gif")
img_2 = tk.PhotoImage(file="2.gif")
img_3 = tk.PhotoImage(file="3.gif")
img_4 = tk.PhotoImage(file="4.gif")

bomb_label = tk.Label(root, image=img_1)
bomb_label.pack()

def update_display():
    fuse_label.config(text=f"Fuse: {bomb}")
    score_label.config(text=f"Score: {score}")

def update_bomb():
    global bomb
    if bomb > 0:
        bomb -= 1
        update_display()
        root.after(1000, update_bomb)
    else:
        label.config(text="BOOM! Game Over")

def update_score():
    global score, bomb
    if bomb > 0:
        score += 1
        bomb += 1
        update_display()

def start(event):
    global press_return
    if press_return:
        press_return = False
        label.config(text="Game Started!")
        update_bomb()

def click():
    update_score()

def press_s(event):
    update_score()

click_button = tk.Button(
    root,
    text="Click me",
    fg="white",
    bg="black",
    width=15,
    font=("Comic Sans MS", 14),
    command=click
)
click_button.pack()

root.bind("<Return>", start)
root.bind("s", press_s)

root.minsize(800, 600)
root.maxsize(1920, 1080)

root.mainloop()