import tkinter 
import random
window = tkinter.Tk()
window.title("Hello Little Toddler")
number = 10
equation = 20
score = 0
def dene(*args):
    global number,equation,stringvar,score
    if equation - number == int(entry.get()):
        window.after(900,lambda:entry.delete(0,tkinter.END))
        number = random.randint(0,200)
        equation = random.randint(number,200)
        label1.config(text=str(number))
        label.config(text=str(equation))
        score += 1
        label4.config(text="Score: "+str(score))
stringvar = tkinter.StringVar()
stringvar.trace_add("write",dene)
label1 = tkinter.Label(window, text=str(number))
label1.grid(column=0,row=0)
label2 = tkinter.Label(window, text="+")
label2.grid(column=1,row=0)
entry = tkinter.Entry(window,textvariable=stringvar)
entry.grid(column=2,row=0)
label3 = tkinter.Label(window,text="=")
label3.grid(column=3,row=0)
label = tkinter.Label(window, text=str(equation))
label.grid(column=4,row=0)
label4 = tkinter.Label(window,text=f"Your Score is {score}")
label4.grid(column=2,row=1)
window.mainloop()
