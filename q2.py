import random
sticks = 21
userChoice = 1

def playGame():
    
    print('There are 21 sticks. You can pick from 1 to 4 sticks at a time, and the computer will then pick from 1 to 4 sticks at a time. Whoever picks the last stick loses!')
    while True:
        print('Current sticks: ' + str(sticks))
        userChoice = askUserChoice()
        if subtractSticks( subtractSticks.userChoice ):
            print('You lost!')
            break
        
        computerChoice = determineComputerChoice()
        print('Computer picked: ' + str(computerChoice) )
        if subtractSticks( computerChoice ):
            print('Computer lost!')
            break
        

def askUserChoice():

 while True:         
        print("How many sticks do you want to remove? (1-4)") #The player can pick between 1-4 sticks, unless there are less than 4 sticks remaining, then the player can only pick a max of how many sticks are left.
        subtractSticks.userChoice = int(input("Enter your choice: "))
        if subtractSticks.userChoice>=1 and subtractSticks.userChoice <= 4:  #determines if the number the player picked is a valid number.
            print("You have removed", subtractSticks.userChoice, "sticks") #if a valid number was chosen, it ends the loop
            
            break
        else:
            print ("You entered an invalid choice. Please remove 1-4 sticks") #if the player enters an invalid number, it will say this message and keep looping untill he enters a valid number.

       
def subtractSticks( number ):

    global sticks
    sticks -= subtractSticks.userChoice
    print("There are", sticks, "sticks left")
     if sticks > 0:
            False
    elif sticks <= 0:
        True
    
    
def determineComputerChoice():

    subtractSticks.Comp_choice = random.randint(1,4) #this makes the computer pick between 1-4 sticks    


