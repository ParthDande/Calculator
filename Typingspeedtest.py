#**********************Typing speed test***************************************
'''Name: PARTH DANDE
def resetfunction():
    global runonce,misswords,accuracy,score,timecounter,misswords,timecounter
    score = 0
    timecounter = 30
    misswords = 0
    runonce = 1
    accuracy=0
    time_label_count.configure(text=timecounter,fg="#06283D")
    random.shuffle(wordlist)
    word_entry.delete(0, END)
    word_label.configure(text=wordlist[0])
    score_label_count.configure(text=score)
    directionallabel.configure(text="")
    resetbutton.destroy()
    exitbutton.destroy()
    startonspace()
    ####################################3
def startonspace():
    main_window.bind("<space>", startcode)
def destroywindow():
    main_window.destroy()

###################################################################################blinking text
def blinkingtext():
    global blinkingvariable
    if blinkingvariable % 2 == 0:
        txt ="Welcome to typing speed test"
        blinkingvariable += 1
    else:
        txt = ""
        blinkingvariable += 1
    fontlabel.configure(text=txt)
    fontlabel.after(500, blinkingtext)

########################################function to implement time
def timecount():###function to start the time after space is entered
    global timecounter,score,misswords,totalwords,charactescounter,resetbutton,exitbutton,accuracy
    if(timecounter>0):
        timecounter-=1
        time_label_count.configure(text=timecounter)
        time_label_count.after(1000,timecount)##to call the time function after every 1 second
        if timecounter<6:
            time_label_count.configure(fg="red")#so that the timer text turns red while 5 seconds is remaining.
    else:
        totalwords=misswords+score
        wpm=totalwords*2
        if totalwords>0:
            accuracy = (score / totalwords) * 100
        main_window.unbind("<space>")
        display_label.configure(text=' Accuracy ={} % | WPM = {} | CPM={}'.format(round(accuracy,2),wpm,charactescounter-1))
        resetbutton = Button(main_window, text="Reset", command=resetfunction, width=10, height=2,font=( 'ariel'),bg="#47B5FF",fg='#06283D',borderwidth="5")####reset button is created here
        resetbutton.place(x=240, y=450)
        exitbutton = Button(main_window,text="Exit",command=destroywindow,width=10,height=2,font=( 'ariel'),bg="#47B5FF",fg='#06283D',borderwidth='5')####exit button is created here
        exitbutton.place(x=450,y=450)

#############function for taking input thorugh enter and matching it with word
def startcode(event):
    global charactescounter,runonce,resetbutton,exitbutton#to call the time function only once as it is a recursive function once called runonce is used
    resetbutton.destroy()
    exitbutton.destroy()
    while runonce>0:
        timecount()
        runonce=0
    global score,misswords
    directionallabel.configure(text='')
    charactescounter=charactescounter+len(word_entry.get())
    if(word_entry.get()[:-1]==word_label["text"]):#to check wether typed word  matches the displayd word.
        score+=1
        #score=score+1
        score_label_count.configure(text=score)
    else:
        misswords+=1#to count the number of missed words
    random.shuffle(wordlist)
    word_label.configure(text=wordlist[0])#to change the lable everytime a random text is called
    word_entry.delete(0,END)
###############################import library

from tkinter import*
import  random
#import customtkinter
from tkinter import  messagebox
################ main_window
main_window=Tk()
main_window.geometry("800x600+400+100")#+400 and+100 to align the window in center of screen
main_window.minsize(800,600)#to keep the size of the window of the tkinter constant
main_window.maxsize(800,600)
main_window.configure(bg="#47B5FF")
main_window.title("typing speed test")
main_window
##################################variables
score=0
timecounter=30
count=0
sliderwords=''
misswords=0
runonce=1
charactescounter=0
blinkingvariable=0
wordlist=['apple','colors','sand','there','yestarday',' tomorrow','random','hello','hero','willpower','believe','constellation','approach','equinox','desert','snow','peace','speed','test','typing','sun','star','anchor','Panda','giraffe']
##########################labels
fontlabel=Label(main_window,text="",font=("arial",24),bg="#47B5FF",fg="#06283D",width=35)
fontlabel.place(x=70,y=10)
blinkingtext()
random.shuffle(wordlist)#to get random word every time the programm is started
word_label=Label(main_window, text =wordlist[0] ,font=("arial",15,"italic bold"),bg="#47B5FF",fg="#F24C4C")
word_label.place(x=340,y=200)
score_label=Label(main_window,text="Score",font=("arial",15,"italic bold"),bg="#47B5FF",fg="#06283D")
score_label.place(x=100,y=80)
score_label_count=Label(main_window,text=score,font=("arial",15,"italic bold"),bg="#47B5FF",fg="#06283D")
score_label_count.place(x=110,y=110)
time_label=Label(main_window,text="Timer",font=("arial",15,"italic bold"),bg="#47B5FF",fg="#06283D")
time_label.place(x=600,y=80)
time_label_count=Label(main_window,text=timecounter,font=("arial",15,"italic bold"),bg="#47B5FF",fg="#06283D")
time_label_count.place(x=620,y=110)
directionallabel=Label(main_window,text=" Enter the text in the box",font=("arial",15,"italic bold"),bg="#47B5FF",fg="#06283D",)
directionallabel.place(x=200,y=300)
display_label=Label(main_window,text='',font=("arial",15,"italic bold"),bg="#47B5FF",fg="#06283D")
display_label.place(x=201,y=301)
#############entry box
word_entry=Entry(main_window,font=("arial",25,"italic bold"),bd=10,justify="center",fg="#06283D")#using justification we can start typing from the center of the box
word_entry.place(x=200,y=240)
word_entry.focus_set()#not workding fix requird
startonspace()


##############################################button
resetbutton=Button(state=DISABLED)
exitbutton=Button(state=DISABLED)
main_window.mainloop()
