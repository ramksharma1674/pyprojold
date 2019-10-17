import scrabble
import string


#print all words containing "oo" adsf
#wordlist=["ram","sonali","laptop","bag","glass","lock","apple","charger"]
letters = "asgt"
ourlist = []
orig_len = len(letters)
calc_len = 0

for word in scrabble.wordlist:
    calc_len = 0
    for letter in letters:
        #print("letter  " + letter)
        if letter in word:
            calc_len = calc_len + 1
            #print("calculate length ")
            #print(calc_len)
    if (orig_len == calc_len):
        print("Matching word  - " + word)
        ourlist.append(word)
        #calc_len = 0
    #else:    
        #calc_len = 0    
            

print("ourlist -- ")
#print(ourlist)
print ("end our list")
        
#for letter in string.ascii_lowercase:
#    exists = False
#    
#    for word in scrabble.wordlist:
#        if letter * 3 in word:
#            exists = True
#            break
#    if not exists:
#        print("There are no word having 3 " + letter)    
            