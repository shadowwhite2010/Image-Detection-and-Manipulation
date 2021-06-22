from tkinter import *
root = Tk()
def validate(user_input):
    # check if the input is numeric
    if  user_input.isdigit():
        # Fetching minimum and maximum value of the spinbox
        minval = int(root.nametowidget(spinbox).config('from')[4])
        maxval = int(root.nametowidget(spinbox).config('to')[4])
  
        # check if the number is within the range
        if int(user_input) not in range(minval, maxval+1):
            print ("Out of range")
            return False
  
        # Printing the user input to the console
        print(user_input)
        return True
  
    # if input is blank string
    elif user_input is "":
        print(user_input)
        return True
  
    # return false is input is not numeric
    else:
        print("Not numeric")
        return False
	
# entry = Entry(root, validate="key")
# entry['validatecommand'] = (entry.register(validate),'%P','%d')
# entry.pack()

spinbox = Spinbox(root, from_ = 1, to = 1000, validate ="key")

# range_validation = root.register(validate)
spinbox['validatecommand'] = (spinbox.register(validate),'%P')
# spinbox.config(validate ="key",
#          validatecommand =(range_validation, '% P'))
spinbox.pack(pady = 20)
root.mainloop()