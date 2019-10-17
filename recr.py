import reader

def power(x,y):
    if y == 0:
        return 1
    elif y == 1:
        return x 
    else:
        return x*power(x, y-1)
    
def oddsumm(n):
    sum=0
    i=1
    while(i<=n):
        sum=sum+(i*2-1)
        i = i+1
    return sum

s1=oddsumm(3)
s2=oddsumm(5)

print (s1)
print(s2)


#list_num = [0,1,2,3,4,5,6,7,8,9,99,676,5653,35,45452,0,24]

#print(list_num[-1])

#list_even = []
#list_odd = []

#num_of_val =  (len(list_num))
#for  i in list_num:
 #   if (i%2 == 0):
  #      list_even.append(i)


#list_even.
#    else:
#         list_odd.append(i)
         
#            
#    #n=power(2,list_num[i])
#    #print(n)
#
#for numb in list_num:
#    print(numb)
    
     
#print("list even")
#print(list_even)   
#print("list odd")
#$print(list_odd)   
