from tkinter import *

fenetre = Tk()
fenetre.config(height=500,width=500)
c = Canvas(fenetre,height=1000,width=1000)
c.pack()

proposer_red = c.create_oval(20,20,40,40,fill="red")
proposer_orange = c.create_oval(60,20,80,40,fill="orange")
proposer_yellow = c.create_oval(100,20,120,40,fill="yellow")

proposer_blue = c.create_oval(20,60,40,80,fill="blue")
proposer_cyan = c.create_oval(60,60,80,80,fill="cyan")
proposer_green = c.create_oval(100,60,120,80,fill="green")

proposer_pink = c.create_oval(20,100,40,120,fill="pink")
proposer_violet = c.create_oval(60,100,80,120,fill="violet")

def UwU(event):
    print("UwU")

c.tag_bind(proposer_red, '<1>', UwU)
c.tag_bind(proposer_orange, '<1>', UwU)
c.tag_bind(proposer_yellow, '<1>', UwU)
c.tag_bind(proposer_blue, '<1>', UwU)
c.tag_bind(proposer_cyan, '<1>', UwU)
c.tag_bind(proposer_green, '<1>', UwU)
c.tag_bind(proposer_pink, '<1>', UwU)
c.tag_bind(proposer_violet, '<1>', UwU)


fenetre.mainloop()