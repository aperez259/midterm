import random
sticks = 21

def playGame():
    global sticks
    
    print('There are 21 sticks. You can pick from 1 to 4 sticks at a time, and the computer will then pick from 1 to 4 sticks at a time. Whoever picks the last stick loses!')
    while True:
        print('Current sticks: ' + str(sticks))
        userChoice = askUserChoice()
        if subtractSticks( userChoice ):
            print('You lost!') 
            break
        
        computerChoice = determineComputerChoice()
        print('Computer picked: ' + str(computerChoice) )
        if subtractSticks( computerChoice ):
            print('Computer lost!')
            break

def askUserChoice():

    YourChoice = ''
    
    while True:
        print("How many sticks do you want to pick up? (1-4)")
        YourPick = int(input("Enter your choice: "))
        if YourPick in range (1,5):  #determines if the number the player picked is a valid number.
            print("You have removed", YourPick, "sticks") 
            return YourPick #if a valid number was chosen, it ends the loop

        else: #if the player enters an invalid number, this message will keep looping untill they enter a valid number.
            print ("You entered an invalid choice. Please remove 1-4 sticks") 


       
def subtractSticks( number ):
    global sticks
    sticks -= number # thissubtracts the number parameter, which are the number choice and computer choice), from the global vlue sticks.


    if sticks <= 0: #if the total value in sticks reaches zero or below, it returns true.
        return True
    else: # if the value of sticks remains above 0, then the it returns false.
        return False


def determineComputerChoice():
    import random
    ComputerPick = random.randint(1,4) #this will make the computer pick a random number between 1-4
    return ComputerPick 

