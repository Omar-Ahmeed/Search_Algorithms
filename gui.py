from tkinter import *
import webbrowser
from Functions import *
from A_Star import A_Star
from BFS import BFS
from DFS import DFS
from Plot_Map import *
from pathlib import Path



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\oed51\OneDrive\Desktop\New folder (4)\out\4\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

Nodes = Get_Graph()
cities = list(Nodes.keys())
window = Tk( className='My Way')

window.geometry("1440x797")
window.configure(bg = "#3A7FF6")


canvas = Canvas(
    window,
    bg = "#3A7FF6",
    height = 797,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    806.0,
    54.0,
    anchor="nw",
    text="Are You Lost ?",
    fill="#FFFFFF",
    font=("GEJaridaHeavy Heavy", 64 * -1)
)

canvas.create_rectangle(
    800.0,
    131.0,
    1128.0,
    153.0,
    fill="#FFFFFF",
    outline="",
    )

canvas.create_text(
    806.0,
    180.0,
    anchor="nw",
    text="Don’t Worry Lets Find Your Way",
    fill="#FFFFFF",
    font=("GEJaridaHeavy Heavy", 24 * -1)
)

canvas.create_text(
    806.0,
    275.0,
    anchor="nw",
    text="MyWay Application Is Designed To Find Paths  ",
    fill="#FFFFFF",
    font=("GEJaridaHeavy Heavy", 24 * -1)
)

canvas.create_text(
    806.0,
    307.0,
    anchor="nw",
    text="Between Some Egyptian Cities You Only  ",
    fill="#FFFFFF",
    font=("GEJaridaHeavy Heavy", 24 * -1)
)

canvas.create_text(
    806.0,
    339.0,
    anchor="nw",
    text="Need To Determine Your Location,",
    fill="#FFFFFF",
    font=("GEJaridaHeavy Heavy", 24 * -1)
)

canvas.create_text(
    806.0,
    371.0,
    anchor="nw",
    text="Your Destination  And Your Algorithm",
    fill="#FFFFFF",
    font=("GEJaridaHeavy Heavy", 24 * -1)
)

canvas.create_text(
    806.0,
    502.0,
    anchor="nw",
    text="The Program Based On ",
    fill="#FFFFFF",
    font=("GEJaridaHeavy Heavy", 24 * -1)
)

canvas.create_text(
    1087.0,
    502.0,
    anchor="nw",
    text="Python",
    fill="#FED956",
    font=("GEJaridaHeavy Heavy", 24 * -1)
)

canvas.create_text(
    806.0,
    534.0,
    anchor="nw",
    text="Using              To Draw The Paths",
    fill="#FFFFFF",
    font=("GEJaridaHeavy Heavy", 24 * -1)
)

canvas.create_text(
    880.0,
    534.0,
    anchor="nw",
    text="Folium",
    fill="#4635AB",
    font=("GEJaridaHeavy Heavy", 24 * -1)
)

canvas.create_text(
    806.0,
    566.0,
    anchor="nw",
    text="And                             To Design The GUI",
    fill="#FFFFFF",
    font=("GEJaridaHeavy Heavy", 24 * -1)
)

canvas.create_text(
    860.0,
    566.0,
    anchor="nw",
    text="Tkinter Designer",
    fill="#FB1C44",
    font=("GEJaridaHeavy Heavy", 24 * -1)
)


canvas.create_text(
    806.0,
    727.0,
    anchor="nw",
    text="Omar El-Sayed Ahmed ",
    fill="#FFFFFF",
    font=("GEJaridaHeavy Heavy", 24 * -1)
)

canvas.create_rectangle(
    0.0,
    0.0,
    739.0,
    797.0,
    fill="#FFFFFF",
    outline="",
    )


canvas.create_text(
    65.0,
    121.0,
    anchor="nw",
    text="Choose Your Location",
    fill="#000000",
    font=("GEJaridaHeavy Heavy", 46 * -1)
)

# Create option menu
variable1 = StringVar(window)
variable1.set("Choose City")
option = OptionMenu(window, variable1, *cities, command= lambda x: print(x))
option.config(width=20, font=('Old Antic Bold', 15), bg="#6DA3FF", fg="#FFFFFF", activebackground="#FFFFFF", activeforeground="#000000")
option['menu'].config(bg="#6DA3FF", fg="#FFFFFF", activebackground="#FFFFFF", activeforeground="#6DA3FF", font=('Old Antic Bold', 10))
option.place(x=65.0, y=200, width=400, height=50 , bordermode=OUTSIDE, anchor=NW)

canvas.create_text(
    65.0,
    308.0,
    anchor="nw",
    text="Choose Your Destination ",
    fill="#000000",
    font=("GEJaridaHeavy Heavy", 46 * -1)
)

variable2 = StringVar(window)
variable2.set("Choose City") 
option = OptionMenu(window, variable2, *cities, command= lambda x: print(x))
option.config(width=20, font=('Old Antic Bold', 15), bg="#6DA3FF", fg="#FFFFFF", activebackground="#FFFFFF", activeforeground="#000000")
option['menu'].config(bg="#6DA3FF", fg="#FFFFFF", activebackground="#FFFFFF", activeforeground="#6DA3FF", font=('Old Antic Bold', 10))
option.place(x=65.0, y=390, width=400, height=50 , bordermode=OUTSIDE, anchor=NW)

canvas.create_text(
    62.0,
    495.0,
    anchor="nw",
    text="Choose Algorithm",
    fill="#000000",
    font=("GEJaridaHeavy Heavy", 46 * -1)
)

# create a radio button
var = IntVar()
R1 = Radiobutton(window,font=('Helvetica', 25)  , text="A*", variable=var, value=1, bg="#FFFFFF", fg="#6DA3FF", activebackground="#6DA3FF", activeforeground="#FFFFFF",command= lambda : print("A*"))
R1.config(width=10, height=1)
R1.place(x=50, y=570, )
R2 = Radiobutton(window,font=('Helvetica', 25)  , text="BFS", variable=var, value=2,bg="#FFFFFF", fg="#6DA3FF", activebackground="#6DA3FF", activeforeground="#FFFFFF",command= lambda : print("BFD"))
R2.config(width=10, height=1)
R2.place(x=250, y=570)
R3 = Radiobutton(window,font=('Helvetica', 25)  , text="DFS", variable=var, value=3,bg="#FFFFFF", fg="#6DA3FF", activebackground="#6DA3FF", activeforeground="#FFFFFF",command= lambda : print("DFS"))
R3.config(width=10, height=1)
R3.place(x=450, y=570 ,bordermode=OUTSIDE, anchor=NW,)

# create a button
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Find_Path(),
    relief="flat"
)
button_1.place(
    x=185.0,
    y=670.0,
    width=367.0,
    height=80.0
)


def Find_Path():
    start_node = variable1.get()
    stop_node = variable2.get()
    if var.get() == 1:
        path = A_Star(start_node, stop_node)
        Plot_Map(path)
    elif var.get() == 2:
        path = BFS(start_node, stop_node)
        Plot_Map(path)
    elif var.get() == 3:
        path = DFS(start_node, stop_node)
        Plot_Map(path)
    else:
        print("Please Choose Algorithm")
    webbrowser.open_new_tab('Map2.html')


window.resizable(False, False)
window.mainloop()
