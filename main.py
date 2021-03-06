#Created using repl.it with the language Python
#Created 4/11/22
#Program will be used to help the homeless find resources to help them


#Imports
#we will be using tk as the base for UI
import tkinter as tk
from PIL import ImageTk, Image


#data storage
posts = []
'''
0 = Type
1 = Location
2 = Expiration
'''
data = [0, 1, 2, 3, 4]
'''
0 = name
1 = dob
2 = age
3 = location(city)
4 = current resources
'''

#Used Procedures

#raise frame functions

#raise the loading window and save the name, a functions calling 2 functions so it works with tk
awesome = ""
#
def saveAndRaise():
  saveInfo()
  raiseAll(chooseCounty, "nothing")

postNumber = 2

type = ""
location = ""
expiration = ""
def postNew():
  global type, location, expiration, postNumber
  #get all info inputted and add it to a list to save
  type = entTypeResource.get()
  location = entLocResource.get()
  expiration = entExResource.get()

  allVars = "Type: " + type + "\n Location: " + location + "\n Expiration: " + expiration
  newPost.config(text = allVars)
  postNumber += 1
  raiseMain()


def saveInfo():
  #appending saved data
  global data
  userName = entNameQuestion.get()
  data[:0] + [userName] + data[0 + 1:]
  userDOB = entDOBQuestion.get()
  data[:1] + [userDOB] + data[1 + 1:]
  userRea = entReaQuestion.get()
  data[:2] + [userRea] + data[2 + 1:]
  
#raise the quetions window to collect needed information
def qRaise():
  raiseAll(questionsWindow, "nothing")


#instead of typing the same thing over and over again using a procedure to raise the frames would be easier 
def raiseAll(raisingFrame, frameRaisingFrameInFront):
  #x is the frame that will be raised in front of "y" which is the frame "x" is being raised in front of
  if frameRaisingFrameInFront == "nothing":
    raisingFrame.tkraise()
  else:
    raisingFrame.tkraise(frameRaisingFrameInFront)
    
#temporary text, polish
def tempTextW(x):
  entNameQuestion.delete(0, "end")
def tempTextDOB(x):
  entDOBQuestion.delete(0, "end")
def tempTextR(x):
  entReaQuestion.delete(0, "end")

#raising functions
def questionsRaise():
  raiseAll(questionsWindow, "nothing")
def raiseMain():
  raiseAll(mainApp, "nothing")
def goPosting():
  global awesome
  raiseAll(postingFrame, "nothing")
  doThis.destroy()
  awesome = tk.Label(mainApp, text = "Good Job! Now homeless people are helped!")
  awesome.grid(row = 2, column = 1)
#go back to main app
def goBack():
  raiseAll(mainApp, "nothing")

def goFind():
  raiseAll(findingFrame, "nothing")
# main window
root = tk.Tk()
root.wm_geometry("1600x2960")
root.winfo_toplevel().title("BlueDoor")
menuWindow = tk.Frame(root)
menuWindow.grid(row = 0, column = 0, stick = 'news')


#title screen

#attaching an image to a variable to be used in the code
#image found at https://img.rawpixel.com/s3fs-private/rawpixel_images/website_content/frbuilding_home_door_blue-image-kybe55fs.jpg?w=800&dpr=1&fit=default&crop=default&q=65&vib=3&con=3&usm=15&bg=F4F4F3&ixlib=js-2.2.1&s=4ef43764da9bcf7b22f6f4e1c1bda729
door = (Image.open("pictures/KeeshasDoor.png"))
resizeDoor = door.resize((225, 377))

door = ImageTk.PhotoImage(resizeDoor)

#display the image using a label
showImg = tk.Label(menuWindow, image = door)
showImg.grid(row = 2, column =5)


#enter button
enterB = tk.Button(menuWindow, text='Search', command = questionsRaise)
enterB.grid(row = 3, column = 5)


#ask for important info that will be used later in the program
questionsWindow = tk.Frame(root)
questionsWindow.grid(row = 0, column = 0, stick = 'news')


#Ask user their name
nameQuestion = tk.Label(questionsWindow, text = "Enter your name")
nameQuestion.pack()
entNameQuestion = tk.Entry(questionsWindow, bd = 3)
entNameQuestion.insert(0, "Enter - (First Name, Last Name")
entNameQuestion.pack()
entNameQuestion.bind("<FocusIn>", tempTextW)


#Enter in your Date of Birth!(dob) efin 1
dobQuestion = tk.Label(questionsWindow, text = "Enter your date of birth below")
dobQuestion.pack()
entDOBQuestion = tk.Entry(questionsWindow, bd = 3)
entDOBQuestion.insert(0, "Enter in 00/00/0000 format")
entDOBQuestion.pack()
entDOBQuestion.bind("<FocusIn>", tempTextDOB)

#Ask the user their current reasources efin 4
reaQuestion = tk.Label(questionsWindow, text = "Enter your current reasources")
reaQuestion.pack()
entReaQuestion = tk.Entry(questionsWindow, bd = 3)
entReaQuestion.insert(0, "Enter your current reasources")
entReaQuestion.pack()
entReaQuestion.bind("<FocusIn>", tempTextR)

#save all entered things
save = tk.Button(questionsWindow, text = 'Next', command = saveAndRaise)
save.pack()


#choosing where person lives

chooseCounty = tk.Frame(root)
chooseCounty.grid(row = 0, column = 0, stick = 'news')

chooseSomething = tk.Label(chooseCounty, text = "Choose your location, this will be used to find potential helpful resources")


choiceCountry = tk.StringVar()
choiceCountry.set("United States")
dropDownCountry = tk.OptionMenu(chooseCounty, choiceCountry, "Canada", "United States", "Mexico")
dropDownCountry.grid(row = 1, column = 2)



choiceState = tk.StringVar()
choiceState.set("Indiana")
dropDownState = tk.OptionMenu(chooseCounty, choiceState, "Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi")
dropDownState.grid(row = 2, column = 2)

choiceCounty = tk.StringVar()
choiceCounty.set("Allen")
dropDownCounty = tk.OptionMenu(chooseCounty, choiceCounty, "Adams","Allen","Barthoomew","Benton","Blackford","Boone","Brown","Carroll","Cass","Clark","Clay","Clinton","Crawford","Daviess")
dropDownCounty.grid(row = 3, column = 2)

enterLoc = tk.Button(chooseCounty, text = "Confirm", command = raiseMain)
enterLoc.grid(row = 4, column = 2)


#Go to main app
mainApp = tk.Frame(root)
mainApp.grid(row = 0, column = 0, stick = 'news')

welcome = tk.Label(mainApp, text = "Welcome to the BlueDoor Main Page, here you can find avaliable resources for your needs!")
welcome.grid(row = 1, column = 1)

doThis = tk.Label(mainApp, text = "It seems that there are no posts right now, make a post to help the needy")
doThis.grid(row = 2, column = 1)


newPost = tk.Label(mainApp, text = "")
newPost.grid(row = postNumber + 1, column = 4)

def destroyPost():
  global awesome
  newPost.config(text = " ")
  awesome.destroy()
  raiseAll(mainApp, "nothing")


#give user the choice to see their BMI
post = tk.Button(mainApp, text = "Post", command = goPosting)
post.grid(row = 1, column = 5)

  
postingFrame = tk.Frame(root)
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

delPost = tk.Button(postingFrame, text = "Delete Past Post", command = destroyPost)
delPost.grid(row = 10, column = 6)
#x button so user can go back
xButton = tk.Button(postingFrame, text = "x", command = goBack)
xButton.grid(row = 1, column = 1)


#when the user clicks to see their BMI it will show up
find = tk.Button(mainApp, text = "Find", command = goFind)
find.grid(row = 1, column = 6)

findingFrame = tk.Frame(root)
findingFrame.grid(row = 0, column = 0, stick = 'news')

#when button is clicked pull up a splash screen as a loading screen


loadingScreen = tk.Label(findingFrame, text = "Loading avaliable resources")
loadingScreen.grid(row = 5, column = 5)


goBackToMain = tk.Button(findingFrame, text = "Load!", command = raiseMain)
goBackToMain.grid(row = 6, column = 5)

#x button so user can go back
xButton = tk.Button(findingFrame, text = "x", command = goBack)
xButton.grid(row = 1, column = 1)


#raising frames so it renders right
raiseAll(menuWindow, "nothing")
root.mainloop()