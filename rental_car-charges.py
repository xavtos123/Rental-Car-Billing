import sys
'''
Section 1: Collect customer input
'''

##Collect Customer Data - Part 1

##1)	Request Rental code:
#Prompt --> "(B)udget, (D)aily, or (W)eekly rental?"
#rentalCode = ?

#2)	Request time period the car was rented.

#Prompt --> "Number of Days Rented:"
#rentalPeriod = ?
#	OR
#Prompt --> "Number of Weeks Rented:"
#rentalPeriod = ?

#CUSTOMER DATA CHECK 1
#ADD CODE HERE TO PRINT:
#rentalCode
#rentalPeriod
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

if rentalCode == "W":
    rentalPeriod = int(input("Number of Weeks Rented:\n"))
else:
    rentalPeriod = int(input("Number of Days Rented:\n"))
print(rentalCode)
print(rentalPeriod)
#3) Set the base charge for the rental type as the variable baseCharge. 
#The base charge is the rental period * the appropriate rate:

budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00	

if rentalCode == "B":
    baseCharge = budgetCharge * rentalPeriod
elif rentalCode == "D":
    baseCharge = dailyCharge * rentalPeriod
else:
    baseCharge = weeklyCharge * rentalPeriod

##baseCharge = ?
if rentalCode == 'B':
    baseCharge = rentalPeriod * budgetCharge
odoStart = int(input("Starting Odometer Reading:\n"))
odoEnd = int(input("Ending Odometer Reading:\n"))
totalMiles = odoEnd - odoStart
print(odoStart)
print(odoEnd)

#Collect Customer Data - Part 2

#4)Collect Mileage information:
#a)	Prompt the user to input the starting odometer reading and store it as the variable odoStart

#Prompt -->"Starting Odometer Reading:\n"
# odoStart = ?


#b)	Prompt the user to input the ending odometer reading and store it as the variable odoEnd

#Prompt -->"Ending Odometer Reading:"
# odoEnd = ?

#CUSTOMER DATA CHECK 2
#ADD CODE HERE TO PRINT:
#odoStart
#odoEnd
#baseCharge

'''
Section 2: Calculate the costs from the customer input
'''

#Calculate Charge 1

#1)	Calculate the mileage.
#a)	Calculate the total mileage: 
#   ending odometer reading  - starting odometer reading 
#   and store it as the variable totalMiles

# totalMiles = ?

# Calculate Charges 2

##2)	 Calculate the mileage charge and store it as 
#     the variable mileCharge:

#a)	Code 'B' (budget) mileage charge: $0.25 for each mile driven

#b)	Code 'D' (daily) mileage charge: no charge if the average
#   number of miles driven per day is 100 miles or less;
#   i)	Calculate the averageDayMiles (totalMiles/rentalPeriod)

#   ii)	If averageDayMiles is above the 100 mile per day
#       limit:
#     (1)	calculate extraMiles (averageDayMiles  - 100)
#     (2)	mileCharge is the charge for extraMiles, 
#         $0.25 for each mile


#c)	Code 'W' (weekly) mileage charge: no charge if the 
#   average number of miles driven per week is 
#   900 miles or less;
 
#   i)	Calculate the averageWeekMiles (totalMiles/ rentalPeriod)

#   ii)	mileCharge is $100.00 per week if the average number of miles driven per week exceeds 900 miles


'''
Section 3: Display the results to the customer
'''
#1) Calculate the Amount Due as the variable amtDue
#   This is the base charge + mile charge

#2. Display the results of the rental calculation:

#Rental Summary
#Rental Code: 
#Rental Period: 
#Starting Odometer: 
#Ending Odometer: 
#Miles Driven: 
#Amount Due: 