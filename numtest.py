n1 = 3.25E-8
n2 = round(n1, 10)
print(n2)

print(pow(2,3))

import math

n3 = math.gcd(24, 500)
print(n3)

n4 = math.hypot(3, 5)
print(n4)

print("{:15} {:>10} {:>5}".format("Description", "Price", "Qty"))
print("{:15} {:10.2f} {:5d}".format("Hammer", 23.456, 6))
print("{:15} {:10.2f} {:5d}".format("Nail", 4.3, 15))

import locale as lc

result = lc.setlocale(lc.LC_ALL, "us")
print (result)
if result == "C":
    lc.setlocale(lc.LC_ALL, "en_US")

print(lc.currency(12345.678, grouping=True))

print("with format")
print(lc.format("%d", 12345.678, grouping=True))
print(lc.format("%.2f", 12345.678, grouping=True))    

from decimal import  Decimal

n5 = Decimal("10.65")
print(n5)

n6 = n5 + Decimal("3.65")
n7 = n5 + 5

print (n6)
print(n7)

print("5 = ", ord("5"))
print("5 = ", ord("A"))

query = ''' select * from table 1
            where a =b
            and c =d
            and f = j'''
print(query, end=" ")

search = "frm"
if search in query:
    print("search term found")
else:
    print("search term not found")                 

title = "the meaning of life...."
print(title.isalpha())
print(title.islower())
print(title.isupper())
print(title.isdigit())


emaild = "ram@.com"
emaild1 = "ram.sharma@com"
emaild2 = "ram.sharma@email.com"

at_index = emaild.find("@")
at_index1 = emaild1.find("@")
at_index2 = emaild2.find("@")

dot_index = emaild.find(".", at_index)
dot_index1 = emaild1.find(".", at_index1)
dot_index2 = emaild2.find(".", at_index2)

print(at_index, at_index1, at_index2, dot_index, dot_index1, dot_index2)

if at_index == -1 or dot_index == -1:
    print("invalid emailid " + emaild)
    
if at_index1 == -1 or dot_index1 == -1:
    print("invalid emailid " + emaild1)
    
if at_index2 == -1 or dot_index2 == -1:
    print("invalid emailid " + emaild2)
    
emaild2 = emaild2.replace("email", "yahoo") 
print(emaild2)   

quote = "If you want to have something you never had, do something you have never done."
words = quote.split()
print(words[0], words[1],words[2])

print(len(words))

today = "09/11/2019"


dates = today.split("/")
print("Month: " + dates[0] + " Day: " + dates[1] + " Year: " + dates[2])


from datetime import date, time, datetime

inv_day = date.today()
print(inv_day)

inv_time = datetime.now()

print(inv_time)


countries= {"MX":"Mexico",
            "IN": "India",
            "US": "United Stats"}

for code in countries.keys():
    print(code + "    " + countries[code ])
    