import q1
import q2

def testQ1():
    balances = {1000, 600, 25, 8}
    for balance in balances:
        print('\tRunning with a balance of $' + str(balance) + ', your program returned: $' + str(q1.computeMinimumPayment( balance )))

print('Q1:')
testQ1()
    
print('Q2:')
q2.playGame()

