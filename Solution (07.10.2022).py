import sys

def pairwiseInteractions(numOfObjects):
    r = 0       #R is the total distance between each object and is calculated below using the for loop.
    n = 0       #N becomes a counter which is used to as the exiting clause for the below for loop.
    for i in range(1,numOfObjects):
        n=i+1
        while True:
            pairwiseLength = float(input("Enter the distance between object " + str(i) + " and object " + str(n) + " in units of 10^-10m: "))
            r += pairwiseLength
            n+=1
            if n > numOfObjects:
                r = (r*(10**-10))
                break
    bindingEnergy(r)

def bindingEnergy(r):
    stdDev = float((3.41*(10**-10)))           #Constants are given. stdDev is Standard Deviation and is displayed as the lower case letter sigma in the formula.
    energyConstant = (1.65*(10**-21))   #energyConstant is displayed as the letter epsilon in the formula.
    u = 0                   #u is the binding energy value which is calculated by the formula.
    print("\nTwo values are given as constants in the equation; \nStandard Deviation, represented as the lower case sigma in the formula is " + str(stdDev) + "m. and;",
          " \nThe energy constant, displayed as epsilon in the formula is " + str(energyConstant) + "J.")
    print("\n")
    print("The calculated r value is: " + str(r) + "m.\n")
    print("The binding energy is: \n")
    u = (4*energyConstant*(((stdDev/r)**12)-((stdDev/r)**6)))       #This is the forumla for calculating the binding energy of objects wih r representing the sum of all pairwise interactions
    print(str(u) + "J.")

    while True:
        print("Would you like to calculate another value for a different set of objects?")
        decision = str(input("Enter Yes, or No: "))
        if decision == 'Yes' or decision == 'yes' or decision == 'y':
            begin()
        elif decision == 'No' or decision == 'no' or decision == 'n':
            sys.exit()



def begin():
    numOfObjects = 0
    while True:
        try:
            numOfObjects = int(input("Enter number of objects: ")) #Number of objects is inputted by the user and a compliance check is carried out to ensure it's an integer.
            if numOfObjects >= 2:
                pairwiseInteractions(numOfObjects)
            else:
                print("You have entered too few objects")          #Error checking 
        except(ValueError):
            print("You did not enter an integer.")

begin()

#I would have liked to have kept each individual pairwise length in an array so that if there were any inaccuracies in the program, the user could return to a certain 
#distance between two objects to input the data again. This would save time, instead of having to enter all of the individual distance values again. 

#I would have liked to have included a way to change the base 10 value for the unit input so that the user didn't have to calculate the values before inputting.
#In a team scenario perhaps I could have directed someone to work on a function which converts inputted units into the same base so the function used in this application can take the values
#and use them with the current state of the solution. 

#I would like to include writing the calculated value to either a CSV file or an Excel document. This would make moving the value around much easier. 
