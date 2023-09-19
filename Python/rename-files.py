"""
Created this script as I was ripping my parents' dvds and bluray box sets for them
This is meant to be used after ripping with makemkv or similar programs
and then this allows you to rename all of those files at once in TV show format: "<name_of_show> SXXEXX"
"""
import os
import platform
from tkinter import BOTTOM, Button, Entry, Frame, Label, StringVar, Tk, ttk

def rename_files(directory,name,file_extension,total_episodes,starting_ep,season_number):
    """
    Handles Renaming the files
    Adds the appropriate 0s based on the number of episodes you input and the season inputted into the GUI
    Once completed with renaming, moves back to the directory where the script is located
    """
    episode = starting_ep
    season = 1
    for filename in os.listdir(directory):
        #seasons 0s logic for proper file sorting when above 10 seasons
        if season_number < 10:
            season = "0" + str(season_number)
        else:
            season = str(season_number)
        ep = str(episode)
        source = directory + filename
        #episode 0s logic for proper file sorting when at different amounts of episodes
        if total_episodes >= 10 and not (total_episodes > 100):
            if episode <= 9:
                ep = "0" + ep
        elif total_episodes >= 100 and not (total_episodes > 1000):
            if episode <= 9:
                ep = "00" + ep
            elif episode <= 99:
                ep = "0" + ep
        elif total_episodes > 1000:
            if episode <= 9:
                ep = "000" + ep
            elif episode <= 99:
                ep = "00" + ep
            elif episode <= 999:
                ep = "0" + ep
        destination = directory + name + " S" + str(season) + "E" + ep + file_extension #creates the string to rename the file with from the variables
        os.rename(source, destination)
        episode += 1
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

def gui():
    """
    Creates the relatively minimal GUI when called
    Uses the function labal_entry_pack to pack into the gui quickly instead of bloating the LOC
    The code is moderately readable
    """
    e_list = []
    base = Tk()
    base.geometry("200x400")
    frame = Frame(base)
    frame.pack()
    dir_label_text = "Path to Folder:"
    dir_entry_text = ""
    name_label_text = "Name of Show"
    name_entry_text = ""
    ext_label_text = "File Extension"
    ext_entry_text = ".mkv"
    total_label_text = "Total Number of episodes"
    total_entry_text = ""
    season_label_text = "Season Number:"
    season_entry_text = "1"
    starting_label_text = "Starting episode Number:"
    starting_entry_text = "1"
    label_entry_pack(dir_label_text,dir_entry_text,frame,e_list)
    label_entry_pack(name_label_text,name_entry_text,frame,e_list)
    label_entry_pack(ext_label_text,ext_entry_text,frame,e_list)
    label_entry_pack(total_label_text,total_entry_text,frame,e_list)
    label_entry_pack(starting_label_text,starting_entry_text,frame,e_list)
    label_entry_pack(season_label_text,season_entry_text,frame,e_list)
    bottom_frame = Frame(base)
    bottom_frame.pack(side=BOTTOM)
    run_button = Button(bottom_frame, text = "Rename Files!", command=lambda:run_all(e_list[0],e_list[1],e_list[2],e_list[3],e_list[4],e_list[5]), font = ("Impact 15"))
    run_button.pack(pady=5)
    base.title("Batch Rename")
    #loops to wait for inputs
    base.mainloop()

def label_entry_pack(label_desc, entry_text, frame, entry_list:list):
    """
    Function for creating labels and packing them into the list to be created
    """
    text = StringVar()
    text.set(label_desc)
    label = Label(frame, textvariable=text)
    label.pack()
    entry = Entry(frame, width = 30,bd=2,)
    entry.insert(0,entry_text)
    entry.pack(padx=5,pady=5)
    entry_list.append(entry)

def run_all(dir:Entry,name:Entry,ext:Entry,total:Entry,starting:Entry,season:Entry):
    """
    Moves into the directory specified, then calls the rename_files function to rename the files
    """
    if platform.system() == "Windows":
        directory = dir.get() + "\\"
    else:
        directory = dir.get()
    os.chdir(directory)
    rename_files(directory,name.get(),ext.get(),int(total.get()),int(starting.get()),int(season.get()))

if __name__ == "__main__":
    gui()
