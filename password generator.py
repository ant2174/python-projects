import random
import string
mainlist=[]
listbig=list(string.ascii_uppercase)
listsmall=list(string.ascii_lowercase)
listsplchar=['!','@','#','$','%','^','&','*','_','-','+','=','|','<','>','?']
big=int(input("Please input number of Capital letters in the password: "))
small=int(input("Please input number of small letters in the password: "))
splchar=int(input("Please input number of special charecters letters in the password: "))
for i in range(0,big):
    a=random.randrange(0,len(listbig))
    mainlist.append(listbig[a])
for i in range(0,small):
    b=random.randrange(0,len(listsmall))
    mainlist.append(listsmall[b])
for i in range(0,splchar):
    c=random.randrange(0,len(listsplchar))
    mainlist.append(listsplchar[c])
random.shuffle(mainlist)    
for i in range(0,len(mainlist)):
    print(mainlist[i],end="")
print("\n")
if(big>0 and small>0 and splchar>0 and big+small+splchar>=10 and splchar>=1 and big>=1):
    print("Strong password!!")
elif(small>0 and big+small+splchar>=10 and (splchar==0 or big==0)):
    print("Moderate password!")
else:
    print("Weak password!!!")    


        
    
        
             
             
