import tkinter as tk

todos_list = {}
root = tk.Tk()
root.geometry("700x700")
root.title("TODO App")

def update_todos_list():
    todos_str = ""
    keys = list(todos_list.keys())
    values = list(todos_list.values())
    for i in range(len(keys)):
        todos_str += f"{i}) {keys[i]} --> {values[i]} \n\n"
    todos.set(todos_str)

def addtodo():
    at = tk.Tk()
    at.geometry("700x700")
    at.title("Add Todo")
    def atodo():
        todo = ate.get()
        status = atse.get()
        global todos_list
        todos_list[todo] = status
        at.destroy()
        update_todos_list()
    atl = tk.Label(at,text="Enter The Todo :- ",font=("serif",25,"bold"))
    atl.pack(pady=10)
    ate = tk.Entry(at,font=("serif",25,"italic"))
    ate.pack(pady=10)
    ats = tk.Label(at, text="Enter The Status of the Todo :- ", font=("serif", 25, "bold"))
    ats.pack(pady=10)
    atse = tk.Entry(at, font=("serif", 25, "italic"))
    atse.pack(pady=10)
    atb = tk.Button(at,text="Add Todo",font=("Times New Roman",25,"bold"),cursor="hand2",activebackground="black",activeforeground="white",command=atodo)
    atb.pack(pady=10)
    at.mainloop()

def updatetodo():
    ut = tk.Tk()
    ut.geometry("700x700")
    ut.title("Add Todo")
    def utodo():
        todo = int(ate.get())
        status = atse.get()
        global todos_list
        keys = list(todos_list.keys())
        todos_list[keys[todo]] = status
        ut.destroy()
        update_todos_list()
    atl = tk.Label(ut,text="Enter The Todo Number :- ",font=("serif",25,"bold"))
    atl.pack(pady=10)
    ate = tk.Entry(ut,font=("serif",25,"italic"))
    ate.pack(pady=10)
    ats = tk.Label(ut, text="Enter The Status of the Todo :- ", font=("serif", 25, "bold"))
    ats.pack(pady=10)
    atse = tk.Entry(ut, font=("serif", 25, "italic"))
    atse.pack(pady=10)
    atb = tk.Button(ut,text="Update Todo",font=("Times New Roman",25,"bold"),cursor="hand2",activebackground="black",activeforeground="white",command=utodo)
    atb.pack(pady=10)
    ut.mainloop()

todos = tk.StringVar()
update_todos_list()

tb = tk.Button(root,text="Add a Todo",font=("monospace",25,"bold"),cursor="hand2",activeforeground="white",activebackground="black",command=addtodo)
tb.pack(pady=10)
ub = tk.Button(root,text="Update a Todo",font=("monospace",25,"bold"),cursor="hand2",activeforeground="white",activebackground="black",command=updatetodo)
ub.pack(pady=10)
tl = tk.Label(root,text="TODOS :- ",font=("Ink Free",20,"bold"))
tl.pack(pady=10)
tlist = tk.Label(root,textvariable=todos,font=("Arial",20,"bold"))
tlist.pack(pady=10)

root.mainloop()