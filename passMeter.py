from clint.textui import colored

#key=[
#        ['!','@','#','$','%','^','&','*','(',')','_','+'],
#        ['Q','W','E','R','T','Y','U','I','O','P','{','}','|'],
#        ['A','S','D','F','G','H','J','K','L',':','"'],
#        ['Z','X','C','V','B','N','M','<','>','?'],
#        ['1','2','3','4','5','6','7','8','9','0','-','='],
#        ['q','w','e','r','t','y','u','i','o','p','[',']','\\'],
#        ['a','s','d','f','g','h','j','k','l',';','\''],
#        ['z','x','c','v','b','n','m',',','.','/']
#        ]
def findPos(char):
    key=[
        ['1','2','3','4','5','6','7','8','9','0'],
        ['Q','W','E','R','T','Y','U','I','O','P'],
        ['A','S','D','F','G','H','J','K','L'],
        ['Z','X','C','V','B','N','M'],
        ]
  
    for row in range(len(key)):
        for col in range(len(key[row])):
            if(char == key[row][col]):
                return [row,col]

def passMeter ():
    print(colored.yellow('-------------------------------------------'))
    print(colored.yellow('|                                         |'))
    print(colored.yellow('|           Welcome to *****              |'))
    print(colored.yellow('|                                         |'))
    print(colored.yellow('|     the world amazing password meter    |'))
    print(colored.yellow('|                                         |'))
    print(colored.yellow('-------------------------------------------'))
    print('')
   # while (True):
    password = input(colored.yellow('Enter a password: '))
    print('')
    #validation variables
    length= False
    capital = False
    lower= False
    number= False
    symbol= False
    dic= False
    pattern = False
    total =0

    #check length 
    if(len(password)>=8):
        length = True
       # total = total + (len(password)*4)
        print(colored.green('The password has more than 8 digits'))
    else:
        print(colored.red('The password should have at least 8 digits'))
    total = total + (len(password)*4)
   # if length :
   #     total = total + (len(password)*4)
    #print(total)
    #check capital letters
    capCounter=0
    for cap in password:
        if(cap.isupper()):
            capital=True 
            capCounter=capCounter+1
           # print(colored.green('The password has at least one capital letter'))
            #break
    if capital:
        total = total +((len(password)-capCounter)*2)
        #print((len(password)-capCounter)*2)
        print(colored.green('The password has at least one capital letter'))
    else:
        print(colored.red('The password shoud have at least one capital letter'))
    
    #check lowercase letters
    lowCounter=0
    for low in password:
        if(low.islower()):
            lower=True 
            lowCounter=lowCounter+1
            #print(colored.green('The password has at least one lowercase letter'))
            #break
    if lower:
        total = total +((len(password)-lowCounter)*2)
        #print((len(password)-lowCounter)*2)
        print(colored.green('The password has at least one lowercase letter'))
    else:
        print(colored.red('The password shoud have at least one lowercase letter'))
    
    #check numbers
    numCounter=0
    midNumCount=0
    for num in password:
        if(num.isdigit()):
            number=True 
            numCounter=numCounter+1
            #print(colored.green('The password has at least one number'))
            #break
    for i in range(1,len(password)-1):
        if password[i].isdigit():
            midNumCount=midNumCount+1
    if number:
        total=total+ (numCounter*4)
        #print(numCounter*4)
        #Bonus for middle numbers
        total=total+(midNumCount*2)
        print(colored.green('The password has at least one number'))
    else:
        print(colored.red('The password shoud have at least one number'))

    #check symbols
    charCount=0
    midCharCount=0
    char=['!','@','#','$','%','^','&','*','(',')','-','+','=',',','.','/','\'',';',']','[','\\','~','`','<','>','?','"',':','{','}','|']
    #char= ['!','@','#','$','%','^','&','*','-','.',':','?','+','=']
    for sym in password:
        if(sym in char):
            symbol=True 
            charCount=charCount+1
            #print(colored.green('The password has at least one symbol'))
            #break
    for i in range(1,len(password)-1):
        if password[i] in char:
            midCharCount=midCharCount+1
    if symbol:
        total=total+(charCount*6)
        #Bonus for middle symbols
        total =total+(midCharCount*2)
        #print(charCount*6)
        print(colored.green('The password has at least one symbol'))
    else:
        print(colored.red('The password shoud have at least one symbol'))
    

    #check keyboard pattern 
    pos=[]
    for ch in password: 
        if(ch.islower() or ch.isupper() or ch.isdigit()):
            pos.append(findPos(ch.upper()))
    #print(pos)
    row=0 
    col=0
    i=0
    rCount=0
    cCount=0
    while row<4 and col<10 and i<len(pos):
        if pos[i][0]==row :
            rCount=rCount+1
        if pos[i][1]==col :
            cCount=cCount+1
       # print("counter: "+str(rCount)+" row "+str(row)+" i "+str(i))
       # print(i)
        if cCount>2 or rCount>2:
            pattern = True
            print(colored.red('Stop using pattern stupid :)'))
            break
        if pos[i][0] != row:
            rCount=0
        if pos[i][1] != col:
            cCount=0
        if i+1 ==len(pos):
            row = row +1 
            col= col+1
            i=0
        i=i+1
    if(not pattern):
        print(colored.green('Wow :) '))


    #check is it a dictionary word or not
    openfile= open('/usr/share/dict/wordlist-probable.txt','r')
    dictionary =openfile.readlines()
    openfile.close()
    for word in dictionary:
        if word.rstrip() == password:
            dic = True
            print(colored.red('The password is a dictionary word'))
            break
    if(not dic):
        print(colored.green('You are lucky. They did not discover your password :) ')) 

    #Calculations

    print(total)
passMeter()


