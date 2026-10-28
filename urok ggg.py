import tkinter as tk
root = tk.Tk()
root.title("Simple windows")
root.geometry("1280x1024+500+200") #розмір вікна
root.iconbitmap("bomb.ico")#вибір іконки :))
#root.resizable (False, False) неможно міняти розмір
root.minsize(800, 600)
root.maxsize(1920, 1080)
label_1 = tk.Label(text = "a", font = ("cosmic sans", 30 , "bold"), bg = "black",fg = "white",   width=50,
        height=3, padx = 5, pady = 5, anchor = "n", #n - угору, s - вниз, w - зліва, e - право
relief = "ridge", bd = 20         )

label_1.pack()
label_1.pack()
root.mainloop()