# Import necessary modules from tkinter. 

from tkinter import Tk, Entry, Button, StringVar

class Calculator:   # Defines a class called calculator  
    # Calling a special method called "constructor method" 
    # to initialise the calculator program.      
    def __init__(self,master):
        # Defining the title displayed in the title bar of the program.  
        master.title("Basic Calculator")
        # Defining the size measurements for the main 
        # window of the calculator program.
        master.geometry('278x570+0+0')
        # Defining the colour of the main window of the program. 
        master.config(bg='purple')
        # Setting the window of the calculator program 
        # as non-resizable(width wise and height wise).
        master.resizable(False,False)

       # Defining a value holder when a buttons are pressed.
        self.equation = StringVar()
       # Setting the initial entry value string as an empty string.
        self.entry_value = ''
       # Creating the entry field of the calculator program.
        Entry(width=12  , bg='#fff', font=('Arial Bold' , 29) ,
              textvariable=self.equation).place(x=4,y=0)


        # Below shows the creation of buttons of the calculator program for 
        # the basic operations and the numbers.
        Button(width=11 , height=4 , text='(' , relief='flat' ,
               bg='light blue' ,
               command=lambda:self.show('(')).place(x= 3 ,y=50 )
        Button(width=11 , height=4 , text=')' , relief='flat' ,
               bg='light blue' , 
               command=lambda:self.show(')')).place(x= 93,y= 50)
        Button(width=11 , height=4 , text='+' , relief='flat' ,
               bg='cyan' , command=lambda:self.show('+')).place(x=183 ,y=50 )
        Button(width=11 , height=4 , text='-' , relief='flat' ,
               bg='cyan' , command=lambda:self.show('-')).place(x= 3,y=125 )
        Button(width=11 , height=4 , text='x' , relief='flat' ,
               bg='cyan' , command=lambda:self.show('*')).place(x= 93,y=125 )
        Button(width=11 , height=4 , text='/' , relief='flat' ,
               bg='cyan' ,
               command=lambda:self.show('/')).place(x= 183,y=125 )
        Button(width=11 , height=4 , text='1' , relief='flat' ,
               bg='white' , command=lambda:self.show(1)).place(x=3 ,y=200 )
        Button(width=11 , height=4 , text='2' , relief='flat' ,
               bg='white' , command=lambda:self.show(2)).place(x=93 ,y=200 )
        Button(width=11 , height=4 , text='3' , relief='flat' ,
               bg='white' , command=lambda:self.show(3)).place(x=183 ,y= 200)
        Button(width=11 , height=4 , text='4' , relief='flat' ,
               bg='white' , command=lambda:self.show(4)).place(x=3 ,y= 275)
        Button(width=11 , height=4 , text='5' , relief='flat' ,
               bg='white' , command=lambda:self.show(5)).place(x=93 ,y= 275)
        Button(width=11 , height=4 , text='6' , relief='flat' ,
               bg='white' , command=lambda:self.show(6)).place(x= 183,y= 275)
        Button(width=11 , height=4 , text='7' , relief='flat' ,
               bg='white' , command=lambda:self.show(7)).place(x= 3,y= 350)
        Button(width=11 , height=4 , text='8' , relief='flat' ,
               bg='white' , command=lambda:self.show(8)).place(x=93 ,y=350 )
        Button(width=11 , height=4 , text='9' , relief='flat' ,
               bg='white' , command=lambda:self.show(9)).place(x= 183,y= 350)
        Button(width=11 , height=4 , text='0' , relief='flat' ,
               bg='white' , command=lambda:self.show(0)).place(x=3 ,y=425 )
        Button(width=11 , height=4 , text='.' , relief='flat' ,
               bg='white' ,
               command=lambda:self.show('.')).place(x= 93,y= 425)
        Button(width=11 , height=4 , text='C' , relief='flat' ,
               bg='red' , command=self.clear).place(x= 183,y= 425)
        Button(width=37 , height=3 , text='=' , relief='flat' ,
               bg='black' , command=self.solve).place(x= 3,y=500 )
        
    # Defining a method to update the entry field when the buttons of the
    # calculator is pressed.
    def show(self,value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    # Defining a method to clear the entry field of the calculator program.
    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)
    
    # Defining a method to calculate the answer for the mathematical
    # expression entered in to the entry field using buttons.
    def solve(self):
       try:
          result= eval(self.entry_value)
          self.equation.set(result)
       except Exception as e:   # Handle exceptions.
            self.entry_value = 'Error'
            self.equation.set(self.entry_value)   # Display error message if evaluation fails.


# Creating a Tkinter root window
# (root window is the main window of the program).
root = Tk()
# Creating an instance of the calculator class.
calculator = Calculator(root)
root.mainloop()   # Instructing to run the Tkinter event loop.
