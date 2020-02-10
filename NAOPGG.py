#created and tested by CristenPerret. Goodluck Have fun GG!

import win32gui, win32con

import tkinter as tk
import webbrowser

NAOPGG ="https://na.op.gg/summoner/userName="
blackList = ["CristenPerret", "...", "replace with", "summonername", "andduopartners", "orfriends"]
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Search", command=self.on_button)
        self.button.pack()
        self.entry.pack()

    def on_button(self):
        cCounter = 0    
        nameList = []  #saved list of playernames
        chatLog = self.entry.get() # string from text field
        filtChatLog = chatLog.splitlines() # separate by line - - ["NAME has joined the lobby", ]
        for x in filtChatLog:
            chatLine = filtChatLog[cCounter] #ensures to loop to every row
            cCounter = cCounter + 1 #loop countr
            sSplitter = " joined the lobby" # first string to split from
            sSplitter2 = ":" #second string to split from
            if sSplitter in chatLine:
                pName = chatLine.split(sSplitter) # separates playername from joined the lobby
                nameList.append(pName[0]) # add the names to list of players
                print ("- - - - - - - -SERVER CONNECTION MESSAGE PARSED- - - - - - - -") #can remove
                print (nameList) # can remove
                uniqueName = set(nameList) #checks for duplicates 
                bName = [word for word in uniqueName if word not in blackList] # skips players listed
            if sSplitter2 in chatLine:
                pName = chatLine.split(sSplitter2)
                nameList.append(pName[0])
                print ("- - - - - - - -PLAYER CHAT MESSAGE PARSED- - - - - - - -")
                print (nameList)
                uniqueName = set(nameList)
                bName = [word for word in uniqueName if word not in blackList]
        else:
            print ("\n\nNow Opening Browser to these players NA.OP.GG Profiles")
            for i in bName:
                    print(NAOPGG + i)
                    webbrowser.open_new_tab(NAOPGG + i)                                                                         
                                           
hide_terminal = win32gui.GetForegroundWindow() # if you want to see the terminal remove
win32gui.ShowWindow(hide_terminal , win32con.SW_HIDE) # if you want to see the terminal remove
       


app = SampleApp()
app.mainloop()



#Below is a test string.
#save to clipboard, paste in the field,
#and press search to begin
'''
JannaBot joined the lobby
JannaBot: sup
NunuBot joined the lobby
NunuBot: this is a test string.
CristenPerret joined the lobby
LucianBot joined the lobby
BrandBot joined the lobby
LucianBot: ff@15
A Name Can Have Space joined the lobby
CristenPerret: GL HF!!
'''
