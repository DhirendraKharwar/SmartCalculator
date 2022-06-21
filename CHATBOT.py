responses=['Smart ChatBot','You can suppose me as your assistant','Thanks','Kya Mtlb','Sorry, This is beyond my ability',"Ohh! Sorry, I don't know Your aim but you always take your strict aim in your life because strict aim can change your life."]

ChatResponses=['Kuchh Naii']

'''
import pyttsx3
import speech_recognition as sr
import time

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def speak2(audio,a):
    engine.say(audio,a)
    engine.say(a)
    engine.runAndWait()

def speak3(audio,a,b):
    engine.say(audio)
    engine.say(a)
    engine.say(b)
    engine.runAndWait()

 '''  


def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)

def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def hcf(a,b,c=0):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
def big(a,b):
    return a if a>b else b
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def end():
    print(responses[2],"Nice to meet you.")
    
    input("Press inter to exit")
    exit()
def myname():
    print(responses[1])
    #speak(responses[1])


def girlfriendname():
    try:
        with open("girlfriendname.txt","r") as f:
         showname=f.read()
         #speak2(showname," is your girlfriend")
         print(showname," is your girlfriend",sep=' ')
         #speak2(showname,'is your girlfriend name.....Is it right?')
         print(showname,'.....Is it right?')
         #speak("Press 0, for No and 1, for Yes")
         n=int(input("Press 0, for No and 1, for Yes: "))
         if n==0:
            with open("girlfriendname.txt","w") as f:
             #speak("Write your girlfriend name")
             n=input("Write your girlfriend name ")
             f.write(n)
             with open("girlfriendname.txt","+a") as f:
              showname=f.read()
              print("Okay,I'll remember.")
              #speak3("Okay,I'll remember.")
         elif n==1:
            with open("girlfriendname.txt","r") as f:
             showname=f.read()
             print("Okay,I'll remember that ",showname," is your girlfriend.")
             #speak3("Okay,I'll remember that ",showname," is your girlfriend.")
         else:
            print("Wrong Entery")
            #speak("Wrong Entery")
    except FileNotFoundError:
            print("I don't know your girfriend name")
            #speak("I don't know your girfriend name")
            f=open("girlfriendname.txt","a+")
            #speak("Write your girlfriend name I will remember for future")
            n=input("Write your girfriend name ")
            f.write(n)
            f=open("girlfriendname.txt","r")
            readname=f.read()
            print("Okay,I'll remember that ",readname," is your girlfriend.")
            #speak3("Okay,I'll remember that ",readname," is your girlfriend.")
            

def boyfriendname():
                try:
                    f=open("boyfriendname.txt","r")
                    showname=f.read()
                    #speak2("Your boyfriend name is ",showname)
                    print("Your boyfriend name is ",showname,sep=' ')
                    #speak2(showname,"Is it right?")
                    print(showname,'Is it right?')
                    #speak("Press 0, for No and 1, for Yes")
                    n=int(input("Press 0, for No and 1, for Yes"))
                    if n==0:
                        f=open("boyfriendname.txt","w")
                        #speak("Write your boyfriend name I will remember for future")
                        n=input("Write your boyfriend name ")
                        f.write(n)
                        f=open("boyfriendname.txt","r")
                        readname=f.read()
                        print("Okay,I'll remember that ",readname," is your boyfriend.")
                        #speak3("Okay,I'll remember that ",readname," is your boyfriend.")
                    elif n==1:
                        f=open("boyfriendname.txt","r")
                        readname=f.read()
                        print("Okay,I'll remember that ",readname," is your boyfriend.")
                        #speak3("Okay,I'll remember that ",readname," is your boyfriend.")
                    else:
                        print("Wrong Entery")
                except FileNotFoundError:
                        print("I don't know your boyfriend name")
                        f=open("boyfriendname.txt","a+")
                        n=input("Write your boyfriend name ")
                        f.write(n)
                        f=open("boyfriendname.txt","r")
                        readname=f.read()
                        print("Okay,I'll remember that ",readname," is your boyfriend.")
            

def friendname():
    try:
        f=open("friendname.txt","r")
        showname=f.read()
        #speak2(showname,"Is your friend")
        print("Your friend name is ",showname,sep=' ')
        #speak2(showname,'Is it right?')
        print(showname,'Is it right?')
        #speak("Press 0, for Not right and press 1, for right")
        n=int(input("Press 0, for Not right and press 1, for right"))
        if n==0:
            f=open("friendname.txt","w")
            #speak("Write your friend name I will remember your friend name for future")
            n=input("Write your friend name ")
            f.write(n)
            f=open("friendname.txt","r")
            readname=f.read()
            #speak3("Okay,I'll remember that ",readname," your friend.")
            print("Okay,I'll remember that ",readname," your friend.")
        elif n==1:
            #speak("Do you want to add your friends name   Press 0,  for don't add  and press 1, for add")
            n=int(input("Do you want to add your friends.... Press 0, for don't add and press 1, for add "))
            if n==1:
                f=open("friendname.txt","a+")
                n=input("Add your friend ")
                f.write(n)
                f=open("friendname.txt","r")
                readname=f.read()
                print("I'll Remember that ",readname," your friend." )
                #speak3("I'll Remember that ",readname," your friend." )
            elif n==0:
                f=open("friendname.txt","r")
                readname=f.read()
                print("I'll Remember that ",readname," your friend ")
                #speak3("I'll Remember that ",readname," your friend ")
            else:
                print("Wrong Entery")
                #speak("Wrong Entery")
        else:
            print("Wrong Entery")
            #speak("Wrong Entery")
    except FileNotFoundError:
        #speak("I don't know your friend name")
        print("I don't know your friend name")
        f=open("friendname.txt","a+")
        #speak("Write your friend name I will remember for future")
        print("Write your friend name I will remember for future")
        n=input("Write your friend name ")
        f.write(n )
        f=open("friendname.txt","r")
        readname=f.read()
        print("Okay,I'll remember that ",readname," is your friend.")
        #speak3("Okay,I'll remember that ",readname," is your friend.")

def java():
    try:
        f=open("What is java.txt","r")
        readfile=f.read()
        print(readfile)
        #speak(readfile)
        #speak("press 1 to continue: ")
        c=int(input("press 1 to continue"))
    
        if c==1:
            f=open("What is java1.txt","r")
            readfile=f.read()
            print(readfile)
            #speak(readfile)
        else:
            print("Wrong Entry")
            #speak("Wrong Entry")
    except FileNotFoundError:
        print("No result found")
        f=open("JavaIntro.txt","a+")
        #speak("Write your friend name I will remember for future")
        print("Enter your Feedback: ")
        n=input("What is Java? ")
        f.write(n )
        f=open("JavaIntro.txt","r")
        JavaIntro=f.read()
        print("Your feedback received: ",JavaIntro)
        #speak3("Okay,I'll remember that ",readname," is your friend.")

def music():
    print("music")
    
    
def aim():
    #speak(responses[4])
    print(responses[4])
def sorry():
    #speak(responses[3])
    print(responses[3])
def help():
    #speak("List of valid commonds")
    print("List of valid commonds")
    for k in operations:
        print(k)
    for k in commands:
        print(k)

def Krna():
    #print(ChatResponses[0])
    print("Kuchh naii bss Apse baate")
def Suno():
    print("Hmm Ji")
def Khana():
    print("Av naii")
def Kyu():
    print("Pta Naii")
def Pagl():
    print("Me nhi App")

operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"MINUS":sub,"SUBTRACTION":sub,"SUBTRACT":sub,"DIFFERENCE":sub,
    "PRODUCT":multiply,"MULTIPLICATION":multiply,"MULTIPLY":multiply,"DIVIDE":division,"DIVISION":division,"LCM":lcm,
    "HCF":hcf,"BIG":big,"MAX":big,"GREATER":big,"MUSIC":music,"SONG":music
            }
commands={"JAVA":java,"NAME":myname,"DOST":friendname,"FRIEND":friendname,"BF":boyfriendname,"BOYFRIEND":boyfriendname,
          "SWEETU":girlfriendname,"JANU":girlfriendname,"JAANU":girlfriendname,"GF":girlfriendname,"GIRLFRIEND":girlfriendname,
          "END":end,"EXIT":end,"CLOSE":end,"STOP":end,"BYE":end,"HELP":help,"AIM":aim,"GOAL":aim,"AMBITION":aim,"MUSIC":music,"PLAY":music}

ChatQuestions={"RHE":Krna,"SUNO":Suno,"ACHHA":Suno,"KHANA":Khana,"KYU":Kyu,"PAGL":Pagl}

def main():
    #speak(responses[0])
    print(responses[0])
    while True:
        print()
        #speak("Enter some text ")
        text=input("Type Message Here:  ")
        for word in text.split(" "):
            if word.upper() in operations.keys():
                try:
                    l=extract_numbers_from_text(text)
                    r=operations[word.upper()](l[0],l[1])
                    print(r)
                    #speak(r)
                except:
                    print("Something is wrong please retry")
                    #speak("Something is wrong please retry")
                finally:
                    break
            
            elif  word.upper() in commands.keys():
                commands[word.upper()]()
                break

            elif  word.upper() in ChatQuestions.keys():
                ChatQuestions[word.upper()]()
                break
        else:
            sorry()

if __name__=="__main__":
    main()
