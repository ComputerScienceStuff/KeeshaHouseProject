#Created using repl.it with the language Python
#Created 4/11/22
#Program will be used to help the homeless find resources to help them


#Imports
#we will be using tk as the base for UI
import tkinter as tk

from PIL import ImageTk, Image


#data storage
data = []
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

#
def saveAndRaise():
  saveInfo()
  raiseAll(questionsWindow, "nothing")

def saveInfo():
  #appending saved data
  global data
  userName = entNameQuestion.get()
  data.append(userName)
  userDOB = entDOBQuestion.get()
  data.append(userDOB)
  userAge = entAgeQuestion.get()
  data.append(userAge)
  userLoc = entLocQuestion.get()
  data.append(userLoc)
  userRea = entReaQuestion.get()
  data.append(userRea)
#raise the quetions window to collect needed information
def qRaise():
  raiseAll(questionsWindow, "nothing")
  
#raise the BMI menu
def bmiRaise():
  raiseAll(bmiMenu, "nothing")
  
#raise the main menu, this will be the core app
def mainRaise():
  raiseAll(mainMenu, "nothing")
#raise the meditation/prayer tab
def prayerRaise():
  global day
  if day == 1:
    print("Prayer/meditaion for day 1:")
    #https://connectusfund.org/10-strong-prayers-for-good-health
    print(meditation[day])
    print("")
    print("")
  elif day == 2:
    print("Prayer/meditaion for day 2:")
    #https://connectusfund.org/10-strong-prayers-for-good-health
    print(meditation[day])
    print("")
    print("")

  else:
    print("ERROR")

#raise the info tab to show user all submitted information
def giveInfo():
  global data
  print("Name: ", data[0])
  print("Weight: ", data[1])
  print("Height: ", data[2])
  print("Age: ", data[3])
  print("Management: ", data[5])
  print("")
  change = input("Would you like to change anything? (y/n) ")

  if change == "y":
    print("You can change the following: ")
    print("Name, Weight, Height, Age, Management ")
    toChange = input("What are we changing? ")
    if toChange == "Name":
      changeName = input("What would you like to change it to? ")
      areYouSure = input("Are you sure? (y/n) ")
      if areYouSure == "n":
        giveInfo()
      else:
        #replace name to new name using slicing
        data = data[:0] + [changeName] + data[0+1:]

    elif toChange == "Weight":
      changeWeight = float(input("What is your current weight now? "))
      areYouSure = input("Are you sure? (y/n) ")
      if areYouSure == "n":
        giveInfo()
      else:
        #replace weight to updated weight using slicing
        data = data[:1] + [changeWeight] + data[1 + 1:]
    elif toChange == "Height":
      changeHeight = float(input("What is your current height? "))
      areYouSure = input("Are you sure? (y/n) ")
      if areYouSure == "n":
        giveInfo()
      else:
        #replace height to updated height using slicing
        data = data[:2] + [changeHeight] + data[2 + 1:]
    elif toChange == "Age":
      changeAge = int(input("What is your current age? "))
      areYouSure = input("Are you sure? (y/n) ")
      if areYouSure == "n":
        giveInfo()
      else:
        #replace age to updated age using slicing
        data = data[:3] + [changeAge] + data[3 + 1:]
    elif toChange == "Management":
      print("What would you like to change your management to? ")
      print("Bulk, Cut, Maintain")
      changeManage = input("Choice: ")
      areYouSure = input("Are you sure? (y/n) ")
      if areYouSure == "n":
        giveInfo()
      else:
        #replace management to new management using slicing
        data = data[:5] + [changeManage] + data[5 + 1:]
      
  else:
    x = 0
    while x <= 20:
      print("")
      x += 1
    raiseAll(mainMenu, "nothing")
  x = 0
  while x <= 20:
    print("")
    x += 1

  

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
def tempTextA(x):
  entAgeQuestion.delete(0, "end")
def tempTextL(x):
  entLocQuestion.delete(0, "end")
def tempTextR(x):
  entReaQuestion.delete(0, "end")
#put multiple procedures into one procedure so it works
def calculateAndRaise():
  collectData()
  BMI()
  bmiRaise()

#go back to the main menu from other menus 
def goBack():
  raiseAll(mainMenu, "nothing")

def exersizeRaise():
  global data
  
  if data[5] == "Bulk":
    raiseAll(exersizeBulk, "nothing")
  elif data[5] == "Maintain":
    raiseAll(exersizeMaintain, "nothing")
  else:
    raiseAll(exersizeCut, "nothing")

def dietRaise():
  global data

  if data[5] == "Bulk":
    raiseAll(dietBulk, "nothing")
  elif data[5] == "Maintain":
    raiseAll(dietMaintain, "nothing")
  else:
    raiseAll(dietCut, "nothing")
#give user a disclosure on BMI
#information from
#https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator#:~:text=Body%20Mass%20Index%20is%20a,range%20is%2018.5%20to%2024.9.
def disclosure():
  print("*BMI is not used for muscle builders, long distance athletes, pregnant women, the elderly or young children.")
  print("")
  print("Further Information:")
  print("A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9. BMI applies to most adults 18-65 years.")
  print("")
  
  
#Used a procedure because tk wont work with just variables or code. 
def collectBMI():
  print(data[4])
  bmiMenu.tkraise()
  
#calulate BMI
def BMI():
  global data
  BMI = data[1]/(data[2]*data[2])

  #append data to a list so it can be used further on in the program
  data.append(round(BMI, 2))

#depending on what the user chose add that to data
def choseCut():
  global data, management
  management = "Cut"
  
  data.append("Cut")
  raiseAll(mainMenu, "nothing")
def choseBulk():
  global data, management
  management = "Bulk"
  data.append("Bulk")
  raiseAll(mainMenu, "nothing")
def choseMaintain():
  global data, management
  management = "Maintain"
  data.append("Maintain")
  raiseAll(mainMenu, "nothing")
def showInfo():
  #https://www.calculator.net/calorie-calculator.html
  print(info[0])
  print("")
  #https://www.who.int/news-room/fact-sheets/detail/healthy-diet
  print(info[1])
def questionsRaise():
  raiseAll(questionsWindow, "nothing")
    
# main window
root = tk.Tk()
root.wm_geometry("2960x1440")
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

#Ask user their age efin 2
ageQuestion = tk.Label(questionsWindow, text = "Enter your age below")
ageQuestion.pack()
entAgeQuestion = tk.Entry(questionsWindow, bd = 3)
entAgeQuestion.insert(0, "Enter current age")
entAgeQuestion.pack()
entAgeQuestion.bind("<FocusIn>", tempTextA)

#Ask the user their location efin 3
locQuestion = tk.Label(questionsWindow, text = "Enter your location")
locQuestion.pack()
entLocQuestion = tk.Entry(questionsWindow, bd = 3)
entLocQuestion.insert(0, "Enter your street address")
entLocQuestion.pack()
entLocQuestion.bind("<FocusIn>", tempTextL)

#Ask the user their current reasources efin 4
reaQuestion = tk.Label(questionsWindow, text = "Enter your current reasources")
reaQuestion.pack()
entReaQuestion = tk.Entry(questionsWindow, bd = 3)
entReaQuestion.insert(0, "Enter your current reasources")
entReaQuestion.pack()
entReaQuestion.bind("<FocusIn>", tempTextR)

#save all enteredsaveNameo
save = tk.Button(questionsWindow, text = 'Next', command = saveAndRaise)
save.pack()

'''
#Go to main app
mainApp = tk.Frame(root)
mainApp.grid(row = 0, column = 0, stick = 'news')

#give user the choice to see their BMI
post = tk.Button(mainApp, text = "Post")
post.grid(row = 1, column = 5)


#when the user clicks to see their BMI it will show up
find = tk.Button(mainApp, text = "Find")
find.grid(row = 1, column = 6)


########################################
#Left off on making the main app
######################################
#give user options on their weight management
weightchoose = tk.Label(bmiMenu, text = "vvv |Choose your weight management| vvv", font = "Arial")
weightchoose.grid(row = 3, column = 3)
#add bulking option, store the data to be used later in the code
btnBulk = tk.Button(bmiMenu, text = "Bulk", command = choseBulk)
btnBulk.grid(row = 5, column = 2)
#explain what bulking is incase user does not know
explBulk = tk.Label(bmiMenu, text = "Bulking is gaining weight")
explBulk.grid(row = 6, column = 2)
#add maintaining option, store the data to be used later in the code
btnMaintain = tk.Button(bmiMenu, text = "Maintain", command = choseMaintain)
btnMaintain.grid(row = 5, column = 3)
#explain what maintaining is incase user does not know
explMaintain = tk.Label(bmiMenu, text = "Maintaining is keeping weight")
explMaintain.grid(row = 6, column = 3)
#add cutting option, store the data to be used later in the code
btnCut = tk.Button(bmiMenu, text = "Cut", command = choseCut)
btnCut.grid(row = 5, column = 4)
#explain what Cutting is incase user does not know
explCut = tk.Label(bmiMenu, text = "Cutting is losing weight")
explCut.grid(row = 6, column = 4)


#Show user their information
discloserMessage = tk.Button(bmiMenu, text = "Discloser", command = disclosure)
discloserMessage.grid(row = 10, column = 3)

#give user option to change their information




#The "mainMenu" will be the main part of the app, all of the information collection was collected in the beginning of the app, we can now use the information collected and stored in "data"

mainMenu = tk.Frame(root)
mainMenu.grid(row = 0, column = 0, stick = 'news')


#exersizes button/choice

#attaching an image to a variable to be used in the code

#image found at https://youtu.be/I9uVg-feZoM
exersizeImg = (Image.open("pictures/icons/exersize.png"))
#resizing the image so that it fits with the other images
resizeExersizeImg = exersizeImg.resize((150, 150), Image.ANTIALIAS)
#assigning the resized image to the originial variable
exersizeImg = ImageTk.PhotoImage(resizeExersizeImg)
#display the image using a label 
showImg = tk.Label(mainMenu, image = exersizeImg)
showImg.grid(row = 2, column = 2)

#add a button so the user can see their daily exersize
btnExersize = tk.Button(mainMenu, text = "Exercises", command = exersizeRaise)
btnExersize.grid(row = 3, column = 2)


#diet button/choice

#attaching an image to a variable to be used in the code
#image found at https://upload.wikimedia.org/wikipedia/commons/7/73/Apple_clipart.png
dietImg = (Image.open("pictures/icons/Apple.png"))
#resizing the image so that it fits with the other images
resizeDietImg = dietImg.resize((150, 150), Image.ANTIALIAS)
#assigning the resized image to the originial variable
dietImg = ImageTk.PhotoImage(resizeDietImg)
#display the image using a label
showImg = tk.Label(mainMenu, image = dietImg)
showImg.grid(row = 2, column = 7)

#add a button so the user can see their diet
btnDiet = tk.Button(mainMenu, text = "Diet", command = dietRaise)
btnDiet.grid(row = 3, column = 7)



#prayer/meditation button/choice
#attaching an image to a variable to be used in the code
#image found at https://static.thenounproject.com/png/51613-200.png
meditationImg = (Image.open("pictures/icons/meditation.png"))
#resizing the image so that it fits with the other images
resizeMeditationImg = meditationImg.resize((150, 150), Image.ANTIALIAS)
#assigning the resized image to the originial variable
meditationImg = ImageTk.PhotoImage(resizeMeditationImg)
#display the image using a label
showImg = tk.Label(mainMenu, image = meditationImg)
showImg.grid(row = 2, column = 10)

#add a button so the user can see their daily meditation
btnMeditation = tk.Button(mainMenu, text = "Meditation", command = prayerRaise)
btnMeditation.grid(row = 3, column = 10)

#info button will show user their collected info and give them the option to update it
btnInfo = tk.Button(mainMenu, text = "I", command = giveInfo)
btnInfo.grid(row = 1, column = 1)

#exersize frame that will show user their exersizes based on what choice of management they had

#exersizes for bulking

exersizeBulk = tk.Frame(root)
exersizeBulk.grid(row = 0, column = 0, sticky = 'news')


#X button to go back to the main menu
returnMain = tk.Button(exersizeBulk, text = "X", command = goBack)
returnMain.grid(row = 1, column = 1)

#exersizes for maintaining
exersizeMaintain = tk.Frame(root)
exersizeMaintain.grid(row = 0, column = 0, sticky = 'news')

#1st exersize

#attaching an image to a variable to be used in the code

#image found at https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsQl1GHC_jYi792PjFGFryM6OGUthVGCbdljHokDJVNL0smFDETTEL_k-bPS0nH5Jd7wQ&usqp=CAU
exersizeExampleImg = (Image.open("pictures/exersizePictures/pushup.png"))
#resizing the image so that it fits with the other images
resizeExersizeExampleImg = exersizeExampleImg.resize((150, 150), Image.ANTIALIAS)
#assigning the resized image to the originial variable
exersizeExampleImg = ImageTk.PhotoImage(resizeExersizeExampleImg)
#display the image using a label 
showImg = tk.Label(exersizeMaintain, image = exersizeExampleImg)
showImg.grid(row = 3, column = 2)

#tell user how many sets x reps to do 
howMany = tk.Label(exersizeMaintain, text = "8 - 12 reps, pushups | if too hard do use knees")
howMany.grid(row = 4, column = 2)

#tell user the exersize name
exersizeName = tk.Label(exersizeMaintain, text = "Push-ups")
exersizeName.grid(row = 2, column = 2)


#2nd exersize

#attaching an image to a variable to be used in the code
#image found at https://cdn.iconscout.com/icon/premium/png-256-thumb/pull-up-1481035-1253869.png
exersizeExampleImg2 = (Image.open("pictures/exersizePictures/pullup.png"))
#resizing the image so that it fits with the other images
resizeExersizeExampleImg2 = exersizeExampleImg2.resize((150, 150), Image.ANTIALIAS)
#assigning the resized image to the originial variable
exersizeExampleImg2 = ImageTk.PhotoImage(resizeExersizeExampleImg2)
#display the image using a label
showImg = tk.Label(exersizeMaintain, image = exersizeExampleImg2 )
showImg.grid(row = 3, column = 5)

#tell user how many sets x reps to do 
howMany = tk.Label(exersizeMaintain, text = "2x 8 - 12 reps")
howMany.grid(row = 4, column = 5)

#tell user the exersize name
exersizeName = tk.Label(exersizeMaintain, text = "Pull-ups")
exersizeName.grid(row = 2, column = 5)

#X button to go back to the main menu
returnMain = tk.Button(exersizeMaintain, text = "X", command = goBack)
returnMain.grid(row = 1, column = 1)

#exersizes for cutting
exersizeCut = tk.Frame(root)
exersizeCut.grid(row = 0, column = 0, sticky = 'news')


#X button to go back to the main menu
returnMain = tk.Button(exersizeCut, text = "X", command = goBack)
returnMain.grid(row = 1, column = 1)



#diet will show their diet based on what management they have

#diet for bulking
dietBulk = tk.Frame(root)
dietBulk.grid(row = 0, column = 0, sticky = 'news')


#X button to go back to the main menu
returnMain = tk.Button(dietBulk, text = "X", command = goBack)
returnMain.grid(row = 1, column = 1)

#diet for maintaining
dietMaintain = tk.Frame(root)
dietMaintain.grid(row = 0, column = 0, sticky = 'news')
#attaching an image to a variable to be used in the code
#image found at 
goodDiet = (Image.open("pictures/exersizePictures/fullmeal.jpg"))
#resizing the image so that it fits with the other images
resizeGoodDiet = goodDiet.resize((450, 350), Image.ANTIALIAS)
#assigning the resized image to the originial variable
goodDiet = ImageTk.PhotoImage(resizeGoodDiet)

#display the image using a label
showImg = tk.Label(dietMaintain, image = goodDiet)
showImg.grid(row = 2, column = 4)

#additional info button so user can learn why it's healthy
more = tk.Button(dietMaintain, text = "MORE", command = showInfo)
more.grid(row = 2, column = 5)
#X button to go back to the main menu
returnMain = tk.Button(dietMaintain, text = "X", command = goBack)
returnMain.grid(row = 1, column = 1)


#diet for cutting
dietCut = tk.Frame(root)
dietCut.grid(row = 0, column = 0, sticky = 'news')






#X button to go back to the main menu
returnMain = tk.Button(dietCut, text = "X", command = goBack)
returnMain.grid(row = 1, column = 1)

'''

#raising frames so it renders right

raiseAll(menuWindow, questionsWindow)

root.mainloop()