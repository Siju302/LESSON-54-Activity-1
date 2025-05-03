from tkinter import *

window = Tk()
window.title('Tkinter Sample Window')
window.geometry('300x300')

greeting = Label(text="Hi User", fg='lightblue', bg='darkblue')
button = Button(text="Click Me!", bg='lightblue', fg='darkblue')
entry = Entry(fg="red", bg="palevioletred", width=50)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=window, text='Sample Frame')
label.pack()

textbox =  Text(fg='palevioletred', bg='pink')
textbox.pack()
window.mainloop()