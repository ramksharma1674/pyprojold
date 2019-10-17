ar1=[3,2,6,77,33,55,43,9,32]


counter= (len(ar1))

print(counter)

#ar1.sort()

print(ar1)

ar1s = []
count=0

for i in ar1:
    for j in ar1:
            if i > j:
                ar1s.append(j)
    #count = count + 1
    
print ("sorted array")
print(ar1s)
