balance = 3200
balance1 = balance
rate = 10
annualInterestRate = 0.2

mensual = annualInterestRate/12

while True:
    balance = balance1
    for i in range(12):
        balance = balance - rate
        balance = balance + (mensual * balance)
    if balance <= 0:
        break
    else:
        rate += 10

print ('Lowest Payment: '+ str(rate))