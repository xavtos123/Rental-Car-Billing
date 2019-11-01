import sys
'''
Section 1: Collect customer input
'''
##1)       Request Rental code:
#Prompt --> "(B)udget, (D)aily, or (W)eekly rental?"
#rentalCode = ?
rentalCode = input('(B)udget, (D)aily, or (W)eekly rental?')
#2)         Request time period the car was rented.

#Prompt --> "Number of Days Rented:"k daysRented = ?
                   #
                   #OR
#Prompt --> "Number of Weeks Rented:"
#weeksRented = ?
              
if rentalCode == 'B' or rentalCode == 'D':
    daysRented = int(input('number of Days Rented:'))
else:
    weeksRented = int(input('Number of Weeks Rented:'))

#CUSTOMER DATA CHECK 1
#ADD CODE HERE TO PRINT:
print ('Rental Code: ',rentalCode)
if rentalCode == 'B' or rentalCode == 'D':
    print ('Number of days rented: ',daysRented)
else:
    print ('Number of weeks rented: ',weeksRented)

#3) Set the base charge for the rental type as the variable baseCharge.
#The base charge is the rental period * the appropriate rate:
budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00

if rentalCode == 'B':
    baseCharge= daysRented * 40.00
elif rentalCode == 'D':
    baseCharge=daysRented * 60.00
elif rentalCode == 'W':
    baseCharge=weeksRented * 190.00

#4) Collect Mileage information:
#a)Prompt the user to input the starting odometer reading and store it as the variable odoStart
#Prompt -->"Starting Odometer Reading:\n"
odoStart = int(input("Enter the starting odometer reading: "))
#b)Prompt the user to input the ending odometer reading and store it as the variable odoEnd
#Prompt -->"Ending Odometer Reading:"
odoEnd = int(input("Enter the ending odometer reading: "))
#CUSTOMER DATA CHECK 2
#ADD CODE HERE TO PRINT:
print ('Odometer starting: ',odoStart)
print ('Odometer ending: ',odoEnd)
print ('Base charge: ',baseCharge)
'''
Section 2: Calculate the costs from the customer input
'''
#1)         Calculate the mileage.
#a)         Calculate the total mileage:
#   ending odometer reading - starting odometer reading
#   and store it as the variable totalMiles
totalMiles= odoEnd - odoStart
#2)         Calculate the mileage charge and store it as
#     the variable mileCharge:
#a)         Code 'B' (budget) mileage charge: $0.25 for each mile driven
if rentalCode == 'B':
    mileCharge=totalMiles * 0.25
#b)         Code 'D' (daily) mileage charge: no charge if the average
#   number of miles driven per day is 100 miles or less;
#   i)        Calculate the averageDayMiles (totalMiles/daysRented)
if rentalCode == 'D':
    averageDayMiles = totalMiles /daysRented
#   ii)       If averageDayMiles is above the 100 mile per day
#       limit:
#     (1) calculate extraMiles (averageDayMiles - 100)
#     (2) mileCharge is the charge for extraMiles,
#         $0.25 for each mile
    if averageDayMiles > 100:
         extraMiles = averageDayMiles -100
         mileCharge= extraMiles * 0.25
    else:
        mileCharge=0

#c)          Code 'W' (weekly) mileage charge: no charge if the
#   average number of miles driven per week is
#   900 miles or less;
#   i)        Calculate the averageWeekMiles (totalMiles/ weeksRented)
if rentalCode == 'W':
    averageWeekMiles = totalMiles /weeksRented
#   ii)       mileCharge is $100.00 per week if the average number of miles driven per week exceeds 900 miles
    if averageWeekMiles > 900:
         mileCharge= weeksRented * 100
    else:
        mileCharge=0
'''
Section 3: Display the results to the customer
'''
#1) Calculate the Amount Due as the variable amtDue
#   This is the base charge + mile charge
amtDue = baseCharge + mileCharge
#2. Display the results of the rental calculation:
#Customer Summary
print('\nCustomer Summary')
#Rental Code:
print ('Rental Code: ',rentalCode)
#Days Rented:
if rentalCode == 'B' or rentalCode == 'D':
    print('Days Rented:', daysRented)
else:
    print('Weeks Rented:', weeksRented)
#Starting Odometer:
print ('Odometer starting: ',odoStart)
#Ending Odometer:
print ('Odometer ending: ',odoEnd)
#Miles Driven:
print ('Total Miles: ',totalMiles)
#Amount Due:
print ('Total Amount: $%.2f' % (amtDue))