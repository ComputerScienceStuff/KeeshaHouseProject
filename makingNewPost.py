#Go to main app
mainApp = tk.Frame(root3)
mainApp.grid(row = 0, column = 0, stick = 'news')

#empty labels to push post and find over
#row 1, column < 5
KillMartin = tk.Label(mainApp, text = "            ")
KillMartin.grid(row = 1, column = 1)
KidnapFamily = tk.Label(mainApp, text = "                  ")
KidnapFamily.grid(row = 1, column = 2)
BuyVan = tk.Label(mainApp, text = "                       ")
BuyVan.grid(row = 1, column = 3)
RunVanOffHighway = tk.Label(mainApp, text = "                                       ")
RunVanOffHighway.grid(row = 1, column = 4)


#give user the choice to see their BMI
post = tk.Button(mainApp, text = "Post", command = goPosting)
post.grid(row = 1, column = 5)

  
postingFrame = tk.Frame(root3)
postingFrame.grid(row = 0, column = 0, stick = 'news')


typeResource = tk.Label(postingFrame, text = "Type")
typeResource.grid(row = 4, column = 5)

entTypeResource = tk.Entry(postingFrame)
entTypeResource.grid(row = 5, column = 5)

locResource = tk.Label(postingFrame, text = "Location")
locResource.grid(row = 6, column = 5)

entLocResource = tk.Entry(postingFrame)
entLocResource.grid(row = 7, column = 5)

exResource = tk.Label(postingFrame, text = "When does it expire")
exResource.grid(row = 8, column = 5)

entExResource = tk.Entry(postingFrame)
entExResource.grid(row = 9, column = 5)

postButton = tk.Button(postingFrame, text = "Post!", command = postNew)
postButton.grid(row = 10, column = 5)

#x button so user can go back
xButton = tk.Button(postingFrame, text = "x", command = goBack)
xButton.grid(row = 1, column = 1)


#when the user clicks to see their BMI it will show up
find = tk.Button(mainApp, text = "Find", command = goFind)
find.grid(row = 1, column = 6)

findingFrame = tk.Frame(root3)
findingFrame.grid(row = 0, column = 0, stick = 'news')

#when button is clicked pull up a splash screen as a loading screen


loadingScreen = tk.Label(findingFrame, text = "Loading avaliable resources")
loadingScreen.grid(row = 5, column = 5)
root3.after(5)

  


goBackToMain = tk.Button(findingFrame, text = "Load!", command = recreate)
goBackToMain.grid(row = 6, column = 5)

#then after a certain amount of time show the user found results. 

#get the info
with open("newPost" + str(postNumber - 2), 'r') as myfile:
  for post in myfile:
    posts.append(post)
#display the info
class newPost:
  def __init__(self, master):
    info = ""
    with open("newPost" + str(postNumber - 2), "r") as f:
      info = f.read()
    self.post = self.Label(master, text = "")
    self.grid(row = postNumber, column = 2)

    self.post.config(text = info)

 
#x button so user can go back
xButton = tk.Button(findingFrame, text = "x", command = goBack)
xButton.grid(row = 1, column = 1)
raiseAll(mainApp, "nothing")
posting = newPost(root3)
root3.mainloop()
