#ceasar cypher/decypher by Panos07

#A clean terminal
import os 
os.system("cls")

#ask for the key
key=int(input("give me the key of the encreption "))

#make sure it is integer 
if isinstance(key, int):
    #choose what to do
    choose=input("you want to cypher or decypher ")
    if choose == "cypher":
        crWord=""
        #ask for the word
        x=input("what do you want to cypher ")
        #Cypherinng
        for letter in x:
            xx=ord(letter)+key 
            crWord+=chr(xx)
        print(crWord)

    elif choose == "decypher":
        crWord=""
        #ask for a word
        y=input("what do want to decypher ")
        #Decyphering
        for letter in y:
            yy=(ord(letter)-key)
            crWord+=chr(yy)
        print(crWord)

#if not start again
else:
    print("The key must be integer ")
    key=0