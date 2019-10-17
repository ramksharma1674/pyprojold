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
    