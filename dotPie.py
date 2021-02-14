#!/usr/bin/env python
import os , sys

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
        ['!','@','#','$','%','^','&','*','(',')','-','+'],
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
    print('-------------------------------------------')
    print('|                                         |')
    print('|          Welcome to dotPie              |')
    print('|                                         |')
    print('|     the world amazing password meter    |')
    print('|                                         |')
    print('-------------------------------------------')
    print('')
    while (True):
        print('Enter 1 to check password')
        print('Enter 2 to exit')
        option= input('Your option ')
        print('')
        if option == '1':
            password = input('Enter a password: ')
            print('')
            #validation variables
            length= False
            capital = False
            lower= False
            number= False
            symbol= False
            dic= False
            pattern = False
            repetition=False
            total =0

            #check is it a dictionary word or not
            openfile= open(os.path.join(sys.path[0], "wordlist-probable.txt"),'r')
            dictionary =openfile.readlines()
            openfile.close()
            for word in dictionary:
                if word.rstrip() == password:
                    dic = True
                    print('The password is a dictionary word')
                    break
            if not dic:
                print('You are lucky it is not in the  :) ')

            
            #check length 
            if(len(password)>=8):
                length = True
                print('The password has more than 8 digits '+'+'+str(len(password)*4))
            else:
                print('The password should have at least 8 digits '+'+'+str(len(password)*4))
            total = total + (len(password)*4)
            capCounter=0
            for cap in password:
                if(cap.isupper()):
                    capital=True 
                    capCounter=capCounter+1

            if capital:
                total = total +((len(password)-capCounter)*2)
                print('The password has at least one capital letter '+'+'+str((len(password)-capCounter)*2))
            else:
                print('The password shoud have at least one capital letter '+'+0')
            
            #check lowercase letters
            lowCounter=0
            for low in password:
                if(low.islower()):
                    lower=True 
                    lowCounter=lowCounter+1

            if lower:
                total = total +((len(password)-lowCounter)*2)
                print('The password has at least one lowercase letter '+'+'+str((len(password)-lowCounter)*2))
            else:
                print('The password shoud have at least one lowercase letter '+'+0')
            
            #check numbers
            numCounter=0
            midNumCount=0
            for num in password:
                if(num.isdigit()):
                    number=True 
                    numCounter=numCounter+1
            for i in range(1,len(password)-1):
                if password[i].isdigit():
                    midNumCount=midNumCount+1
            if number:
                total=total+ (numCounter*4)
                print('The password has at least one number '+'+'+str(numCounter*4))
                #Bonus for middle numbers
                if midNumCount>0:
                    total=total+(midNumCount*2)
                    print('The password has at least one number in the middle '+'+'+str(midNumCount*2))
            else:
                print('The password shoud have at least one number '+'+0')

            #check symbols
            charCount=0
            midCharCount=0
            char=['!','@','#','$','%','^','&','*','(',')','-','+','=',',','.','/','\'',';',']','[','\\','~','`','<','>','?','"',':','{','}','|']
            for sym in password:
                if(sym in char):
                    symbol=True 
                    charCount=charCount+1
            for i in range(1,len(password)-1):
                if password[i] in char:
                    midCharCount=midCharCount+1
            if symbol:
                total=total+(charCount*6)
                #Bonus for middle symbols
                if midCharCount>0:
                    total =total+(midCharCount*2)
                    print('The password has at least one symbol in the middle '+'+'+str(midCharCount*2))
                print('The password has at least one symbol '+'+'+str(charCount*6))
            else:
                print('The password shoud have at least one symbol '+'+0')
            
            #Meet requirement
            if length and capital and lower and number and symbol:
                total=total +10
                print('The password met the basic requirements '+'+10')

            #check if only letters
            if not symbol and not number:
                print('The password only contains letters '+'-'+str(len(password)))
                total=total-len(password)

            #check if only numbers
            if not symbol and not lower and not capital:
                print('The password only contains numbers '+'-'+str(len(password)))
                total=total-len(password)

            #check keyboard pattern 
            pos=[]
            for ch in password: 
                if(ch.islower() or ch.isupper() or ch.isdigit()):
                    pos.append(findPos(ch.upper()))
            row=0 
            col=0
            i=0
            rCount=0
            cCount=0
            patCounter=-1
            while row<4 and col<10 and i<len(pos):
                if pos[i][0]==row :
                    rCount=rCount+1
                if pos[i][1]==col :
                    cCount=cCount+1
                if cCount>=2 or rCount>=2:
                    pattern = True
                    patCounter=patCounter+1
                if pos[i][0] != row:
                    rCount=0
                if pos[i][1] != col:
                    cCount=0
                if i+1 ==len(pos):
                    row = row +1 
                    col= col+1
                    i=0
                i=i+1
            if pattern:
                total=total-(patCounter*2)
                print('Stop using pattern :) '+'-'+str(patCounter*2))
            else:
                print('Wow :) '+'-0')

            #check repetition  
            rep=0
            for i in range(len(password)):
                for j in range(len(password)):
                    if i != j and password[i]== password[j]:
                        repetition=True
                        rep=rep+1

            if repetition:
                total=total-(rep)
                print('You should start using different letters :)'+' -'+str(rep))
            else:
                print('You are the master of unrepeated characters'+' -0')

            #sequential 
            seqCount=0 
            for i in range(len(password)):
                if i+1< len(password): 
                    if ord(password[i]) == ord(password[i+1])-1 or ord(password[i])-1 == ord(password[i+1]):
                        seqCount=seqCount+1
            if seqCount >2 :
                total=total-((seqCount+1)*2)
                print('Sequence are not allowed :) '+'-'+str((seqCount+1)*2))

            
            #calculate score
            print('')
            if total > 100:
                #very strong
                print('Very strong password')
                print('Score: 10')
            elif total >= 80 and total<=100:
                #very strong
                print('Very strong password')
                print('Score: '+str(total/10))
            elif total >=60 and total<80:
                #strong
                print('Strong password')
                print('Score: '+str(total/10))
            elif total >=40 and total<60:
                #good
                print('Good password')
                print('Score: '+str(total/10))
            elif total>=20 and total <40:
                #weak
                print('Weak password')
                print('Score: '+str(total/10))
            elif total>=0 and total <20:
                #very weak 
                print('Very weak password')
                print('Score: '+str(total/10))
            else:
                print('Very weak password')
                print('Score: 1')
            print('')
        elif option == '2':
            print('')
            print('#############################')
            print('#                           #')
            print('#          Bye Bye          #')
            print('#                           #')
            print('#############################')
            break
        else:
            print(' ')
            print('Invalid option')
            print('')
	
		    
passMeter()

