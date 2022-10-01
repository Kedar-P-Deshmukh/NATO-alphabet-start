import tkinter



window= tkinter.Tk()
window.title("Miles to KM converter")
window.minsize(width=300,height=150)
window.config(padx=50)
inp=tkinter.Entry()
mile=tkinter.Label(text="miles", font=("arial",24,"bold"))
km=tkinter.Label(text="KM", font=("arial",24,"bold"))
value=tkinter.Label(text=0, font=("arial",24,"bold"))

inp.grid(column=2,row=0)
mile.grid(column=3,row=0)
km.grid(column=3,row=1)
value.grid(column=2,row=1)


def buttonClick():

    print("click bet activated")
    value.config(text=int(float(inp.get())*1.6))





mybutton=tkinter.Button(text="Convert", command=buttonClick)
mybutton.grid(column=2,row=2)

window.mainloop()