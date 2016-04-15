def computeMinimumPayment( balance ):

    if balance <= 10:
      return (balance) #if your balance is $10 or below, your minimum payment will be the balance.
    elif balance > 10 and int(balance)*.021 <= 10 :
      return (10) #if your balance is higher than $10 and also $10 is higher than 2.1% of your balance, then your minimum payment will be $10.
    elif int(balance)*.021 > 10 :
      return (int(balance) * .021) #if 2.1% of your balance is higher than $10, your minimum payment will be 2.1% of your balance.

