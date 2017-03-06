from Tkinter import *
import tkMessageBox

def process():
    # tkMessageBox.showinfo("Results", JD.get())
    Label(app, text='{0}'.format(txt.get()), width=4, height=4, font=("Calibri",13)).grid(row=3, column= 0, sticky=SW)
    print "asd"

root = Tk()
root.title('Profile Recommender')
root.wm_state('zoomed')

app = Frame(root)
app.pack()

text = None

Label(app, text=' ', font=("Calibri",16)).grid(row=1, column=0, sticky=NW)
Label(app, text='Job Description          ', font=("Calibri -weight bold", 16)).grid(row=2, column=0, sticky=NW)
Label(app, text='', width=7, font=("Calibri",16)).grid(row=2, column=3, sticky=NW)

txt = StringVar()
Entry(app, textvariable=txt, width=60, font=("Calibri light",16)).grid(row=2, column=1, sticky=NE)

Button(app, text='Search', command=process, width=10, font=("Calibri -weight bold", 14)).grid(row=2, column=4, sticky=SE)

root.mainloop()