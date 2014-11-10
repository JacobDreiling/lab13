#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_rectangle(390,580,410,600, fill="red")

# Create your "enemies" here, before the class
enemyEins = drawpad.create_oval(50,50,119,188, fill="purple")
enemyZwei = drawpad.create_oval(50,200,188,269, fill="blue")

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "red")
       	    self.up.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.unter = Button(self.myContainer1)
       	    self.unter.configure(text="unter", background= "red")
       	    self.unter.grid(row=2,column=1)
       	    self.unter.bind("<Button-1>", self.unterClicked)
       	    
       	    self.linke = Button(self.myContainer1)
       	    self.linke.configure(text="linke", background= "red")
       	    self.linke.grid(row=1,column=0)
       	    self.linke.bind("<Button-1>", self.linkeClicked)
       	    
       	    self.recht = Button(self.myContainer1)
       	    self.recht.configure(text="recht", background= "red")
       	    self.recht.grid(row=1,column=2)
       	    self.recht.bind("<Button-1>", self.rechtClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    global enemyEins
	    global enemyZwei
	    # Remember to include your "enemies" with "global"
	    
	    # Uncomment this when you're ready to test out your animation!
	    #drawpad.after(10,self.animate)
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	   
	def unterClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	   
	def linkeClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	   
	def rechtClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
		

app = MyApp(root)
root.mainloop()