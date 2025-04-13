from tkinter import *

#cerate a window
#setup widget
#create a function
def convert():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_display.config(text = f"{km}")



#setting up window
window = Tk() #creating tkinter object
window.title("Miles to Km")
window.config(padx= 50 , pady= 50)

#miles entry
miles_input = Entry()
miles_input.grid(row = 0 , column = 1)


#miles label
miles_label = Label(text="miles")
miles_label.grid(column = 2 , row = 0)


#is_equal_to label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column = 0 , row = 1)

#km result
km_result_display = Label(text="0")
km_result_display.grid(column = 1, row = 1)

#km label
km_result_label = Label(text="km")
km_result_label.grid(column = 2 , row = 1)

#calculate button
calculate_button = Button(text="Calculate" , command= convert)
calculate_button.grid(column = 1 , row = 2)




window.mainloop()

