import ttkbootstrap as ttk
import csv
import pickle
import tkinter as tk



#dictionary so that the input colour when creating a new flavour will be saved as a ttkbootstrap widget theme
colours = {"green": "primary",
           "orange": "secondary",
           "light pink": "success", 
           "dark pink": "info", 
           "beige": "warning", 
           "red": "danger", 
           "white": "light", 
           "blue": "dark"}

#function that saves the data
def save():
    with open(r"resources/monsterDictionary.pkl", "wb") as fp:
        pickle.dump(monsterDictionary, fp)
    
    with open(r"resources/monsterTypes.pkl", "wb") as gingle:
        pickle.dump(monsterTypes, gingle)


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

#function that adds a new flavour to the list, reloads the frame and then saves it
def addFlavour(name, colour):
    monsterDictionary[name] = 0
    monsterTypes.append([name, colours[colour]])
    save()
    options()



#open the save files
with open(r"resources/monsterDictionary.pkl", "rb") as peepee:
    monsterDictionary = pickle.load(peepee)
print(monsterDictionary)

with open(r"resources/monsterTypes.pkl", "rb") as fart:
    monsterTypes = pickle.load(fart)




#create the ui elements

#create the window
window = ttk.Window(themename="monster", title = "Monster Tracker", iconphoto= r"resources/monsterPNG.png", size=[500,800], position=[700, 150])

#create the frame for the buttons to go in
titleFrame = ttk.Labelframe(window, text="Monster Types", bootstyle="primary")
titleFrame.pack(side="top")


#create the frame for the information to go in
infoFrame = ttk.Frame(window)
infoFrame.pack(side="top")


#function that contains titleFrame and all widgets inside of it, calling it will reload the widget
def options():
    removeFrames(titleFrame)
    #create the buttons for the drinks
    for i in range(0, len(monsterTypes)):
        button = ttk.Button(titleFrame, text= monsterTypes[i][0], bootstyle= monsterTypes[i][1], command=lambda idx = i: counter(idx))
        button.pack(fill= "x", padx= 25, pady=5, side="top")

    label = ttk.Label(titleFrame, text="Add a new flavour", bootstyle="primary")
    label.pack(side="top")
#input box for name of new monster
    monsterInput = ttk.Entry(titleFrame)
    monsterInput.pack(side= "left", padx=25, pady=10)
#monster colours
#this is then put into the colours dictionary to find the ttkbootstrap widget theme that fits the colour
    colours = ["green", "orange", "light pink", "dark pink", "beige", "red", "white", "blue"]

#creates combo box for the colour to be chose
    monsterColour = ttk.Combobox(titleFrame)
    #inserts the colours from the array into the box
    monsterColour["values"] = (colours)
    #inserts the word "colour" to identify what the box does
    monsterColour.insert(0, "Colour")
    monsterColour.pack(side="left")


    #function that is triggerd by the "add flavour" button
    #this is easier because multiple things need to be done by the button as it has to get the input from the combobox and entry
    def temp():
        name = monsterInput.get()
        colour = monsterColour.get()
        addFlavour(name, colour)
        
    
    #button to add monster
    monsterInputButton = ttk.Button(titleFrame, text="Add Flavour", command= temp)
    monsterInputButton.pack(side="left", padx= 25, pady=10)


options()

window.mainloop()