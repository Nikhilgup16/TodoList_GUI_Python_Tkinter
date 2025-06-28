from tkinter import *
window = Tk()

window.geometry("500x500")
window.title("Todo List")
window.config(background="skyblue")

notes = []

def myNoteFunc(event):
    window.withdraw()
    myNoteWindow = Toplevel()
    myNoteWindow.geometry("500x500")
    myNoteWindow.title("My Notes")
    myNoteWindow.config(background="skyblue")

    def homePage(event):
        myNoteWindow.withdraw()
        window.deiconify()

    home_page_btn = Button(
        myNoteWindow,
        font="Arial 15 bold",
        text="Home Page",
    )
    home_page_btn.bind("<Button-1>",homePage)
    home_page_btn.place(x=350,y = 430)

    header = Label(
    myNoteWindow,
    text="My Note's",
    font="Arial 40 bold",
    background="green",
    foreground="yellow",
    )
    header.pack(fill=X)

    for i in range(0,6):
        Label(
            myNoteWindow,
            text=notes[i],
            font="Arial 30 bold",
            background="skyblue",
            anchor="w",
            ).pack(fill="both",padx=10,pady=4)

def addNoteFunc(event):

    global notes
    window.withdraw()
    addNoteWindow = Toplevel()
    addNoteWindow.geometry("500x500")
    addNoteWindow.title("Add Note")
    addNoteWindow.config(background="skyblue")

    def homePage(event):
        addNoteWindow.withdraw()
        window.deiconify()

    def storeNote():
        Text = entry.get()
        if Text == "":
            pass
        elif len(Text) > 20:
            warning = Label(
                addNoteWindow,
                text=" (Warning : Your Text Is Greater Than 20 Character's) ",
                background="skyblue",
            )
            warning.place(x=30,y=250)
        else:
            notes.append(Text)  

    header = Label(
    addNoteWindow,
    text="Add Note",
    font="Arial 40 bold",
    background="green",
    foreground="yellow",
    )
    header.pack(fill=X)

    writing_icon = Label(
        addNoteWindow,
        text="✍️",
        background="skyblue",
        font="Arial 150 bold",
    )
    writing_icon.place(x=150,y=70)

    noteLabel = Label(
        addNoteWindow,
        text=" (Note : You Can Only Add 5 Notes And The Added Note Should Be 20 Character's Long) ",
        background="skyblue",
    )
    noteLabel.place(x=25,y=280)

    entry = Entry(addNoteWindow,font="Arial 30 bold")
    entry.place(x=30,y = 300)

    submitBtn = Button(
        addNoteWindow,
        font="Arial 15 bold",
        text="Submit",
        command=storeNote,
    )
    submitBtn.place(x=390,y = 370)

    home_page_btn = Button(
        addNoteWindow,
        font="Arial 15 bold",
        text="Home Page",
    )
    home_page_btn.bind("<Button-1>",homePage)
    home_page_btn.place(x=350,y = 430)

def deleteNoteFunc(event):
    global notes
    window.withdraw()
    deleteNoteWindow = Toplevel()
    deleteNoteWindow.geometry("500x500")
    deleteNoteWindow.title("Delete Note")
    deleteNoteWindow.config(background="skyblue")

    def homePage(event):
        deleteNoteWindow.withdraw()
        window.deiconify()

    home_page_btn = Button(
        deleteNoteWindow,
        font="Arial 15 bold",
        text="Home Page",
    )
    home_page_btn.bind("<Button-1>",homePage)
    home_page_btn.place(x=350,y = 430)

    header = Label(
    deleteNoteWindow,
    text="Delete Note",
    font="Arial 40 bold",
    background="green",
    foreground="yellow",
    )
    header.pack(fill=X)

    def delete_saved_note(index):
        del notes[index]
        deleteNoteWindow.destroy()
        deleteNoteFunc(None)

    for i in range(0,6):
        Button(
            deleteNoteWindow,
            text=notes[i],
            font="Arial 20 bold",
            background="skyblue",
            anchor="w",
            borderwidth=0,
            relief="flat",
            activebackground="skyblue",
            command=lambda i=i: delete_saved_note(i),
            ).pack(fill="both",padx=10)

header = Label(
    window,
    text="Todo List App",
    font="Arial 40 bold",
    background="green",
    foreground="yellow",
)
header.pack(fill=X)

frame = Frame(window,background="skyblue")
frame.place(x=140,y=190)

my_note = Label(
    frame,
    text="My Notes",
    font="Arial 30 bold",
    background="skyblue",
    foreground="green",
)
my_note.bind("<Button-1>", myNoteFunc)
my_note.pack(padx=20)

add_note = Label(
    frame,
    text="Add Note",
    font="Arial 30 bold",
    background="skyblue",
    foreground="green",
)
add_note.bind("<Button-1>", addNoteFunc)
add_note.pack(padx=20)

delete_note = Label(
    frame,
    text="Delete Note",
    font="Arial 30 bold",
    background="skyblue",
    foreground="green",
)
delete_note.bind("<Button-1>", deleteNoteFunc)
delete_note.pack()

window.mainloop()