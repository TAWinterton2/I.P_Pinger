#Travis Winterton
#I.P Checker 
#   A python script that takes I.P adresses from a csv. / xls file and pings each one
#   marking each one that responded back or did not repond back 

import pandas as pd 
import tkinter as tk
from tkinter import filedialog
from tkinter import *



#Open Window for file select
def open_file_path():
    try:
        file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Comma Seperated Values ", "*.csv"), ("Microsoft Excel Files", ".*xls")])
        display_file_contents(file_path)
    except Exception as e:
        print("Error has occured!: ", e)


        
    
def display_file_contents(file_path):
    try:
        df = pd.read_csv(file_path)
        print(df.head())
    except Exception as e:
        print("Uh oh... something happend: \n", e)




#main funciton
def main():

    #should probably put all of this into a class at some point....


    #set up main window application
    root = tk.Tk()
    root.title("TEST")

 
    #open a file button
    open_button = tk.Button(root, text="Open File", command=open_file_path)
    open_button.pack(padx=20, pady=20)

    selected_file_label = tk.Label(text="Select File")
    #selected_file_label.pack()




  

    root.mainloop()



# run main function
if __name__ == '__main__':
    main()



