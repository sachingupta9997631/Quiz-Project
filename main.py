from tkinter import *
import sqlite3

db=sqlite3.connect("data.db")
cur=db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS record(SN number,Question text,option1 text,option2 text,option3 text,option4 text,answer text)")
######################################fuctions defined#####################

def about():
    win1=Toplevel()
    win1.title("About Page")

    win1.config(bg="#07caf0")
    win1.geometry("1530x1000+0+0")
    img=PhotoImage(file="Pic_req\\1.png")
    lab=Label(win1,image=img)
    lab.pack(side=LEFT)
    lab.place(x=0,y=0)
 
    main=Label(win1,text="Quiz App",font=("bahnschrift semibold",55),fg="white",bg="#07caf0")
    main.pack(pady=10)

    txt1="* The Main Objective of this Application is for Education Purpose\n to take Quiz Activities.\n\n* This Application will allow the Faculties or the\n Admin to create a questionnaire"
    txt2="\n\n* This Application will save the questionnaire data at once by the admin\n"
    txt3="and will be displayed one by one in the game.\n"
    txt4="\n* You will also be getting the score according to your correct option\n"
    txt5="\n* The timer will be there which will show the remaining time you are with."

    devel=StringVar()
    devel.set(str("Developed By:\nSachin Gupta"))
    
    main_data=StringVar()
    main_data.set(str(txt1+txt2+txt3+txt4))
    
    tag1=Label(win1,text="A B O U T",font=("bahnschrift semibold",25),fg="white",bg="#07caf0")
    tag1.pack()

    data_show=Label(win1,textvariable=main_data,font=("bahnschrift semibold",20),fg="white",bg="#07caf0")
    data_show.pack(side=LEFT)
    data_show.place(x=50,y=250)

    developer=Label(win1,textvariable=devel,font=("bahnschrift semibold",30),fg="white",bg="#07caf0")
    developer.pack(side=LEFT)
    developer.place(x=750,y=600)
    
    end=Button(win1,text="Main Menu",font=("bahnschrift semibold",25),fg="white",bg="#07caf0",command=lambda:win1.destroy())
    end.pack()
    end.place(x=1160,y=600)

    win1.mainloop()


def instruct():
    win1=Toplevel()
    win1.title("Instructions")

    win1.config(bg="#07caf0")
    win1.geometry("1530x1000+0+0")
    img=PhotoImage(file="Pic_req\\1.png")
    lab=Label(win1,image=img)
    lab.pack(side=LEFT)
    lab.place(x=0,y=0)
 
    main=Label(win1,text="Quiz App",font=("bahnschrift semibold",55),fg="white",bg="#07caf0")
    main.pack(pady=10)

    txt1="You Will Find 5 Options on the Main Page\n\nStart Game:\nYou can Start Your Quiz Game from here where you have \nto just start the game and click on the correct given option\nthe questions will be updated after when you click to one question\nand according to your correct Option your scores will ne updated."
    txt2="\n\nQuestionnaire:\nUsing this Option you can Add/Create a Questionnaire of the quiz and delete it too."
    txt3="\n\nAbout:\nHere you will know about this Application by the developer"
    txt4="\n\nExit:\nfrom this button you can exit to windows."
    

    main_data=StringVar()
    main_data.set(str(txt1+txt2+txt3+txt4))
    
    tag1=Label(win1,text="I N S T R U C T I O N S",font=("bahnschrift semibold",25),fg="white",bg="#07caf0")
    tag1.pack()

    data_show=Label(win1,textvariable=main_data,font=("bahnschrift semibold",20),fg="white",bg="#07caf0")
    data_show.pack(side=LEFT)
    data_show.place(x=10,y=200)
    
    end=Button(win1,text="Main Menu",font=("bahnschrift semibold",25),fg="white",bg="#07caf0",command=lambda:win1.destroy())
    end.pack()
    end.place(x=1160,y=600)

    win1.mainloop()


def start_game():
    win1=Toplevel()
    win1.title("Quiz App")
    win1.config(bg="#07caf0")
    win1.geometry("1530x1000+0+0")
    img1=PhotoImage(file="Pic_req\\1.png")
    lab1=Label(win1,image=img1)
    lab1.pack(side=LEFT)
    lab1.place(x=0,y=0)

    sno,ques,op1,op2,op3,op4,ans=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()

    score=IntVar()
    
    count=StringVar()
    count.set("0")

    stats=StringVar()
    stats.set(str("Click on the Correct Option Button..."))
    #####################functions#####################
    def clock():
        if int(str(timer.get()))>0:
            t=int(str(timer.get()))-1
            timer.set(str(t))
            win1.after(1000,clock)
        else:
            stats.set(str("Oops! The time is Over..."))
            a_ent.config(state="disable")
            b_ent.config(state="disable")
            c_ent.config(state="disable")
            d_ent.config(state="disable")
            start_but.config(state="disable")
    ###################################################
    
    main_title=Label(win1,text="Quiz Game",font=("bahnschrift semibold",40),fg="yellow",bg="#07caf0")
    main_title.pack(fill=X,pady=10)

    fill_inst=Label(win1,text="( Best Of Luck )",font=("bahnschrift semibold",18),fg="white",bg="#07caf0")
    fill_inst.pack()

    lab_ques=Label(win1,text="Question",font=("bahnschrift semibold",24),fg="white",bg="#07caf0")
    lab_ques.pack()
    lab_ques.place(x=100,y=200)

    timer_lab=Label(win1,text="Time Left:",font=("bahnschrift semibold",24),fg="white",bg="#07caf0")
    timer_lab.pack()
    timer_lab.place(x=500,y=250)

    timer_lab_show=Label(win1,width=2,textvariable=timer,font=("bahnschrift semibold",24),fg="white",bg="#07caf0")
    timer_lab_show.pack()
    timer_lab_show.place(x=680,y=250)
    
    ent_ques_no=Label(win1,textvariable=count,width=2,font=("bahnschrift semibold",22),fg="white",bg="#07caf0")
    ent_ques_no.pack()
    ent_ques_no.place(x=250,y=204)

    lab_ques_ent=Label(win1,bg="#07caf0",fg="white",font=("bahnschrift semibold",18),text="The Question is: ")
    lab_ques_ent.pack()
    lab_ques_ent.place(x=100,y=270)

    ent_ques=Entry(win1,state="disabled",textvariable=ques,font=("bahnschrift semibold",18),width=105,fg="#07caf0",bg="white")
    ent_ques.pack()
    ent_ques.place(x=100,y=320)

    lab_opt=Label(win1,bg="#07caf0",fg="white",font=("bahnschrift semibold",18),text="The 4 Options are: ")
    lab_opt.pack()
    lab_opt.place(x=100,y=390)

    a_lab=Label(win1,text="(a):",font=("bahnschrift semibold",18),fg="white",bg="#07caf0")
    a_lab.pack()
    a_lab.place(x=100,y=450)

    a_ent=Button(win1,textvariable=op1,state="disabled",font=("bahnschrift semibold",18),width=20,fg="#07caf0",bg="white",command=lambda:submit("a"))
    a_ent.pack(pady=10)
    a_ent.place(x=150,y=450)

    b_lab=Label(win1,text="(b):",font=("bahnschrift semibold",18),fg="white",bg="#07caf0")
    b_lab.pack()
    b_lab.place(x=100,y=520)

    b_ent=Button(win1,textvariable=op2,state="disabled",font=("bahnschrift semibold",18),width=20,fg="#07caf0",bg="white",command=lambda:submit("b"))
    b_ent.pack(pady=10)
    b_ent.place(x=150,y=520)

    c_lab=Label(win1,text="(c):",font=("bahnschrift semibold",18),fg="white",bg="#07caf0")
    c_lab.pack()
    c_lab.place(x=100,y=590)

    c_ent=Button(win1,textvariable=op3,state="disabled",font=("bahnschrift semibold",18),width=20,fg="#07caf0",bg="white",command=lambda:submit("c"))
    c_ent.pack(pady=10)
    c_ent.place(x=150,y=590)

    d_lab=Label(win1,text="(d):",font=("bahnschrift semibold",18),fg="white",bg="#07caf0")
    d_lab.pack()
    d_lab.place(x=100,y=660)

    d_ent=Button(win1,textvariable=op4,state="disabled",font=("bahnschrift semibold",18),width=20,fg="#07caf0",bg="white",command=lambda:submit("d"))
    d_ent.pack(pady=10)
    d_ent.place(x=150,y=660)

    lab_score=Label(win1,text="Scores:",font=("bahnschrift semibold",24),fg="white",bg="#07caf0")
    lab_score.pack()
    lab_score.place(x=600,y=650)
    
    score_no=Label(win1,textvariable=score,width=2,font=("bahnschrift semibold",22),fg="white",bg="#07caf0")
    score_no.pack()
    score_no.place(x=730,y=654)
    ################functions defined###########################
    def start():
        count.set(str(int(count.get())+1))
        sno.set(str(""))
        ques.set(str(""))
        op1.set(str(""))
        op2.set(str(""))
        op3.set(str(""))
        op4.set(str(""))
        ans.set(str(""))

        if int(str(count.get()))==1:
            clock()
            a_ent.config(state="normal")
            b_ent.config(state="normal")
            c_ent.config(state="normal")
            d_ent.config(state="normal")
            
        tempo=str(count.get())
        cur.execute("select * from record where SN=(?)",(str(tempo),))
        a=cur.fetchone()
        if a==None:
            stats.set(str("No More Questions Were Feeded..."))
        else:
            sno.set(str(a[0]))
            ques.set(str(a[1]))
            op1.set(str(a[2]))
            op2.set(str(a[3]))
            op3.set(str(a[4]))
            op4.set(str(a[5]))
            ans.set(str(a[6]))
    
    def submit(opt=str()):
        if(opt==str(ans.get())):
            t=score.get()
            t+=1
            score.set(t)
        start()
        
    def result():
        f=str(score.get())
        stats.set(str("Your Score is: " + f))
        timer.set(str("0"))

        
    entry=Entry(win1,fg="lightgreen",bg="#07caf0",font=("bahnschrift semibold",16),textvariable=stats,state="disabled",width=50)
    entry.pack()
    entry.place(x=880,y=510)

    stat_lab=Label(win1,text="Status: ",fg="yellow",bg="#07caf0",font=("bahnschrift semibold",16))
    stat_lab.pack()
    stat_lab.place(x=800,y=510)
    ############################################################

    start_but=Button(win1,text="Start Game",font=("bahnschrift semibold",18),width=20,fg="white",bg="#07caf0",command=start)
    start_but.pack()
    start_but.place(x=500,y=510)

    back_but=Button(win1,text="Main Menu",font=("bahnschrift semibold",18),width=20,fg="white",bg="#07caf0",command=lambda:win1.destroy())
    back_but.pack()
    back_but.place(x=1150,y=580)

    res_but=Button(win1,text="View Result",font=("bahnschrift semibold",18),width=20,fg="white",bg="#07caf0",command=result)
    res_but.pack()
    res_but.place(x=500,y=580)

    win1.mainloop()


def questions():

    global cur
    win1=Toplevel()
    win1.title("Quiz App")
    win1.config(bg="#07caf0")
    win1.geometry("1530x1000+0+0")
    img1=PhotoImage(file="Pic_req\\1.png")
    lab1=Label(win1,image=img1)
    lab1.pack(side=LEFT)
    lab1.place(x=-10,y=0)

    count=StringVar()
    cur.execute("select MAX(SN) from record")
    temp=cur.fetchone()
    if temp[0]==None:
        count.set("1")
    else:
        alex=temp[0]+1
        count.set(str(alex))
    
    stats=StringVar()
    
    main_title=Label(win1,text="Creating Questionnaire",font=("bahnschrift semibold",40),fg="yellow",bg="#07caf0")
    main_title.pack(fill=X,pady=10)

    fill_inst=Label(win1,text="( Fill all the fields carefully )",font=("bahnschrift semibold",20),fg="white",bg="#07caf0")
    fill_inst.pack()

    lab_ques=Label(win1,text="Question",font=("bahnschrift semibold",24),fg="white",bg="#07caf0")
    lab_ques.pack()
    lab_ques.place(x=100,y=250)
    
    ent_ques_no=Entry(win1,state="disabled",textvariable=count,width=2,font=("bahnschrift semibold",20),fg="white",bg="#07caf0")
    ent_ques_no.pack()
    ent_ques_no.place(x=250,y=250)

    lab_ques_ent=Label(win1,bg="#07caf0",fg="white",font=("bahnschrift semibold",20),text="Enter the Question: ")
    lab_ques_ent.pack()
    lab_ques_ent.place(x=100,y=320)

    ent_ques=Entry(win1,font=("bahnschrift semibold",18),width=100,fg="#07caf0",bg="white")
    ent_ques.pack()
    ent_ques.place(x=100,y=370)

    lab_opt=Label(win1,bg="#07caf0",fg="white",font=("bahnschrift semibold",20),text="Enter the 4 Options: ")
    lab_opt.pack()
    lab_opt.place(x=100,y=440)

    a_lab=Label(win1,text="(a):",font=("bahnschrift semibold",20),fg="white",bg="#07caf0")
    a_lab.pack()
    a_lab.place(x=100,y=500)

    a_ent=Entry(win1,font=("bahnschrift semibold",18),width=40,fg="#07caf0",bg="white")
    a_ent.pack()
    a_ent.place(x=150,y=500)

    b_lab=Label(win1,text="(b):",font=("bahnschrift semibold",20),fg="white",bg="#07caf0")
    b_lab.pack()
    b_lab.place(x=100,y=550)

    b_ent=Entry(win1,font=("bahnschrift semibold",18),width=40,fg="#07caf0",bg="white")
    b_ent.pack()
    b_ent.place(x=150,y=550)

    c_lab=Label(win1,text="(c):",font=("bahnschrift semibold",20),fg="white",bg="#07caf0")
    c_lab.pack()
    c_lab.place(x=100,y=600)

    c_ent=Entry(win1,font=("bahnschrift semibold",18),width=40,fg="#07caf0",bg="white")
    c_ent.pack()
    c_ent.place(x=150,y=600)

    d_lab=Label(win1,text="(d):",font=("bahnschrift semibold",20),fg="white",bg="#07caf0")
    d_lab.pack()
    d_lab.place(x=100,y=650)

    d_ent=Entry(win1,font=("bahnschrift semibold",18),width=40,fg="#07caf0",bg="white")
    d_ent.pack()
    d_ent.place(x=150,y=650)

    ans_lab=Label(win1,text="Answer(Only the Options): ",font=("bahnschrift semibold",20),fg="white",bg="#07caf0")
    ans_lab.pack()
    ans_lab.place(x=100,y=700)

    ans_ent=Entry(win1,font=("bahnschrift semibold",18),width=5,fg="#07caf0",bg="white")
    ans_ent.pack()
    ans_ent.place(x=440,y=700)


    ################functions defined###########################

    def clear():
        a_ent.delete(0,'end')
        b_ent.delete(0,'end')
        c_ent.delete(0,'end')
        d_ent.delete(0,'end')
        ent_ques.delete(0,'end')
        stats.set("")

    def submit():
        a,b,c,d,e,f,g=str(count.get()),str(ent_ques.get()),str(a_ent.get()),str(b_ent.get()),str(c_ent.get()),str(d_ent.get()),str(ans_ent.get())

        if(b=="" or c=="" or d=="" or e=="" or f=="" or g==""):
            stats.set("The Fields were not properly filled...")
        else:
            cur.execute("insert into record values(?,?,?,?,?,?,?)",(a,b,c,d,e,f,g))
            db.commit()
            k=int(count.get())
            count.set(str(k+1))
            clear()
            stats.set(str("The Previos Question was Saved Successfully..."))
        
    entry=Entry(win1,fg="lightgreen",bg="#07caf0",font=("bahnschrift semibold",16),textvariable=stats,state="disabled",width=50)
    entry.pack()
    entry.place(x=880,y=660)

    stat_lab=Label(win1,text="Status: ",fg="lightgreen",bg="#07caf0",font=("bahnschrift semibold",16))
    stat_lab.pack()
    stat_lab.place(x=780,y=660)

    def delete():
        cur.execute("DELETE from record")
        count.set("1")
    ############################################################

    clear_but=Button(win1,text="Clear Fields",font=("bahnschrift semibold",18),width=20,fg="white",bg="#07caf0",command=clear)
    clear_but.pack()
    clear_but.place(x=1150,y=510)

    back_but=Button(win1,text="Main Menu",font=("bahnschrift semibold",18),width=20,fg="white",bg="#07caf0",command=lambda:win1.destroy())
    back_but.pack()
    back_but.place(x=1150,y=580)

    sub_but=Button(win1,text="Submit",font=("bahnschrift semibold",18),width=20,fg="#07caf0",bg="white",command=submit)
    sub_but.pack()
    sub_but.place(x=800,y=585)

    del_but=Button(win1,text="Delete all Previous Questions",font=("bahnschrift semibold",18),width=25,fg="#07caf0",bg="white",command=delete)
    del_but.pack()
    del_but.place(x=765,y=515)

    win1.mainloop()

###########################################################################

win=Tk()
win.title("Quiz App")

win.config(bg="#07caf0")
win.geometry("1530x1000+0+0")
img=PhotoImage(file="Pic_req\\1.png")
lab=Label(win,image=img)
lab.pack(side=LEFT)
lab.place(x=0,y=0)

timer=StringVar()
timer.set("0")

img2=PhotoImage(file="Pic_req\\3.png")
lab2=Label(win,image=img2)
lab2.pack(side=LEFT)
lab2.place(x=550,y=200)

time_lab=Label(win,text="Set Timer (in Seconds only)",font=("bahnschrift semibold",25),fg="white",bg="#07caf0")
time_lab.pack()
time_lab.place(x=300,y=680)

time_lock=Entry(win,width=4,font=("bahnschrift semibold",25),fg="#07caf0",bg="white")
time_lock.pack()
time_lock.place(x=730,y=680)

################################functions Defined#########################################
def lock_down():
    timer.set(str(time_lock.get()))
    loack.config(state="disabled")
##########################################################################################

loack=Button(win,text="Lock timer",font=("bahnschrift semibold",18),fg="#07caf0",bg="white",command=lock_down)
loack.pack()
loack.place(x=830,y=680)

main=Label(win,text="Quiz App",font=("bahnschrift semibold",55),fg="white",bg="#07caf0")
main.pack(pady=10)

tag1=Label(win,text="Let's Check Your Knowledge",font=("bahnschrift semibold",25),fg="white",bg="#07caf0")
tag1.pack()

strt=Button(win,text="Start Quiz",font=("bahnschrift semibold",25),fg="#07caf0",bg="white",command=start_game)
strt.pack()
strt.place(x=100,y=250)

adm=Button(win,text="Questionnaire",font=("bahnschrift semibold",25),fg="#07caf0",bg="white",command=questions)
adm.pack()
adm.place(x=100,y=370)

hlp=Button(win,text="Instructions",font=("bahnschrift semibold",25),fg="#07caf0",bg="white",command=instruct)
hlp.pack()
hlp.place(x=100,y=490)

abt=Button(win,text="About",font=("bahnschrift semibold",25),fg="#07caf0",bg="white",command=about)
abt.pack()
abt.place(x=100,y=610)

end=Button(win,text="Exit to Windows",font=("bahnschrift semibold",25),fg="white",bg="#07caf0",command=lambda:win.destroy())
end.pack()
end.place(x=1160,y=600)

win.mainloop()
