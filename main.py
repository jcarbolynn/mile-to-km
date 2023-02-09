import tkinter

# initialize new object from this class
window = tkinter.Tk()

# # need to keep window open so use while loop, built in as main loop
# keep at bottom of code
# window.mainloop()

window.title("Mile to Km Converter")
# window.minsize(width = 400, height = 300)
window.config(padx=20, pady=20)

# create a label using the label class
# things wont show up without specifyin ghow it will be displayed
equals = tkinter.Label(text="is equal to", font = ("arial", 10, "italic"))
equals.grid(column=0,row=1)

converted = tkinter.Label(text="0", font = ("arial", 10, "normal"))
converted.grid(column=1,row=1)

miles = tkinter.Label(text="miles", font = ("arial", 10, "normal"))
miles.grid(column=2,row=0)

km = tkinter.Label(text="km", font = ("arial", 10, "normal"))
km.grid(column=2,row=1)

def to_km(miles):
  return round(miles * 1.6, 2)

def button_clicked():
  converted.config(text=to_km(int(input_miles.get())))


# when button detects command, triggers this method, no () because we only want to call the function when the button is clicked
calculate_button = tkinter.Button(text= 'Calculate', command=button_clicked)
calculate_button.grid(column=1,row=2)

# entry component
input_miles = tkinter.Entry(text="0")
input_miles.grid(column=1,row=0)



window.mainloop()
