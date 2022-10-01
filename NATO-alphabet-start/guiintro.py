import tkinter



window= tkinter.Tk()
window.title("my first Gui")
window.minsize(width=500,height=300)
mylable=tkinter.Label(text="ohh m g", font=("arial",24,"bold"))
mylable.config(text="click the button")
mylable.pack()
band=False


def buttonClick():

    print("click bet activated")
    mylable.config(text=et.get())
    mybutton.destroy()
    et.destroy()
    print(tx.get(1.0 ,tkinter.END))



mybutton=tkinter.Button(text="click here!", command=buttonClick)
mybutton.pack()

et=tkinter.Entry(width=10)
et.pack()

tx=tkinter.Text(width=20,height=10)
tx.pack()
def bango():
    print(sbox.get())
sbox=tkinter.Spinbox(from_=10 , to=20,width=10, command=bango)
sbox.pack()
def bangow(value):
    print(value)
sboxw=tkinter.Scale(from_=10 , to=20,width=10, command=bangow)
sboxw.pack()

def chango():
    print(ckstat.get())
ckstat=tkinter.IntVar()
ck=tkinter.Checkbutton(command=chango,text="ho ki nahi",variable=ckstat)
ck.pack()

def pango():
    print(rad.get())
rad=tkinter.IntVar()
rad1=tkinter.Radiobutton(variable=rad , text="ho", value=1, command=pango)
rad2=tkinter.Radiobutton(variable=rad , text="nffdsfahi", value=2, command=pango)
rad1.pack()
rad2.pack()
window.mainloop()
