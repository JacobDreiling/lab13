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
directionE = 1
directionZ = 1
directionD = 1

# Create your "enemies" here, before the class
enemyEins = drawpad.create_oval(50,50,119,188, fill="purple")
enemyZwei = drawpad.create_oval(50,200,188,269, fill="blue")
enemyDrei = drawpad.create_oval(50,300,188,438, fill="green")

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.ueber = Button(self.myContainer1)
       	    self.ueber.configure(text="ueber", background= "red")
       	    self.ueber.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.ueber.bind("<Button-1>", self.ueberClicked)
       	    
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
       	    
       	def ueberClicked(self, event):   
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
	
def animateE():
	global drawpad
	global player
	global enemyEins
	global enemyZwei
	global enemyDrei
	global directionE
	# Remember to include your "enemies" with "global"
	Ex1, Ey1, Ex2, Ey2 = drawpad.coords(enemyEins)
        if Ex2 > int(drawpad.winfo_width())+69: 
            directionE = -869
        elif Ex1 < 0:
            directionE = 690
        drawpad.move(enemyEins,directionE,0)
        drawpad.after(20,animateE)
            
def animateZ():
	global drawpad
	global player
	global enemyEins
	global enemyZwei
	global enemyDrei
	global directionZ
        Zx1, Zy1, Zx2, Zy2 = drawpad.coords(enemyZwei)
        if Zx2 > int(drawpad.winfo_width())+138: 
            directionZ = -938
        elif Zx1 < 0:
            directionZ = 69
        drawpad.move(enemyZwei,directionZ,0)
        drawpad.after(20,animateZ)
            	    
def animateD():
	global drawpad
	global player
	global enemyEins
	global enemyZwei
	global enemyDrei
	global directionD
        Dx1, Dy1, Dx2, Dy2 = drawpad.coords(enemyDrei)
        if Dx2 > int(drawpad.winfo_width())+138: 
            directionD = -938
        elif Dx1 < 0:
            directionD = 6.9
        drawpad.move(enemyDrei,directionD,0)
	drawpad.after(20,animateD)
		
# call the animate function to start our recursion
animateE()
animateZ()
animateD()

app = MyApp(root)
root.mainloop()