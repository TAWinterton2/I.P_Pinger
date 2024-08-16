#Travis Winterton
#I.P Checker 
#   A python script that takes I.P adresses from a csv. / xls file and pings each one
#   marking each one that responded back or did not repond back 

import pandas as pd 
import tkinter as tk
import pathlib
from ping import ping


from tkinter import filedialog
from tkinter import *



#should probably put all of this into a class at some point....


#Open Window for file select
def open_file_path():

    text_widget.delete('1.0', tk.END)
    text_widget.insert(tk.END, "-" * 60 + '\n' )
    text_widget.insert(tk.END, "Starting Ping Scan...\n")
    text_widget.insert(tk.END, "-" * 60 + '\n' )

    try:
        file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Comma Seperated Values ", "*.csv"), ("Microsoft Excel Files", ".*xls")])
        print(file_path)
        file_extension = pathlib.Path(file_path).suffix

        display_file_contents(file_path, file_extension)
    except Exception as e:

        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, "-" * 60 + '\n' )
        text_widget.insert(tk.END, "An Error has Occured: ", e)
        text_widget.insert(tk.END, "-" * 60 + '\n' )
        
        print("Error has occured!: ", e)
    
def display_file_contents(file_path, extension):
    
    if extension == '.csv':
        try:
            
            #store contents into data frame, clean, then into list

            df = pd.read_csv(file_path, usecols=['I.P'])
            df.dropna(inplace=True)
            
            nodes = df["I.P"].to_list()

            #Start Pinging
            good_ping, bad_ping = ping(nodes, 3)

        
            #Display Results
            text_widget.delete('1.0', tk.END)
            text_widget.insert(tk.END, "-" * 60 + '\n' )
            text_widget.insert(tk.END, "Ping Scan Completed: \n")
            text_widget.insert(tk.END, "Sucessful Pings: \n")
            for x in good_ping:
                text_widget.insert(tk.END, x + '\n')
            
            text_widget.insert(tk.END, "Failed Pings: \n")
            for x in bad_ping:
                text_widget.insert(tk.END, x + "\n")
            text_widget.insert(tk.END, "-" * 60 + '\n' )
            

        except Exception as e:
            print("Uh oh... something happend: \n", e)
   
    elif extension == '.xls':
        try:
            df = pd.read_excel(file_path)
            df.dropna(inplace=True)
            print("Opening File")
            text_widget.delete('1.0', tk.END)
            text_widget.insert(tk.END, df)
        except Exception as e:
            print("Uh oh... something happend: \n", e)
    
    else:
            text_widget.delete('1.0', tk.END)
            text_widget.insert(tk.END, "File type Not Supported")
            raise Exception("File Type Not Supported")

        
    




#set up main window application
root = tk.Tk()
root.title("TEST")

#open a file button
open_button = tk.Button(root, text="Open File", command=open_file_path)
open_button.pack(padx=20, pady=20)

#Create a text widget
text_widget = tk.Text(root, wrap="word", width=60, height=20)
text_widget.pack(pady=10, padx=10)

selected_file_label = tk.Label(text="Select File")

text_widget.insert(tk.END, "-" * 60 + '\n' )
text_widget.insert(tk.END, "Please Select a File\n")
text_widget.insert(tk.END, "-" * 60 + '\n' )

root.mainloop()



