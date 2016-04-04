sticks = 21

def playGame():
    global sticks
    
    print('There are 21 sticks. You can pick from 1 to 4 sticks at a time, and the computer will then pick from 1 to 4 sticks at a time. Whoever picks the last stick loses!')
    while True:
        print('Current sticks: ' + str(sticks))
        userChoice = askUserChoice()
        
        sticks -= askUserChoice.userChoice #subtracts the sticks that the player removed
        if sticks <= 0: #checks to see if there are 0 sticks left and if so, prints out a 'you lost' message
            print('You lost!')
            break
        
        computerChoice = determineComputerChoice()
        print('Computer picked: ' + str(determineComputerChoice.computerChoice))

        sticks -= determineComputerChoice.computerChoice #subtracts the sticks that the computer removed
        if sticks <= 0: #checks to see if there are 0 sticks left and if so, prints out a 'computer lost' message
            print('Computer lost!')
            break
        

def askUserChoice():
    
 while True:         
        print("How many sticks do you want to pick up? (1-4)")
        askUserChoice.userChoice = int(input("Enter your choice: ")) #
        if askUserChoice.userChoice >=1 and askUserChoice.userChoice <= 4:  #determines if the number the player picked is a valid number.
            print("You have removed", askUserChoice.userChoice, "sticks") #if a valid number was chosen, it ends the loop
            break
        else: #if the player enters an invalid number, this message will keep looping untill they enter a valid number.
            print ("You entered an invalid choice. Please remove 1-4 sticks") 


       
def subtractSticks( number ): # moved subtract sticks within the playGame function.
    global sticks
 


def determineComputerChoice():
    import random
    determineComputerChoice.computerChoice = random.randint(1,4) #this will make the computer pick a random number between 1-4


