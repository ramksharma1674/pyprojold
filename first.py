print ("Hello Pythos World !!!")

x="4"

print(type(x))

#def print_directory_contents(sPath):
#    import os                                       
#    for sChild in os.listdir(sPath):                
#        sChildPath = os.path.join(sPath,sChild)
#        if os.path.isdir(sChildPath):
#            print_directory_contents(sChildPath)
#        else:
#            print(sChildPath)

def print_directory_contents(sPath):            
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)    
    
            
            

print_directory_contents("c:\project\java\pyproj")

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]

#print(A6)
#print(range(0))

def f(x,l=[]):
    for i in range(x):
        print (i)
        l.append(i*i)
    #print("Final list")
    #print(l) 

#f(2)
#f(3,[3,2,1])
#f(3)

import datetime
print(datetime)
#datetime.datetime.now = lambda:
# datetime.datetime(2012, 12, 12)