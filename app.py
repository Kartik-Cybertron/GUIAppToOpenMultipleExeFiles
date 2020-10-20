import tkinter as tk
from tkinter import filedialog, Text
import os

# To create a graphical display structure
root = tk.Tk()
apps = []

# to check the file if exist then enter the module or continue to next module
if os.path.isfile('save.txt'):
    # to open the file and read the dtaa from it
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps =  [x for x in tempApps if x.strip()]



def addApp():
# to fetch and destroy the children processes in realtime
    for widget in frame.winfo_children():
        # it will destroy the duplictae object from the widget
        widget.destroy()

# to open a file from explorer and set defalt exe and all types of file in dropdown
    filename = filedialog.askopenfilename(initialdir="/",title="Select file",
                    filetypes= (("executables","*.exe"),("all files","*.*")))
    # to append fileames to apps
    apps.append(filename)
    # print(filename)

    # to fetch filenames from apps and pate it on labels on the frame/display
    for app in apps:
        # to craete a label on framw
        label = tk.Label(frame,text =app, bg="gray")
        # to set a label on screen
        label.pack()



def runApp():
    for app in apps:
        # to start the file through os module start method 
        os.startfile(app)



# to set the a canvas or working display area inside a root structure
canvas = tk.Canvas(root, height=500,width=500,bg="#263D42")
# to set the data on the root
canvas.pack()

# to create a frame inside the diplay with a spcific bgcolor
frame = tk.Frame(root, bg="white")
# setting the point where to set it and will be responsive as per the window 
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

# to create a button inside the root structure with padding and fore/back ground colors
openFile = tk.Button(root, text="Open File",padx=10,pady=5,
                        fg="white",bg="#263D42", command=addApp)
# to set on frame
openFile.pack()

# to create a 2nd button inside the root structure with padding and fore/back ground colors
runApps = tk.Button(root, text="Run Apps",padx=10,pady=5,
                        fg="white",bg="#263D42", command=runApp)
# to set on frame
runApps.pack()

for app in apps:
        # to craete a label on framw
        label = tk.Label(frame,text =app)
        # to set a label on screen
        label.pack()



# keep looping the frame / root
root.mainloop()



# file handling
# to create a file or open existing file inside the current folder in write mode
with open('save.txt','w') as f:
    for app in apps:
        # to write data in the file
        f.write(app +',')