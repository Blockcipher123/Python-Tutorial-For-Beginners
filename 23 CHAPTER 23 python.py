# ***************************************************************************************************************************************************************************
# **************************************************************CH-23*************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************




# ======================================================== creat widgets using loop ======================================================================

import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Loop GUI') 

labels = ['What is your name : ', 'What is your age : ', 'What is your gender : ', 'Country : ', 'State : ', 'City : ']



for i in range(len(labels)):
    cur_label = 'label' + str(i)
    cur_label = ttk.Label(win, text=labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W)

# entry box
name_var = tk.StringVar()
user_info = {
    'name' : tk.StringVar(), 
    'age' : tk.StringVar(),
    'gender' : tk.StringVar(),
    'country' : tk.StringVar(), 
    'state' : tk.StringVar(),
    'city' : tk.StringVar() 
}
counter=0
for i in user_info:
    cur_entrybox = 'entry' + i
    cur_entrybox = ttk.Entry(win, width=16, textvariable=user_info[i])
    cur_entrybox.grid(column=1, row=counter)
    counter += 1

def submit():
    print(user_info['name'].get())
    print(user_info['age'].get())
    print(user_info['gender'].get())
    print(user_info['country'].get())
    print(user_info['state'].get())
    print(user_info['city'].get())

submit_button = tk.Button(win, text='Submit',command=submit)
submit_button.grid(row = 6, columnspan=2)


# Seee in Console in OUTPUT

win.mainloop()

# ===================================================== YOUR PYTHON COURSE IS COMPLETED ================================================


# ==================================================== CONGRALUTATION YOU HAVA COMPLETED YOUR PYTHON COURSE ==============================================