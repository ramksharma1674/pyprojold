print("The Miles Per Gallon program\n\n")


while True:
    miles = float(input("Enter miles driven:\t\t"))

    while (miles <=0):
        print("Numbe of miles can not be 0 or less, please try again.\n")
        miles = float(input("Enter miles driven:\t\t"))

    gas = float(input("Enter gallon of gas used:\t"))


    while (gas <=0):
        print("Numbe of gallons can not be 0, please try again.\n")
        gas = float(input("Enter gallon of gas used:\t"))
    
    cost = float(input("Enter cost per gallon of gas:\t"))


    while (cost <=0):
        print("Cost per gallon can not be 0, please try again.\n")
        cost = float(input("Enter cost per gallon of gas:\t"))
    
    milespergallon = round((miles/gas),2)
    print("\nMiles Per Gallon:\t\t", milespergallon)

    gascost = round(cost * milespergallon,2)
    print("\nTotal gas cost:\t\t", gascost)
    
    costpermile = round(cost  / milespergallon ,2)
    print("\nCost per mile:\t\t", costpermile)
    
    resp = input("Get entries for another trip (y/n) ?")
    if resp.lower() == 'n':
        break

print()
print("Bye")


cntr = 0

while (cntr <= 5):
    print(cntr, end=" ")
    cntr += 1
print("Conuter is over ")    
#a=9
#if (a<10):
#    print(" a is less then 10")
#    print("a is 9")
#else:
#    print("else part")    


import _locale

# set locale for use in currency formatting

result = _locale.setlocale(_locale.LC_ALL, '')
if result == 'C':
    _locale.setlocale(_locale.LC_ALL, 'en_US')

print("Welcome to future value calculator")
print()

choice = "y"

while choice.lower() == "y":

    mon_inv = float(input("Enter monthly investment: \t"))
    yr_int_rate = float(input("Enter yearly interest rate: \t"))
    years = int(input("Enter Number of Years: \t"))
    
    # convert yearly values to monthly values
    mon_int_rate= yr_int_rate / 12 /100
    months = years * 12
    
    # calculate
    future_value = 0
    for i in range(months):
        future_value = future_value + mon_inv
        mon_int_amount = future_value * mon_int_rate
        future_value = future_value + mon_int_amount
        
    print("Future value : \t\t\t" , int(future_value))
    print()
    
    # continue ?
    
    choice= input("Continue ? (y/n): ")
    print()
print("Bye!!!")            
    