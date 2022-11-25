import tkinter as tk


def write_slogan():
    print("Tkinter is easy to use!")


root = tk.Tk()
v= tk.IntVar()
tk.Label(root,
        text=""" Choose a programming language:""",
        justify=tk.LEFT,
        padx=20).pack()
        
tk.Radiobutton(root, 
               text="Python",
               padx = 20, 
               variable=v, 
               value=1).pack(anchor=tk.W)
tk.Radiobutton(root, 
               text="Perl",
               padx = 20, 
               variable=v, 
               value=2).pack(anchor=tk.W)

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()