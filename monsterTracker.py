import ttkbootstrap as ttk
import csv
import pickle

#function to delete all widgets in a frame
def removeFrames(frame):
    for widgets in frame.winfo_children():
        widgets.pack_forget()

#displays stats
def counter(num):
    #clears old info
    removeFrames(infoFrame)
    colour = monsterTypes[num][1]
    type = monsterTypes[num][0]
    #displays new info
    label = ttk.Label(infoFrame, text= f"you have consumed {monsterDictionary[type]} cans of {monsterTypes[num][0]}")
    label.pack(side="left", padx=5, pady=5, fill= "x")
    #makes button to add one to drink counter
    addButton = ttk.Button(infoFrame, text="I just drank one", bootstyle= colour, command= lambda idx = num: drink(idx))
    addButton.pack(side="right")

#function that is triggered by the "i just drank one" button
#increases count of that flavour by one and saves it
def drink(num):
    type = monsterTypes[num][0]
    #increases count by one
    monsterDictionary[type] = monsterDictionary[type] + 1
    #saves new number
    with open(r"resources/monsterDictionary.pkl", "wb") as fp:
        pickle.dump(monsterDictionary, fp)
    #updates counter
    counter(num)

#open the save files
with open(r"resources/monsterDictionary.pkl", "rb") as peepee:
    monsterDictionary = pickle.load(peepee)

with open(r"resources/monsterTypes.pkl", "rb") as fart:
    monsterTypes = pickle.load(fart)

#create the ui elements

#create the window
window = ttk.Window(themename="monster", title = "Monster Tracker", iconphoto= r"resources/monsterPNG.png", size=[400,800], position=[700, 150])

#create the frame for the buttons to go in
titleFrame = ttk.Labelframe(window, text="Monster Types", bootstyle="primary")
titleFrame.pack(side="top", expand = True, fill= "both")

#create the frame for the information to go in
infoFrame = ttk.Frame(window, bootstyle="primary")
infoFrame.pack(side="bottom")

#create the buttons for the drinks
for i in range(0, len(monsterTypes)):
    button = ttk.Button(titleFrame, text= monsterTypes[i][0], bootstyle= monsterTypes[i][1], command=lambda idx = i: counter(idx))
    button.pack(fill= "x", padx= 25, pady=5, side="top")

window.mainloop()