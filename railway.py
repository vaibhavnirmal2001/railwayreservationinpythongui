from tkinter import *
from PIL import ImageTk, Image
import shutil
import os
import easygui

from tkinter import filedialog
from tkinter import messagebox as mb



def open_window():
    read = easygui.fileopenbox()
    return read



def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File not found!")



def copy_file():
    source1 = open_window()
    destination1 = filedialog.askdirectory()
    shutil.copy(source1, destination1)
    mb.showinfo('confirmation', "File Copied !")


def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)
    else:
        mb.showinfo('confirmation', "File not found !")


def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension = os.path.splitext(chosenFile)[1]
    print("Enter new name for the chosen file")
    newName = input()
    path = os.path.join(path1, newName + extension)
    print(path)
    os.rename(chosenFile, path)
    mb.showinfo('confirmation', "File Renamed !")


def move_file():
    source = open_window()
    destination = filedialog.askdirectory()
    if (source == destination):
        mb.showinfo('confirmation', "Source and destination are same")
    else:
        shutil.move(source, destination)
        mb.showinfo('confirmation', "File Moved !")


def make_folder():
    newFolderPath = filedialog.askdirectory()
    print("Enter name of new folder")
    newFolder = input()
    path = os.path.join(newFolderPath, newFolder)
    os.mkdir(path)
    mb.showinfo('confirmation', "Folder created !")


def remove_folder():
    delFolder = filedialog.askdirectory()
    os.rmdir(delFolder)
    mb.showinfo('confirmation', "Folder Deleted !")


def list_files():
    folderList = filedialog.askdirectory()
    sortlist = sorted(os.listdir(folderList))
    i = 0
    print("Files in ", folderList, "folder are:")
    while (i < len(sortlist)):
        print(sortlist[i] + '\n')
        i += 1







root = Tk()

root.geometry("450x700")
root.maxsize(700,500)
root.title("My Group Project using GUI")






Label(root, text="Railway Reservation System", font=("Helvetica 16 bold"), fg="black", padx="90", pady="30", bg="gray"
      , relief=SUNKEN, borderwidth="4").grid(row=5, column=2)


Button(root, text="Open Passengers Data", command=open_file, padx="20", pady="5", borderwidth="10", bg="black", fg="white",
       font=("Helvetica 16 bold")).grid(row=15, column=2)


Button(root, text="Delete Passengers Data", command=delete_file, padx="20", pady="5", borderwidth="10", bg="black", fg="white",
       font=("Helvetica 16 bold")).grid(row=35, column=2)

Button(root, text="Make a Folder for\n Passengers Data", command=make_folder, padx="20", pady="5", borderwidth="10", bg="black", fg="white",
       font=("Helvetica 16 bold")).grid(row=75, column=2)

Button(root, text="Remove a Folder of Passengers Data", command=remove_folder, padx="20", pady="5", borderwidth="10", bg="black",
       fg="white", font=("Helvetica 16 bold")).grid(row=65, column=2)



root.mainloop()



