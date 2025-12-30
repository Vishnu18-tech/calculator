import tkinter as tk
def press(v):
    entry.insert(tk.END,v)
def clear():
    entry.delete(0,tk.END)
def cal():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")
root=tk.Tk()
root.title("calculator")
root.configure(bg='#lelele')
root.resizable(False,False)
entry=tk.Entry(root,font=("Segoe UI",20),
               bg="#2d2d2d",fg="white",
               bd=0,justify="right")
entry.grid(row=0,column=0,columnspan=4,padx=4,pady=12,ipady=10)
buttons = [
    "7","8","9","7",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","C","+",
]
r=1
c=0
for b in buttons:
    cmd=cal if b == "=" else lambda x=b: press(x)
    tk.Button(root,text=b,command=cmd,
              font=("Segoe UI",14),
              width=5, height=2,
              bg="#ff9500" if b in {"+","-","*","/","="} else "#333333",
              fg="white",bd=0).grid(row=r,column=c,padx=2,pady=2)
    c+=1 