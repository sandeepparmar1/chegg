
from tkinter import *
from PIL import ImageTk,Image
from tkinter.ttk import Combobox,Treeview,Style,Scrollbar
import sqlite3
from tkinter import messagebox
from re import findall
from datetime import datetime


con=sqlite3.connect(database="bank")
curobj=con.cursor()
try:
    curobj.execute("create table account_details(account_no integer primary key autoincrement,account_name text,account_password text,account_email text,account_mob text,account_type text,account_bal float,account_opendate text)")
    curobj.execute("create table txn(txn_account_no int,txn_amt float,txn_update_bal float,txn_date text,txn_type text,foreign key(txn_account_no) REFERENCES account_details(account_no))")
except:
    print("Database","Something went wrong in your database maybe tables already exsist")

con.commit()
con.close

#CREATING MAIN WINDOW
win=Tk()
win.state('zoomed')
imgmain=Image.open("Logos/mainbank.jpg").resize((1800,950))
imgtkmain=ImageTk.PhotoImage(imgmain,master=win)
lbl_image=Label(master=win,image=imgtkmain,bd=0)
lbl_image.place(x=0,y=0)

win.title("Banking Automation")

#TITLE OF MAIN WINDOW
lbl_title=Label(master=win,text="Banking Automation",font=("Arial",50,'bold','underline',),bg="#87C7D1")
lbl_title.place(x=450,y=20)


#ALL LOGOS AND IMAGES USED IN ALL FRAMES 
img=Image.open("Logos/logo4.png").resize((250,100))
imgtk=ImageTk.PhotoImage(img,master=win)
lbl_image=Label(master=win,image=imgtk,bd=0)
lbl_image.place(x=0,y=0)

#WITHDRAW LOGO
imgwd=Image.open("Logos/logo4 - Copy.png").resize((250,100))
imgtkwd=ImageTk.PhotoImage(imgwd,master=win)


lbl_image=Label(master=win,image=imgtk,bd=0)
lbl_image.place(x=0,y=0)

#login page logo
img1=Image.open("Logos/logonew-color.jpg").resize((250,100))
imgtk1=ImageTk.PhotoImage(img1,master=win)


#account number logo
img2=Image.open("Logos/login2.png").resize((30,40))
imgtk2=ImageTk.PhotoImage(img2,master=win)


#password logo
img3=Image.open("Logos/passwordicon1.png").resize((30,40))
imgtk3=ImageTk.PhotoImage(img3,master=win)

#USER PAGE PICTURE
user_image=Image.open('Logos/newuser.jpg').resize((1700,850))
imagetkuser=ImageTk.PhotoImage(user_image,master=win)

#USER CHASE PAGE LOGO
user_logo=Image.open("Logos/userchaselogo.png").resize((100,100))
user_logotk=ImageTk.PhotoImage(user_logo,master=win)

#USER NAME ENTER IMAGE
userimage=Image.open("Logos/username.png").resize((30,40))
userimagetk=ImageTk.PhotoImage(userimage,master=win)

#USER PHONE ICON
phoneimage=Image.open("Logos/phoneicon.jpg").resize((30,40))
phoneimagetk=ImageTk.PhotoImage(phoneimage,master=win)

#USER EMAIL ICON
emailimage=Image.open("Logos/emailicon.jpeg").resize((30,40))
emailimagetk=ImageTk.PhotoImage(emailimage,master=win)

#USER PASSWORD ICON
pswrdimage=Image.open("Logos/passwordicon2.png").resize((30,40))
pswrdimagetk=ImageTk.PhotoImage(pswrdimage,master=win)

#BACK BUTTON IMAGE
img4=Image.open("Logos/backbutton.png").resize((50,60))
imgtk4=ImageTk.PhotoImage(img4,master=win)
#BACK BUTTON IMAGE
img5=Image.open("Logos/backbuttoncopy.png").resize((50,60))
imgtk5=ImageTk.PhotoImage(img5,master=win)

#LOGOUT IMAGE
logimage=Image.open("Logos/logoutimage.jpg").resize((100,100))
logimagetk=ImageTk.PhotoImage(logimage,master=win)
#LOGIN IMAGE
login_image=Image.open("Logos/login.jpg").resize((773,782))
login_imagetk=ImageTk.PhotoImage(login_image,master=win)


#NEW USER WINDOW
def new_user():
    frm2.destroy()
    frm.destroy()

    new_frm=Frame(win)
    new_frm.configure(bg="#F0F0FF",bd=0)
    new_frm.place(x=0,y=0,height=950,width=1550)
    
    #NEW FRAME FOR USER ENTRIES
    entry_frm1=Frame(win)
    entry_frm1.configure(bg="Black")
    entry_frm1.place(x=363,y=22,height=790,width=780)
    
    entry_frm=Frame(win)
    entry_frm.configure(bg="#FFFFEF")
    entry_frm.place(x=360,y=25,height=780,width=775)

    def dstry():
        new_frm.destroy()
        entry_frm.destroy()
        entry_frm1.destroy()
        login_screen()
#SETTING ENTER KEY WORK
    def enter_key(event):
        user_mob.focus_set()
        
    def enter_key2(event):
        user_email.focus_set()


    def enter_key3(event):
        user_pswrd.focus_set()

#FOCUSIN EVENT FOR USER NAME

    def text(Event):
        Text=user_name.get()
        if(Text=="Enter your name"):
            user_name.delete(0,'end')
        else:
            pass

        
        
#FOCUS OUT EVENT FOR USER NAME
    def text_focusout(Event):
        Text=user_name.get()
        if(Text==""):
            user_name.insert('end',"Enter your name")
        else:
            pass
        
    user_name=Entry(entry_frm,width=25,font=('Arial',26),bd=4)
    user_name.configure(highlightthickness=0.5,highlightcolor="blue")
    user_name.insert(0,"Enter your name")
    user_name.place(x=130,y=120)
    #USER NAME ENTRY BOX BINDING
    user_name.bind("<FocusIn>",text)
    user_name.bind("<FocusOut>",text_focusout)
    user_name.bind("<Return>",enter_key)

#FOCUSIN EVENT FOR USER MOBILE NUMBER
    def text1(Event):
        Text=user_mob.get()
        if(Text=="Enter your mobile number"):
            user_mob.delete(0,'end')
        else:
            pass

        
        
#FOCUS OUT EVENT FOR USER BOBILE NUMBER
    def text_focusout1(Event):
        Text=user_mob.get()
        if(Text==""):
            user_mob.insert('end',"Enter your mobile number")
        else:
            pass

    user_mob=Entry(entry_frm,width=25,font=('Arial',26),bd=4)
    user_mob.configure(highlightthickness=0.5,highlightcolor="blue")
    user_mob.insert(0,"Enter your mobile number")
    user_mob.place(x=130,y=200)
    #MOBILE NUMBER ENTRY BOX BINDING
    user_mob.bind("<FocusIn>",text1)
    user_mob.bind("<FocusOut>",text_focusout1)
    user_mob.bind("<Return>",enter_key2)
    
    
    #FOCUSIN EVENT FOR PASSWORD    
    def text2(Event):
        Text=user_pswrd.get()
        if(Text=="Enter your password"):
            user_pswrd.delete(0,'end')
        else:
            pass

        
        
#FOCUS OUT EVENT FOR PASSWORD
    def text_focusout2(Event):
        Text=user_pswrd.get()
        if(Text==""):
            user_pswrd.insert('end',"Enter your password")
        else:
            pass

    user_pswrd=Entry(entry_frm,width=25,font=('Arial',26),bd=4,)
    user_pswrd.configure(highlightthickness=0.5,highlightcolor="blue")
    user_pswrd.insert(0,"Enter your password")
    user_pswrd.place(x=130,y=360)
    #PASSWORD ENTRY BOX BINDING
    user_pswrd.bind("<FocusIn>",text2)
    user_pswrd.bind("<FocusOut>",text_focusout2)
    

    
    
#FOCUSIN EVENT FOR PASSWORD    
    def text3(Event):
        Text=user_email.get()
        if(Text=="Enter your email id"):
            user_email.delete(0,'end')
        else:
            pass

        
        
#FOCUS OUT EVENT FOR PASSWORD
    def text_focusout3(Event):
        Text=user_email.get()
        if(Text==""):
            user_email.insert('end',"Enter your email id")
        else:
            pass

    user_email=Entry(entry_frm,width=25,font=('Arial',26),bd=4,)
    user_email.configure(highlightthickness=0.5,highlightcolor="blue")
    user_email.insert(0,"Enter your email id")
    user_email.place(x=130,y=280)
    #PASSWORD ENTRY BOX BINDING
    user_email.bind("<FocusIn>",text3)
    user_email.bind("<FocusOut>",text_focusout3)
    user_email.bind("<Return>",enter_key3)
    
    
    cb_type=Combobox(entry_frm,values=["Saving account","Current account"],width=24,font=('Arial',26))
    cb_type.current(0)
    cb_type.place(x=130,y=440)
    
    #NEW USER PAGE IMAGE
    newuser_lbl=Label(master=new_frm,image=imagetkuser,bd=0)
    newuser_lbl.place(x=0,y=0)
    #USER CHASE PAGE LOGO
    user_logo_lbl=Label(master=entry_frm,image=user_logotk,bd=0)
    user_logo_lbl.place(x=0,y=0)
#USER NAME ICON
    name_image=Label(master=entry_frm,image=userimagetk,bg='#FFFFEF')
    name_image.place(x=90,y=123)
#USER PHONE ICON
    phone_image=Label(master=entry_frm,image=phoneimagetk,bg="#FFFFEF")
    phone_image.place(x=90,y=203)    
    
#USER EMAIL ICON
    email_image=Label(master=entry_frm,image=emailimagetk,bg="#FFFFEF")
    email_image.place(x=90,y=283)
#USER PASSWORD ICON
    pswrd_image=Label(master=entry_frm,image=pswrdimagetk,bg="#FFFFEF")
    pswrd_image.place(x=90,y=(283+80))
    
    def enter_button(event):
        button_image4.configure(bg="blue")
    def exit_button(event):
        button_image4.configure(bg='#C1C1CD')
#DONE BUTTON ENTRY EVENT        
    def done_button1(event):
        done_button.configure(bg="#e2fafe",fg="blue")
    def exitdone_button1(event):
        done_button.configure(bg='#F0F0FF',fg="black")
    
#DONE BUTTON FUNCTION 
    def done():
        name=user_name.get()
        mob=user_mob.get()
        email=user_email.get()
        pswrd=user_pswrd.get()
        acc_type=cb_type.get()
        if(name=="Enter your name" or name==""):
            name1=False
        else:
            name1=True
        if(mob=="Enter your mobile number" or mob==""):
            mob1=False
        else:
            mob1=True
        if(email=="Enter your email id" or email==""):
            email1=False
        else:
            email1=True
        if(pswrd=="Enter your password" or pswrd==""):
            pswrd1=False
        else:
            pswrd1=True
        if(acc_type=="Saving account" or acc_type=="Current account"):
            acc_type1=True
        else:
            acc_type1=False
        if(name1==False or mob1==False or email1==False or pswrd1==False or acc_type1==False):
            messagebox.showerror("Failed","Enter all fields")
            user_name.focus_set()
        
            
        if(name1==True):
            res=findall("[^(a-zA-Z)]",name)
    
        if(mob1==True):
            resu=findall('[\D]',mob)
        if(email1==True):
            resul=findall("[@]",email)
        try:        
            if(len(res)>0 or len(name)<=2):
                name1=False
                messagebox.showerror("Failed","Name is Incorrect")
                user_name.focus_set()
                
            elif(len(resu)>0 or len(mob)>10 or len(mob)<10):
                mob1=False
                messagebox.showerror("Failed","Number is greater or lesser then 10 digit don't use 0 or +91 before number")
                user_mob.focus_set()

            elif(len(resul)==0 or len(resul)>1):
                email1=False
                messagebox.showerror('Failed',"Email id is Incorrect")
                user_email.focus_set()
        except:
            pass
        if(acc_type=="Saving account"):
            bal=1000
        else:
            bal=10000
        date1=str(datetime.now().date())
        date=date1
        
        if(name1==True and mob1==True and email1==True and pswrd1==True and acc_type1==True):
            con=sqlite3.connect(database="bank")
            curobj=con.cursor()
            #if need use try except block
            curobj.execute("insert into account_details(account_name,account_password,account_email,account_mob,account_type,account_bal,account_opendate) values(?,?,?,?,?,?,?)",(name,pswrd,email,mob,acc_type,bal,date))
            con.commit()
            con.close
            con=sqlite3.connect(database="bank")
            curobj=con.cursor()
            a=curobj.execute("select max(account_no) from account_details")
            a=a.fetchone()
            messagebox.showinfo("Account number",f"Your account number is {a[0]}")
            dstry()
        
    #FORTH IMAGE BACK BUTTON
    button_image4=Button(master=new_frm,image=imgtk4,bd=0,bg='#C1C1CD',command=dstry)
    button_image4.place(x=0,y=0)
    button_image4.bind("<Enter>",enter_button)
    button_image4.bind("<Leave>",exit_button)

    #CREATING DONE BUTTON
    done_button=Button(entry_frm,text='    Done    ',font=('Arial',20,'bold'),bd=5,bg="#F0F0FF",command=done)
    done_button.place(x=280,y=523)
    #BINDING DONE BUTTON
    done_button.bind("<Enter>",done_button1)
    done_button.bind("<Leave>",exitdone_button1)
    
    
    lbl_title=Label(master=entry_frm,text="Sign up",font=("Arial",50,'bold',),bg="#FFFFEF")
    lbl_title.place(x=250,y=0)

    
    
    
#FORGOT PASSWORD
def forgot_password():
    frm2.destroy()
    frm.destroy()
    forgot_frm=Frame(win)
    forgot_frm.configure(bg="#F0F0FF",bd=0)
    forgot_frm.place(x=0,y=0,height=950,width=1550)
    
    #NEW FRAME FOR FORGOT PASSWORD
    forgot_entry_frm1=Frame(win)
    forgot_entry_frm1.configure(bg="Black")
    forgot_entry_frm1.place(x=363,y=22,height=790,width=780)
    
    forgot_entry_frm=Frame(win)
    forgot_entry_frm.configure(bg="#FFFFEF")
    forgot_entry_frm.place(x=360,y=25,height=780,width=775)

    def dstry():
        forgot_frm.destroy()
        forgot_entry_frm.destroy()
        forgot_entry_frm1.destroy()
        login_screen()
#BACK BUTTON EVENT
    def enter_button(event):
        button_image4.configure(bg="blue")
    def exit_button(event):
        button_image4.configure(bg='#C1C1CD')
#DONE BUTTON ENTRY EVENT        
    def done_button1(event):
        done_button.configure(bg="#e2fafe",fg="blue")
    def exitdone_button1(event):
        done_button.configure(bg='#F0F0FF',fg="black")

#NEW USER PAGE IMAGE
    forgot_lbl=Label(master=forgot_frm,image=imagetkuser,bd=0)
    forgot_lbl.place(x=0,y=0)
#USER CHASE PAGE LOGO
    user_logo_lbl=Label(master=forgot_entry_frm,image=user_logotk,bd=0)
    user_logo_lbl.place(x=0,y=0)
#USER NAME ICON
    name_image=Label(master=forgot_entry_frm,image=userimagetk,bg='#FFFFEF')
    name_image.place(x=90,y=123)
#USER PHONE ICON
    phone_image=Label(master=forgot_entry_frm,image=phoneimagetk,bg="#FFFFEF")
    phone_image.place(x=90,y=203)    
    
#USER EMAIL ICON
    email_image=Label(master=forgot_entry_frm,image=emailimagetk,bg="#FFFFEF")
    email_image.place(x=90,y=283)

#SETTING ENTER KEY WORK
    def enter_key(event):
        user_mob.focus_set()
        
    def enter_key2(event):
        user_email.focus_set()


#FOCUSIN EVENT FOR USER NAME

    def text(Event):
        Text=user_name.get()
        if(Text=="Enter your account number"):
            user_name.delete(0,'end')
        else:
            pass

        
        
#FOCUS OUT EVENT FOR USER NAME
    def text_focusout(Event):
        Text=user_name.get()
        if(Text==""):
            user_name.insert('end',"Enter your account number")
        else:
            pass
        
    user_name=Entry(forgot_entry_frm,width=25,font=('Arial',26),bd=4)
    user_name.configure(highlightthickness=0.5,highlightcolor="blue")
    user_name.insert(0,"Enter your account number")
    user_name.place(x=130,y=120)
    #USER NAME ENTRY BOX BINDING
    user_name.bind("<FocusIn>",text)
    user_name.bind("<FocusOut>",text_focusout)
    user_name.bind("<Return>",enter_key)

#FOCUSIN EVENT FOR USER MOBILE NUMBER
    def text1(Event):
        Text=user_mob.get()
        if(Text=="Enter your mobile number"):
            user_mob.delete(0,'end')
        else:
            pass

        
        
#FOCUS OUT EVENT FOR USER MOBILE NUMBER
    def text_focusout1(Event):
        Text=user_mob.get()
        if(Text==""):
            user_mob.insert('end',"Enter your mobile number")
        else:
            pass

    user_mob=Entry(forgot_entry_frm,width=25,font=('Arial',26),bd=4)
    user_mob.configure(highlightthickness=0.5,highlightcolor="blue")
    user_mob.insert(0,"Enter your mobile number")
    user_mob.place(x=130,y=200)
    #MOBILE NUMBER ENTRY BOX BINDING
    user_mob.bind("<FocusIn>",text1)
    user_mob.bind("<FocusOut>",text_focusout1)
    user_mob.bind("<Return>",enter_key2)
    
    
#FOCUSIN EVENT FOR EMAIL    
    def text3(Event):
        Text=user_email.get()
        if(Text=="Enter your email id"):
            user_email.delete(0,'end')
        else:
            pass

        
        
#FOCUS OUT EVENT FOR EMAIL
    def text_focusout3(Event):
        Text=user_email.get()
        if(Text==""):
            user_email.insert('end',"Enter your email id")
        else:
            pass

    user_email=Entry(forgot_entry_frm,width=25,font=('Arial',26),bd=4,)
    user_email.configure(highlightthickness=0.5,highlightcolor="blue")
    user_email.insert(0,"Enter your email id")
    user_email.place(x=130,y=280)
    #EMAIL ENTRY BOX BINDING
    user_email.bind("<FocusIn>",text3)
    user_email.bind("<FocusOut>",text_focusout3)
    
    def done():
        name=user_name.get()
        mob=user_mob.get()
        email=user_email.get()

        if(name=="Enter your account number" or name==""):
            name1=False
            messagebox.showerror("Failed","Enter correct account number")
            user_name.focus_set()
        elif(mob=="Enter your mobile number" or mob==""):
            mob1=False
            messagebox.showerror("Failed","Enter correct mobile number")
            user_mob.focus_set()
        elif(email=="Enter your email id" or email==""):
            email1=False
            messagebox.showerror("Failed","Enter correct email id")
            user_email.focus_set()
        elif(True):
            con=sqlite3.connect(database="bank")
            curobj=con.cursor()
            try:
                curobj.execute("select account_password from account_details where account_no=? and account_email=? and account_mob=?",(name,email,mob))
            except:
                pass
            tup=curobj.fetchall()
            con.close()
            if(len(tup)==0):
                messagebox.showerror("Failed","Check again details not matched")
            else:
                messagebox.showinfo("Details",f"your account password is {tup[0]}")
                dstry()

    
    
    
    
    #FORTH IMAGE BACK BUTTON
    button_image4=Button(master=forgot_frm,image=imgtk4,bd=0,bg='#C1C1CD',command=dstry)
    button_image4.place(x=0,y=0)
    button_image4.bind("<Enter>",enter_button)
    button_image4.bind("<Leave>",exit_button)
    #CREATING GET PASSWORD BUTTON
    done_button=Button(forgot_entry_frm,text='Get password',font=('Arial',20,'bold'),bd=5,bg="#F0F0FF",command=done)
    done_button.place(x=280,y=523)
    #BINDING DONE BUTTON
    done_button.bind("<Enter>",done_button1)
    done_button.bind("<Leave>",exitdone_button1)
 
    
    lbl_title=Label(master=forgot_entry_frm,text="Forgot Password?",font=("Arial",40,'bold',),bg="#FFFFEF")
    lbl_title.place(x=180,y=0)
    
    
    
    
    
#LOGIN WINDOW 
def login_screen():
    
    
#LOGIN FRAMES
    global frm2, frm
    frm2=Frame(win)
    frm2.configure(bg='Black')
    frm2.place(x=500,y=120,width=560,height=710)
    
    frm=Frame(win)
    frm.configure(bg='#C1C1CD')
    frm.place(x=500,y=120,width=550,height=700)
    
    
# IMAGES USED ON LOGIN SCREEN
#First image #LOGIN LOGO
    lbl_image1=Label(master=frm,image=imgtk1,bd=0)
    lbl_image1.place(x=150,y=550)
#second image #ACCOUNT NUMBER LOGO 
    lbl_image2=Label(master=frm,image=imgtk2,bg='#C1C1CD')
    lbl_image2.place(x=45,y=123)
#third image #ACCOUNT PASSWORD LOGO
    lbl_image3=Label(master=frm,image=imgtk3,bg='#C1C1CD')
    lbl_image3.place(x=45,y=223)

    def login_details():
        acn=login_entry.get()
        pswrd=pswrd_entry.get()
        a=findall("[^(0-9)]",acn)
        if(acn=="Enter account number" or acn=="" or len(a)>0 ):#or len(result)>0):
            messagebox.showerror("Failed","Enter correct account number")
            login_entry.focus_set()
            
        elif(pswrd=="Enter Password" or pswrd==""):
            messagebox.showerror("Failed","Enter correct password")
            pswrd_entry.focus_set()
        else:
            con=sqlite3.connect(database="bank")
            curobj=con.cursor()
            curobj.execute("select * from account_details where account_no=? and account_password=?",(acn,pswrd))
            global details
            details=(curobj.fetchone())
            if(details==None):
                messagebox.showerror("Database","No data found")
                login_entry.focus_set()
            else:
                login_()

            
#SETTING ENTER KEY WORK
    def enter_key(event):
        pswrd_entry.focus_set()    
    def enter_key2(event):
        login_details()    
    
#FOCUSIN EVENT FOR LOGIN ACCOUNT NUMBER
    def text(Event):
        Text=login_entry.get()
        if(Text=="Enter account number"):
            login_entry.delete(0,'end')
        else:
            pass
        
#FOCUS OUT EVENT FOR LOGIN ACCOUNT NUMBER
    def text_focusout(Event):
        Text=login_entry.get()
        if(Text==""):
            login_entry.insert('end',"Enter account number")
        else:
            pass

#FOCUSIN EVENT FOR LOGIN PASSWORD
    def pswrd_text(Event):
        pswrd=pswrd_entry.get()
        if(pswrd=="Enter Password"):
            pswrd_entry.delete(0,'end')
        else:
            pass
#FOCUS OUT EVENT FOR LOGIN PASSWORD

    def pswrd_focusout(Event):
        pswrd=pswrd_entry.get()
        if(pswrd==""):
            pswrd_entry.insert('end',"Enter Password")
        else:
            pass

    

    #CREATING LOGIN ACCOUNT NUMBER ENTRY BOX
    login_entry=Entry(frm,width=20,font=('Arial',26),bd=5,)
    login_entry.configure(highlightthickness=0.5,highlightcolor="blue")
    login_entry.insert(0,"Enter account number")
    login_entry.place(x=85,y=120)
    #ACCOUNT NUMBER LOGIN ENTRY BOX BINDING
    login_entry.bind("<FocusIn>",text)
    login_entry.bind("<FocusOut>",text_focusout)
    login_entry.bind("<Return>",enter_key)
    

    #CREATING LOGIN PASSWORD ENTRY BOX
    pswrd_entry=Entry(frm,font=('Arial',26,),bd=5)
    pswrd_entry.configure(highlightthickness=0.5,highlightcolor="blue")
    pswrd_entry.insert(0,"Enter Password")
    pswrd_entry.place(x=85,y=220)
    
    #PASSWORD ENTRY BINDING
    pswrd_entry.bind("<FocusIn>",pswrd_text)
    pswrd_entry.bind("<FocusOut>",pswrd_focusout)
    pswrd_entry.bind("<Return>",enter_key2)
    
    
    #CREATING LOGIN BUTTON WITH 26,26 SPACES EACH SIDE
    login_button=Button(frm,text='                          LOGIN                         ',command=login_details,font=('Arial',15,'bold'),bd=5,bg="green",fg="White")
    login_button.place(x=85,y=300)

    
#USER BUTTON ENTRY EVENT        
    def done_button1(event):
        user_button.configure(bg="#e2fafe",fg="blue")
    def exitdone_button1(event):
        user_button.configure(bg='#F0F0FF',fg="black")
#FORGOT PASSWORD BUTTON ENTRY EVENT        
    def done_button2(event):
        fgpswrd_button.configure(bg="#e2fafe",fg="blue")
    def exitdone_button2(event):
        fgpswrd_button.configure(bg='#F0F0FF',fg="black")

    #CREATING USER BUTTON
    user_button=Button(frm,text='NEW USER',font=('Arial',15,'bold'),bd=5,command=new_user,bg='#F0F0FF')
    user_button.place(x=350,y=380)
    #BINDING USER BUTTON
    user_button.bind("<Enter>",done_button1)
    user_button.bind("<Leave>",exitdone_button1)
    
    #CREATING FORGOT PASSWORD BUTTON
    fgpswrd_button=Button(frm,text='FORGOT PASSWORD?',font=('Arial',15,'bold'),bd=5,command=forgot_password,bg='#F0F0FF')
    fgpswrd_button.place(x=85,y=380)
    #BINDING FORGOT BUTTON
    fgpswrd_button.bind("<Enter>",done_button2)
    fgpswrd_button.bind("<Leave>",exitdone_button2)
    
    #CREATING SHOW PASSWORD BUTTON
    show_button=Label(frm,text="Show",bg='#C1C1CD',fg="blue")
    #PLACE ONCE NEW USER BUTTON PAGE IS COMPLETE
    
def login_():
                frm.destroy()
                frm2.destroy()
                log_frm=Frame(win)
                log_frm.configure(bg="#F0F0FF",bd=0)
                log_frm.place(x=0,y=0,height=950,width=1550)
                lbl_image=Label(master=log_frm,image=imgtkmain,bd=0)
                lbl_image.place(x=0,y=0)
                
                
                
                #NEW FRAME FOR USER ENTRIES
                entry_frm1=Frame(log_frm)
                entry_frm1.configure(bg="Black")
                entry_frm1.place(x=363,y=22,height=790,width=780)
    
                #CHECK BALANCE
                def done_button2(event):
                    check_balance.configure(fg="blue")
                def exitdone_button2(event):
                    check_balance.configure(fg="black")
                
                #WITHDRAW
                def done_button3(event):
                    withdraw_balance.configure(fg="blue")
                def exitdone_button3(event):
                    withdraw_balance.configure(fg="black")
                #DEPOSIT
                def done_button4(event):
                    deposit_balance.configure(fg="blue")
                def exitdone_button4(event):
                    deposit_balance.configure(fg="black")
                #transfer
                def done_button5(event):
                    transfer_balance.configure(fg="blue")
                def exitdone_button5(event):
                    transfer_balance.configure(fg="black")
                #UPDATE
                def done_button6(event):
                    update_profile.configure(fg="blue")
                def exitdone_button6(event):
                    update_profile.configure(fg="black")

                #TXN_HISTORY
                def done_button7(event):
                    txn_his.configure(fg="blue")
                def exitdone_button7(event):
                    txn_his.configure(fg="black")


                #LOGOUT BUTTON
                def enter_button(event):
                    logout.configure(bg="blue")
                def exit_button(event):
                    logout.configure(bg='#C1C1CD')
                    
                #CHECK BALANCE FUNCTION
                def chk_bal():
                    global BG_frm1,entry_frm2,frm
                    entry_frm1.place_forget()
                    
                    try:
                        if(frm2==True):
                            BG_frm2.destroy()
                            entry_frm3.destroy()
                    except:
                        pass
                      
                    try:
                         if(txnhis==True):
                            BG_frm5.destroy()
                            entry_frm5.destroy()
                    except:
                        pass
                    
                    
                    try:
                        if(update_profile1==True):
                            BG_frm3.destroy()
                            entry_frm4.destroy()
                    except:
                        pass
                    
                    try:
                        if(frmwithdraw1==True):
                            BG_frm.destroy()
                            wd_frm.destroy()
                    except:
                        pass
                    
                    try:
                        if(deposit1==True):
                            BGdp_frm.destroy()
                            dp_frm.destroy()
                    except:
                            pass
    
                
                    
                    BG_frm1=Frame(log_frm)
                    BG_frm1.configure(bg="brown")
                    BG_frm1.place(x=460,y=150,height=610,width=760)
                    
                    entry_frm2=Frame(log_frm)
                    entry_frm2.configure(bg="#FFFFEF")
                    entry_frm2.place(x=460,y=150,height=600,width=750)
                    
                    con=sqlite3.connect(database="bank")
                    curobj=con.cursor()
                    curobj.execute("select * from account_details where account_no=?",(details[0],))
                    bal=curobj.fetchone()
                    con.close()
                    
                    acn_lbl=Label(master=entry_frm2,text=f"Account Number\t\t{bal[0]}",bg="#FFFFEF",font=('Arial',20,'bold'))
                    acn_lbl.place(x=100,y=200)

                    acn_type=Label(master=entry_frm2,text=f"Account Type\t\t{bal[5]}",bg="#FFFFEF",font=('Arial',20,'bold'))
                    acn_type.place(x=100,y=300)

                    avl_lbl=Label(master=entry_frm2,text=f"Available Balance\t\tRS:{bal[6]}",bg="#FFFFEF",font=('Arial',20,'bold'))
                    avl_lbl.place(x=100,y=400)

                    name_lbl=Label(master=entry_frm2,text=details[1],bg="#FFFFEF",font=('Arial',40,'bold'))
                    name_lbl.place(x=300,y=0)
                    frm=True

                    def dstry():
                        BG_frm1.destroy()
                        entry_frm2.destroy()
                        entry_frm1.place(x=363,y=22,height=790,width=780)
                     

                    button_image4=Button(master=entry_frm2,image=imgtk5,bd=0,bg='#C1C1CD',command=dstry)
                    button_image4.place(x=1,y=0)

                def withdraw_bal():
                    global BG_frm,wd_frm,frmwithdraw1
                    entry_frm1.place_forget()
                    try:
                        if(frm2==True):
                            BG_frm2.destroy()
                            entry_frm3.destroy()
                    except:
                        pass
                    
                    
                    try:
                         if(txnhis==True):
                            BG_frm5.destroy()
                            entry_frm5.destroy()
                    except:
                        pass
                    
                    
                    try:
                        if(update_profile1==True):
                            BG_frm3.destroy()
                            entry_frm4.destroy()
                    except:
                        pass
                    
                    try:
                        if(frm==True):
                            BG_frm1.destroy()
                            entry_frm2.destroy()
                    except:
                        pass
                    
                    try:
                        if(deposit1==True):
                            BGdp_frm.destroy()
                            dp_frm.destroy()
                    except:
                            pass
                        
                    def done():
                        bal=user_withdraw.get()
                        try:
                            bal1=float(bal)
                            if(bal1<0):
                                messagebox.showerror("Failed","Put positive value")
                                user_withdraw.delete(0,'end')
                                user_withdraw.focus_set()
                        except:
                            pass
                        if(True):
                            balance=findall("[^(0-9)]",bal)
                        if(len(balance)>0 or bal==""):
                            messagebox.showerror("Failed","enter correct value")
                            user_withdraw.delete(0,'end')
                            user_withdraw.focus_set()
                        else:
                            dt=str(datetime.now())
                            bal=float(bal)
                            con=sqlite3.connect(database="bank")
                            curobj=con.cursor()
                            curobj.execute("select * from account_details where account_no=?",(details[0],))
                            upd_bal=curobj.fetchone()
                            con.close()
                            baln=float(upd_bal[6])
                            if(baln>bal):
                                con=sqlite3.connect(database="bank")
                                curobj=con.cursor()
                                curobj.execute("update account_details set account_bal=(account_bal-?) where account_no=?",(bal,details[0]))
                                curobj.execute("insert into txn values(?,?,?,?,?)",(details[0],bal,(baln-bal),dt,"Debit"))
                                con.commit()
                                con.close()
                                messagebox.showinfo("Deposit",f"Withdraw of {bal} done")
                                user_withdraw.delete(0,'end')
                                user_withdraw.focus_set()
                            else:
                                messagebox.showerror("Failed","Insufficient balance")
                        
                        #(7, 'sandy', '111', 'a@gmail.com', '7988667751', 'Current account', 10000.0, '2022-12-26')
                        #txn_account_no int,txn_amt float,txn_update_bal float,txn_date text,txn_type text,foreign key(txn_account_no)

    
    
    
                    BG_frm=Frame(log_frm)
                    BG_frm.configure(bg="brown")
                    BG_frm.place(x=460,y=150,height=610,width=760)

                    wd_frm=Frame(log_frm)
                    wd_frm.configure(bg="#FFFFEF")
                    wd_frm.place(x=460,y=150,height=600,width=750)
                    #FOCUSIN EVENT FOR TXN
                    def enter_key(event):
                        done()    
    

                    def text(Event):
                        Text=user_withdraw.get()
                        if(Text=="Enter Amount"):
                            user_withdraw.delete(0,'end')
                        else:
                            pass

        
        
                    #FOCUS OUT EVENT FOR TXN_WITHDRAW
                    def text_focusout(Event):
                        Text=user_withdraw.get()
                        if(Text==""):
                            user_withdraw.insert('end',"Enter Amount")
                        else:
                            pass

                    def done_button1(event):
                        done_button.configure(bg="#e2fafe",fg="blue")
                    def exitdone_button1(event):
                        done_button.configure(bg='#F0F0FF',fg="black")
                        
                    
                            
    
                
                    user_withdraw=Entry(wd_frm,width=25,font=('Arial',26),bd=4)
                    user_withdraw.configure(highlightthickness=0.5,highlightcolor="blue")
                    user_withdraw.insert(0,"Enter Amount")
                    user_withdraw.place(x=130,y=180)
                    user_withdraw.bind("<FocusIn>",text)
                    user_withdraw.bind("<FocusOut>",text_focusout)
                    user_withdraw.bind("<Return>",enter_key)
                    
                   #BINDING DONE BUTTON
                    userwd_lbl=Label(master=wd_frm,text="Withdraw",bd=0,font=('Arial',40,"bold"),bg="#FFFFEF")
                    userwd_lbl.place(relx=.35,rely=0)
                    done_button=Button(wd_frm,text='    Done    ',font=('Arial',20,'bold'),bd=5,bg="#F0F0FF",command=done)
                    done_button.place(x=280,y=320)
                    lbl_image=Label(master=wd_frm,image=imgtkwd,bd=0)
                    lbl_image.place(x=250,y=490)

                    
                    done_button.bind("<Enter>",done_button1)
                    done_button.bind("<Leave>",exitdone_button1)

                    
                    
                    
                    frmwithdraw1=True
                    def dstry():
                        BG_frm.destroy()
                        wd_frm.destroy()
                        
                        entry_frm1.place(x=363,y=22,height=790,width=780)
                     

                    button_image4=Button(master=wd_frm,image=imgtk5,bd=0,bg='#C1C1CD',command=dstry)
                    button_image4.place(x=1,y=0)
                    
                    
                    
                    
                    
                def deposit_bal():
                    global BGdp_frm,dp_frm,deposit1
                    entry_frm1.place_forget()
                    try:
                        if(frm2==True):
                            BG_frm2.destroy()
                            entry_frm3.destroy()
                    except:
                        pass
                    
                    
                    try:
                         if(txnhis==True):
                            BG_frm5.destroy()
                            entry_frm5.destroy()
                    except:
                        pass
                    
                    
                    try:
                        if(update_profile1==True):
                            BG_frm3.destroy()
                            entry_frm4.destroy()
                    except:
                        pass
                    
                    try:
                        if(frm==True):
                            BG_frm1.destroy()
                            entry_frm2.destroy()
                    except:
                        pass
                    
                    try:
                         if(frmwithdraw1==True):
                            BG_frm.destroy()
                            wd_frm.destroy()
                    except:
                        pass
    
    
    
                    BGdp_frm=Frame(log_frm)
                    BGdp_frm.configure(bg="brown")
                    BGdp_frm.place(x=460,y=150,height=610,width=760)

                    dp_frm=Frame(log_frm)
                    dp_frm.configure(bg="#FFFFEF")
                    dp_frm.place(x=460,y=150,height=600,width=750)
                    deposit1=True
                    def dstry():
                        BGdp_frm.destroy()
                        dp_frm.destroy()
                        entry_frm1.place(x=363,y=22,height=790,width=780)
                        
                        
                    def enter_key(event):
                        done()    
    
                    def text(Event):
                        Text=user_deposit.get()
                        if(Text=="Enter Amount"):
                            user_deposit.delete(0,'end')
                        else:
                            pass

        
        
                    #FOCUS OUT EVENT FOR TXN_WITHDRAW
                    def text_focusout(Event):
                        Text=user_deposit.get()
                        if(Text==""):
                            user_deposit.insert('end',"Enter Amount")
                        else:
                            pass
                    
                

                    def done_button1(event):
                        done_button.configure(bg="#e2fafe",fg="blue")
                    def exitdone_button1(event):
                        done_button.configure(bg='#F0F0FF',fg="black")
    
                    def done():
                        baln=user_deposit.get()
                        try:
                            bal1=float(baln)
                            if(bal1<0):
                                messagebox.showerror("Failed","Put positive value")
                                user_deposit.delete(0,'end')
                                user_deposit.focus_set()
                        except:
                            pass
                        if(True):
                            balance=findall("[^(0-9)]",baln)
                        if(len(balance)>0 or baln==""):
                            messagebox.showerror("Failed","enter correct value")
                            user_deposit.delete(0,'end')
                            user_deposit.focus_set()
                        else:
                            dt=str(datetime.now())
                            baln=float(baln)
                            con=sqlite3.connect(database="bank")
                            curobj=con.cursor()
                            curobj.execute("update account_details set account_bal=(account_bal+?) where account_no=?",(baln,details[0]))
                            con.commit()
                            con.close
                            con=sqlite3.connect(database="bank")
                            curobj=con.cursor()
                            curobj.execute("select * from account_details where account_no=?",(details[0],))
                            upd_bal=curobj.fetchone()
                            con.close()
                            con=sqlite3.connect(database="bank")
                            curobj=con.cursor()
                            curobj.execute("insert into txn values(?,?,?,?,?)",(details[0],baln,upd_bal[6],dt,"Credit"))
                            con.commit()
                            con.close()
                            messagebox.showinfo("Deposit",f"Deposit of {baln} done")
                            user_deposit.delete(0,'end')
                            user_deposit.focus_set()
                        
                        #(7, 'sandy', '111', 'a@gmail.com', '7988667751', 'Current account', 10000.0, '2022-12-26')
                        #txn_account_no int,txn_amt float,txn_update_bal float,txn_date text,txn_type text,foreign key(txn_account_no)

                    user_deposit=Entry(dp_frm,width=25,font=('Arial',26),bd=4)
                    user_deposit.configure(highlightthickness=0.5,highlightcolor="blue")
                    user_deposit.insert(0,"Enter Amount")
                    user_deposit.place(x=130,y=180)
                    user_deposit.bind("<FocusIn>",text)
                    user_deposit.bind("<FocusOut>",text_focusout)
                    user_deposit.bind("<Return>",enter_key)
                    userd_lbl=Label(master=dp_frm,text="Deposit",bd=0,font=('Arial',40,"bold"),bg="#FFFFEF")
                    userd_lbl.place(relx=.35,rely=0)
                    done_button=Button(dp_frm,text='    Done    ',font=('Arial',20,'bold'),bd=5,bg="#F0F0FF",command=done)
                    done_button.place(x=280,y=320)
                    lbl_image=Label(master=dp_frm,image=imgtkwd,bd=0)
                    lbl_image.place(x=250,y=490)

                    #BINDING DONE BUTTON
                    done_button.bind("<Enter>",done_button1)
                    done_button.bind("<Leave>",exitdone_button1)

                     

                    button_image4=Button(master=dp_frm,image=imgtk5,bd=0,bg='#C1C1CD',command=dstry)
                    button_image4.place(x=1,y=0)
                def transfer():
                    try:
                         if(frmwithdraw1==True):
                            BG_frm.destroy()
                            wd_frm.destroy()
                    except:
                        pass
                    
                    
                    try:
                         if(txnhis==True):
                            BG_frm5.destroy()
                            entry_frm5.destroy()
                    except:
                        pass
                    
                    
                    try:
                        if(update_profile1==True):
                            BG_frm3.destroy()
                            entry_frm4.destroy()
                    except:
                        pass
                    
                    try:
                        if(frm==True):
                            BG_frm1.destroy()
                            entry_frm2.destroy()
                    except:
                        pass
                    
                    
                    try:
                        if(deposit1==True):
                            BGdp_frm.destroy()
                            dp_frm.destroy()
                    except:
                            pass
    
    
    
                    global BG_frm2, entry_frm3,frm2
                    entry_frm1.place_forget()
                    BG_frm2=Frame(log_frm)
                    BG_frm2.configure(bg="brown")
                    BG_frm2.place(x=460,y=150,height=610,width=760)

                    entry_frm3=Frame(log_frm)
                    entry_frm3.configure(bg="#FFFFEF")
                    entry_frm3.place(x=460,y=150,height=600,width=750)
                    frm2=True
                    def dstry():
                        BG_frm2.destroy()
                        entry_frm3.destroy()
                        entry_frm1.place(x=363,y=22,height=790,width=780)
                    def done_button1(event):
                        done_button.configure(bg="#e2fafe",fg="blue")
                    def exitdone_button1(event):
                        done_button.configure(bg='#F0F0FF',fg="black")
                    
                    def text(Event):
                        Text=user_trnsfr.get()
                        if(Text=="Enter account number"):
                            user_trnsfr.delete(0,'end')
                        else:
                            pass

        
        
                    #FOCUS OUT EVENT FOR TXN_WITHDRAW
                    def text_focusout(Event):
                        Text=user_trnsfr.get()
                        if(Text==""):
                            user_trnsfr.insert('end',"Enter account number")
                        else:
                            pass
                    def text1(Event):
                        Text=user_trnsfr_bal.get()
                        if(Text=="Enter amount"):
                            user_trnsfr_bal.delete(0,'end')
                        else:
                            pass

                    def enter_key(event):
                        user_trnsfr_bal.focus_set() 
                    def enter_key2(event):
                        done()    
        
        
                    #FOCUS OUT EVENT FOR TXN_WITHDRAW
                    def text_focusout1(Event):
                        Text=user_trnsfr_bal.get()
                        if(Text==""):
                            user_trnsfr_bal.insert('end',"Enter amount")
                        else:
                            pass   

                    def done():
                        acc=user_trnsfr.get()
                        baln=user_trnsfr_bal.get()
                        if(True):
                            balance=findall("[^(0-9)]",acc)
                        if(len(balance)>0 or acc=="" or acc=="Enter account number" or int(acc)==int(details[0])):
                            messagebox.showerror("Failed","enter correct value")
                            user_trnsfr.delete(0,'end')
                            user_trnsfr.focus_set()
                        else:
                            con=sqlite3.connect(database="bank")
                            curobj=con.cursor()
                            curobj.execute("select * from account_details where account_no=?",(int(acc),))
                            data=curobj.fetchall()
                            print(len(data))
                            con.close()
                            if(len(data)>0):
                                try:
                                    bal1=float(baln)
                                    if(bal1<0):
                                        messagebox.showerror("Failed","Put positive value")
                                        user_trnsfr_bal.delete(0,'end')
                                        user_trnsfr_bal.focus_set()
                                except:
                                    pass
                                if(True):
                                    balance=findall("[^(0-9)]",baln)
                                    if(len(balance)>0 or baln==""):
                                        messagebox.showerror("Failed","enter correct value")
                                        user_deposit.delete(0,'end')
                                        user_deposit.focus_set()
                                    else:
                                        dt=str(datetime.now())
                                        bal=float(baln)
                                        con=sqlite3.connect(database="bank")
                                        curobj=con.cursor()
                                        curobj.execute("select * from account_details where account_no=?",(details[0],))
                                        upd_bal=curobj.fetchone()
                                        curobj.execute("select * from account_details where account_no=?",(int(acc),))
                                        update_bal=curobj.fetchone()
                                        print(update_bal)
                                        con.close()
                                        baln=float(upd_bal[6])
                                        if(baln>bal):
                                            con=sqlite3.connect(database="bank")
                                            curobj=con.cursor() 
                                            curobj.execute("update account_details set account_bal=?-? where account_no=?",(baln,bal,details[0]))
                                            curobj.execute("insert into txn values(?,?,?,?,?)",(details[0],bal,upd_bal[6]-bal,dt,"Debit"))
                                            #txn_account_no int,txn_amt float,txn_update_bal float,txn_date text,txn_type text
                                            curobj.execute("update account_details set account_bal=?+? where account_no=?",(update_bal[6],bal,int(acc)))
                                            curobj.execute("insert into txn values(?,?,?,?,?)",(int(acc),bal,update_bal[6]+bal,dt,"Credit"))
                                            con.commit()
                                            con.close()
                                            messagebox.showinfo("Deposit",f"Deposit of {bal} done")
                                            user_trnsfr.delete(0,'end')
                                            user_trnsfr_bal.delete(0,'end')
                                            user_trnsfr.focus_set()
                                        else:
                                            messagebox.showerror("Failed","Insufficient balance")
                            if(len(data)==0):
                                        messagebox.showerror("Failed","no such account exists")
                                        
                                                               
                        #(7, 'sandy', '111', 'a@gmail.com', '7988667751', 'Current account', 10000.0, '2022-12-26')
                        #txn_account_no int,txn_amt float,txn_update_bal float,txn_date text,txn_type text,foreign key(txn_account_no)

                    
                    user_trnsfr=Entry(entry_frm3,width=25,font=('Arial',26),bd=4)
                    user_trnsfr.configure(highlightthickness=0.5,highlightcolor="blue")
                    user_trnsfr.insert(0,"Enter account number")
                    user_trnsfr.place(x=130,y=120)
                    user_trnsfr.bind("<FocusIn>",text)
                    user_trnsfr.bind("<FocusOut>",text_focusout)
                    user_trnsfr.bind("<Return>",enter_key)
                    
                    user_trnsfr_bal=Entry(entry_frm3,width=25,font=('Arial',26),bd=4)
                    user_trnsfr_bal.configure(highlightthickness=0.5,highlightcolor="blue")
                    user_trnsfr_bal.insert(0,"Enter amount")
                    user_trnsfr_bal.place(x=130,y=200)
                    user_trnsfr_bal.bind("<FocusIn>",text1)
                    user_trnsfr_bal.bind("<FocusOut>",text_focusout1)
                    user_trnsfr_bal.bind("<Return>",enter_key2)
                    
                    
                    usertrnsfr_lbl=Label(master=entry_frm3,text="Transfer",bd=0,font=('Arial',40,"bold"),bg="#FFFFEF")
                    usertrnsfr_lbl.place(relx=.35,rely=0)
                    done_button=Button(entry_frm3,text='    Done    ',font=('Arial',20,'bold'),bd=5,bg="#F0F0FF",command=done)
                    done_button.place(x=280,y=320)
                    lbl_image=Label(master=entry_frm3,image=imgtkwd,bd=0)
                    lbl_image.place(x=250,y=490)

                    #BINDING DONE BUTTON
                    done_button.bind("<Enter>",done_button1)
                    done_button.bind("<Leave>",exitdone_button1)

                     

                    button_image4=Button(master=entry_frm3,image=imgtk5,bd=0,bg='#C1C1CD',command=dstry)
                    button_image4.place(x=1,y=0)

                def updateprofile():
                    try:
                         if(frmwithdraw1==True):
                            BG_frm.destroy()
                            wd_frm.destroy()
                    except:
                        pass
                    
                    
                    try:
                         if(txnhis==True):
                            BG_frm5.destroy()
                            entry_frm5.destroy()
                    except:
                        pass
                    
                    
                    try:
                        if(frm2==True):
                            BG_frm2.destroy()
                            entry_frm3.destroy()
                    except:
                        pass
                    
                    try:
                        if(frm==True):
                            BG_frm1.destroy()
                            entry_frm2.destroy()
                    except:
                        pass
                    
                    
                    try:
                        if(deposit1==True):
                            BGdp_frm.destroy()
                            dp_frm.destroy()
                    except:
                            pass
    
    
                    global BG_frm3,entry_frm4,update_profile1
                    entry_frm1.place_forget()
                    BG_frm3=Frame(log_frm)
                    BG_frm3.configure(bg="brown")
                    BG_frm3.place(x=460,y=150,height=610,width=760)
                    

                    entry_frm4=Frame(log_frm)
                    entry_frm4.configure(bg="#FFFFEF")
                    entry_frm4.place(x=460,y=150,height=600,width=750)
                    
                    def done():
                        name=user_update_name.get()
                        mob=user_update_mob.get()
                        email=user_update_email.get()
                        pwd=user_update_pwd.get()
                        res=findall("[^(a-zA-Z)]",name)
                        resu=findall('[\D]',mob)
                        resul=findall("[@]",email)
                        if(name=="" or mob=="" or email=="" or pwd==""):
                            messagebox.showerror("Failed","Enter correct value no empty field allowed")
                        elif(len(res)>0 or len(name)<2):
                            messagebox.showerror("Failed","Enter correct name")
                            user_update_name.focus_set()
                        elif(len(resu)>0 or len(mob)>10 or len(mob)<10):
                            messagebox.showerror("Failed","Number is greater or lesser then 10 digit don't use 0 or +91 before number")
                            user_update_mob.focus_set()
                        
                        elif(len(resul)==0 or len(resul)>1):
                            messagebox.showerror('Failed',"Email id is Incorrect")
                            user_update_email.focus_set()
                        elif(name==details[1] and mob==details[4] and email==details[3] and pwd==details[2]):
                            messagebox.showinfo("Update","No new information to add")
                        elif(True):
                            con=sqlite3.connect(database="bank")
                            curobj=con.cursor()
                            curobj.execute("update account_details set account_name=?,account_mob=?,account_email=?,account_password=? where account_no=?",(name,mob,email,pwd,details[0]))
                            con.commit()
                            con.close()
                            messagebox.showinfo("Updated","Your profile is updated login again")
                            log_frm.destroy()
                            entry_frm1.destroy()
                            login_screen()
                                
                            
        
                    
                    
                    def enter_key(event):
                        user_update_mob.focus_set()
                    def enter_key1(event):
                        user_update_email.focus_set()
                    def enter_key2(event):
                        user_update_pwd.focus_set()
                    def enter_key3(event):
                        done()
        
                    
                    upd_lbl=Label(master=entry_frm4,text="Update profile",bd=0,font=('Arial',40,"bold"),bg="#FFFFEF")
                    upd_lbl.place(relx=.28,rely=0)
                    upd_name_lbl=Label(master=entry_frm4,text="Name ",bd=0,font=('Arial',20,"bold"),bg="#FFFFEF")
                    upd_name_lbl.place(x=130,y=100)
                    user_update_name=Entry(entry_frm4,width=25,font=('Arial',26),bd=4)
                    user_update_name.configure(highlightthickness=0.5,highlightcolor="blue")
                    user_update_name.place(x=130,y=130)
                    user_update_name.insert('end',details[1])
                    user_update_name.bind("<Return>",enter_key)
                    upd_mob_lbl=Label(master=entry_frm4,text="Mobile number",bd=0,font=('Arial',20,"bold"),bg="#FFFFEF")
                    upd_mob_lbl.place(x=130,y=200)
                    
                    user_update_mob=Entry(entry_frm4,width=25,font=('Arial',26),bd=4)
                    user_update_mob.configure(highlightthickness=0.5,highlightcolor="blue")
                    user_update_mob.place(x=130,y=230)
                    user_update_mob.insert("end",details[4])
                    user_update_mob.bind("<Return>",enter_key1)
                    
                    upd_email_lbl=Label(master=entry_frm4,text="Email",bd=0,font=('Arial',20,"bold"),bg="#FFFFEF")
                    upd_email_lbl.place(x=130,y=300)
                    
                    user_update_email=Entry(entry_frm4,width=25,font=('Arial',26),bd=4)
                    user_update_email.configure(highlightthickness=0.5,highlightcolor="blue")
                    user_update_email.place(x=130,y=330)
                    user_update_email.insert("end",details[3])
                    user_update_email.bind("<Return>",enter_key2)
                    
                    
                    upd_pwd_lbl=Label(master=entry_frm4,text="Password",bd=0,font=('Arial',20,"bold"),bg="#FFFFEF")
                    upd_pwd_lbl.place(x=130,y=400)
                    
                    user_update_pwd=Entry(entry_frm4,width=25,font=('Arial',26),bd=4)
                    user_update_pwd.configure(highlightthickness=0.5,highlightcolor="blue")
                    user_update_pwd.place(x=130,y=430)
                    user_update_pwd.insert("end",details[2])
                    user_update_pwd.bind("<Return>",enter_key3)
                    
                    def done_button1(event):
                        done_button.configure(bg="#e2fafe",fg="blue")
                    def exitdone_button1(event):
                        done_button.configure(bg='#F0F0FF',fg="black")
                    
                    done_button=Button(entry_frm4,text='   Update   ',font=('Arial',20,'bold'),bd=5,bg="#F0F0FF",command=done)
                    done_button.place(x=280,y=510)
                    #BINDING DONE BUTTON
                    done_button.bind("<Enter>",done_button1)
                    done_button.bind("<Leave>",exitdone_button1)
                    #USER NAME ICON
                    name_image=Label(master=entry_frm4,image=userimagetk,bg='#FFFFEF')
                    name_image.place(x=90,y=123+10)
                    #USER PHONE ICON
                    phone_image=Label(master=entry_frm4,image=phoneimagetk,bg="#FFFFEF")
                    phone_image.place(x=90,y=203+30)    
    
                    #USER EMAIL ICON
                    email_image=Label(master=entry_frm4,image=emailimagetk,bg="#FFFFEF")
                    email_image.place(x=90,y=333)
                    #USER PASSWORD ICON
                    pswrd_image=Label(master=entry_frm4,image=pswrdimagetk,bg="#FFFFEF")
                    pswrd_image.place(x=90,y=433)

                    update_profile1=True
                    
                    def dstry():
                        BG_frm3.destroy()
                        entry_frm4.destroy()
                        entry_frm1.place(x=363,y=22,height=790,width=780)
                     

                    button_image4=Button(master=entry_frm4,image=imgtk5,bd=0,bg='#C1C1CD',command=dstry)
                    button_image4.place(x=1,y=0)
                def txn_hist():
                    
                    try:
                         if(frmwithdraw1==True):
                            BG_frm.destroy()
                            wd_frm.destroy()
                    except:
                        pass
                    
                    
                    try:
                         if(update_profile1==True):
                            BG_frm3.destroy()
                            entry_frm4.destroy()
                    except:
                        pass
                    
                    
                    try:
                        if(frm2==True):
                            BG_frm2.destroy()
                            entry_frm3.destroy()
                    except:
                        pass
                    
                    try:
                        if(frm==True):
                            BG_frm1.destroy()
                            entry_frm2.destroy()
                    except:
                        pass
                    
                    
                    try:
                        if(deposit1==True):
                            BGdp_frm.destroy()
                            dp_frm.destroy()
                    except:
                            pass
    
    
                    global BG_frm5,entry_frm5,txnhis
                    entry_frm1.place_forget()
                    BG_frm5=Frame(log_frm)
                    BG_frm5.configure(bg="brown")
                    BG_frm5.place(x=460,y=150,height=610,width=760)
                    
                    entry_frm5=Frame(log_frm)
                    entry_frm5.configure(bg="#FFFFEF")
                    entry_frm5.place(x=460,y=150,height=600,width=750)
                    txnhis=True
                    
                    
                    
                    #LAST 10 TRANSACTION
                    def done_button2(event):
                        last_trns.configure(fg="blue")
                    def exitdone_button2(event):
                        last_trns.configure(fg="black")
                
                #ONLY CREDIT
                    def done_button3(event):
                        credit_trns.configure(fg="blue")
                    def exitdone_button3(event):
                        credit_trns.configure(fg="black")
                #ONLY DEBIT
                    def done_button4(event):
                        debit_trns.configure(fg="blue")
                    def exitdone_button4(event):
                        debit_trns.configure(fg="black")
                        
                    def trns_debit():
                        
                        tv=Treeview(entry_frm5)
                        tv.place(x=0,y=62,relheight=0.90,relwidth=1)
                        sb=Scrollbar(entry_frm5,orient="vertical",command=tv.yview)
                        sb.place(relx=.968,y=65,relheight=.88,relwidth=0.03)
                    
                    
                        style=Style()
                        style.configure("Treeview.Heading",font=("Arial",10,"bold"),foreground="brown")
                    
                    
                        tv['columns']=("Date","Amount","Updated bal","Time","Type")
                        tv.column("Date",width=100,anchor="c")
                        tv.column("Amount",width=100,anchor="c")
                        tv.column("Updated bal",width=100,anchor="c")
                        tv.column("Time",width=100,anchor="c")
                        tv.column("Type",width=100,anchor="c")
                    
                        tv.heading("Date",text="Date")
                        tv.heading("Amount",text="Amount")
                        tv.heading("Updated bal",text="Updated bal")
                        tv.heading("Time",text="Time")
                        tv.heading("Type",text="Type")
                        tv["show"]='headings'
                    
                        con=sqlite3.connect(database="bank")
                        curobj=con.cursor()
                        curobj.execute("select txn_date,txn_amt,txn_update_bal,txn_type from txn where txn_account_no=? and txn_type=? order by txn_date DESC",(details[0],"Debit"))
                        for row in curobj:
                            s=str(row[0])
                            a=s[0:10]
                            b=s[11:19]
                            tv.insert("","end",values=(a,row[1],row[2],b,row[3]))
                        con.close()
                        
                                            
                        
                    def trns_credit():
                        
                        tv=Treeview(entry_frm5)
                        tv.place(x=0,y=62,relheight=0.90,relwidth=1)
                        sb=Scrollbar(entry_frm5,orient="vertical",command=tv.yview)
                        sb.place(relx=.968,y=65,relheight=.88,relwidth=0.03)
                    
                    
                        style=Style()
                        style.configure("Treeview.Heading",font=("Arial",10,"bold"),foreground="brown")
                    
                    
                        tv['columns']=("Date","Amount","Updated bal","Time","Type")
                        tv.column("Date",width=100,anchor="c")
                        tv.column("Amount",width=100,anchor="c")
                        tv.column("Updated bal",width=100,anchor="c")
                        tv.column("Time",width=100,anchor="c")
                        tv.column("Type",width=100,anchor="c")
                    
                        tv.heading("Date",text="Date")
                        tv.heading("Amount",text="Amount")
                        tv.heading("Updated bal",text="Updated bal")
                        tv.heading("Time",text="Time")
                        tv.heading("Type",text="Type")
                        tv["show"]='headings'
                    
                        con=sqlite3.connect(database="bank")
                        curobj=con.cursor()
                        curobj.execute("select txn_date,txn_amt,txn_update_bal,txn_type from txn where txn_account_no=? and txn_type=? order by txn_date DESC",(details[0],"Credit"))
                        for row in curobj:
                            s=str(row[0])
                            a=s[0:10]
                            b=s[11:19]
                            tv.insert("","end",values=(a,row[1],row[2],b,row[3]))
                        con.close()
                    
                    
                    
                    
                    def trns_10():
                        
                        tv=Treeview(entry_frm5)
                        tv.place(x=0,y=62,relheight=0.90,relwidth=1)
                        sb=Scrollbar(entry_frm5,orient="vertical",command=tv.yview)
                        sb.place(relx=.968,y=65,relheight=.88,relwidth=0.03)
                    
                    
                        style=Style()
                        style.configure("Treeview.Heading",font=("Arial",10,"bold"),foreground="brown")
                    
                    
                        tv['columns']=("Date","Amount","Updated bal","Time","Type")
                        tv.column("Date",width=100,anchor="c")
                        tv.column("Amount",width=100,anchor="c")
                        tv.column("Updated bal",width=100,anchor="c")
                        tv.column("Time",width=100,anchor="c")
                        tv.column("Type",width=100,anchor="c")
                    
                        tv.heading("Date",text="Date")
                        tv.heading("Amount",text="Amount")
                        tv.heading("Updated bal",text="Updated bal")
                        tv.heading("Time",text="Time")
                        tv.heading("Type",text="Type")
                        tv["show"]='headings'
                    
                        con=sqlite3.connect(database="bank")
                        curobj=con.cursor()
                        curobj.execute("select txn_date,txn_amt,txn_update_bal,txn_type from txn where txn_account_no=? order by txn_date DESC limit 10",(details[0],))
                        for row in curobj:
                            s=str(row[0])
                            a=s[0:10]
                            b=s[11:19]
                            tv.insert("","end",values=(a,row[1],row[2],b,row[3]))
                        con.close()
                    
                    #CREATING CREDIT
                    credit_trns=Button(entry_frm5,text='Credit transaction',font=('Arial',15,'bold'),bd=0,relief="sunken",bg="#FFFFEF",command=trns_credit)
                    credit_trns.place(x=300,y=0)
                    #BINDING TRNS 
                    credit_trns.bind("<Enter>",done_button3)
                    credit_trns.bind("<Leave>",exitdone_button3)
                    #CREATING DEBIT
                    debit_trns=Button(entry_frm5,text='Debit transaction',font=('Arial',15,'bold'),bd=0,relief="sunken",bg="#FFFFEF",command=trns_debit)
                    debit_trns.place(x=500,y=0)
                    #BINDING TRNS 
                    debit_trns.bind("<Enter>",done_button4)
                    debit_trns.bind("<Leave>",exitdone_button4)
                    
                    
                    #CREATING TRNS
                    last_trns=Button(entry_frm5,text='Last 10 transaction',font=('Arial',15,'bold'),bd=0,relief="sunken",bg="#FFFFEF",command=trns_10)
                    last_trns.place(x=100,y=0)
                    #BINDING TRNS 
                    last_trns.bind("<Enter>",done_button2)
                    last_trns.bind("<Leave>",exitdone_button2)
                    
                    tv=Treeview(entry_frm5)
                    tv.place(x=0,y=62,relheight=0.90,relwidth=1)
                    sb=Scrollbar(entry_frm5,orient="vertical",command=tv.yview)
                    sb.place(relx=.968,y=65,relheight=.88,relwidth=0.03)
                    
                    
                    
                    
                    
                    style=Style()
                    style.configure("Treeview.Heading",font=("Arial",10,"bold"),foreground="brown")
                    
                    
                    tv['columns']=("Date","Amount","Updated bal","Time","Type")
                    tv.column("Date",width=100,anchor="c")
                    tv.column("Amount",width=100,anchor="c")
                    tv.column("Updated bal",width=100,anchor="c")
                    tv.column("Time",width=100,anchor="c")
                    tv.column("Type",width=100,anchor="c")
                    
                    tv.heading("Date",text="Date")
                    tv.heading("Amount",text="Amount")
                    tv.heading("Updated bal",text="Updated bal")
                    tv.heading("Time",text="Time")
                    tv.heading("Type",text="Type")
                    tv["show"]='headings'
                    
                    con=sqlite3.connect(database="bank")
                    curobj=con.cursor()
                    curobj.execute("select txn_date,txn_amt,txn_update_bal,txn_type from txn where txn_account_no=? order by txn_date DESC",(details[0],))
                    for row in curobj:
                        s=str(row[0])
                        a=s[0:10]
                        b=s[11:19]
                        tv.insert("","end",values=(a,row[1],row[2],b,row[3]))
                    con.close()
                    
                                   
                    #txn_account_no int,txn_amt float,txn_update_bal float,txn_date text,txn_type text,
                    
                    def dstry():
                        BG_frm5.destroy()
                        entry_frm5.destroy()
                        entry_frm1.place(x=363,y=22,height=790,width=780)
                     

                    button_image4=Button(master=entry_frm5,image=imgtk5,bd=0,bg='#C1C1CD',command=dstry)
                    button_image4.place(x=1,y=0)
                    

        

                login_image=Label(master=entry_frm1,image=login_imagetk,bd=0)
                login_image.place(x=0,y=0)
                #WELCOME LABEL
                lbl_welcome=Label(master=entry_frm1,text=f"Welcome {details[1]}",font=("arial",20,"bold"),bd=0,bg="#0678D0",fg="purple")
                lbl_welcome.place(x=0,y=0)
                
                global chkcount
                chkcount=0
                def chk(event):
                    global chkcount
                    chkcount=chkcount+1
                    if(chkcount>1):
                        try:
                            BG_frm1.destroy()
                            entry_frm2.destroy()
                        except:
                            pass
                        

                #CREATING CHECK BALANCE
                check_balance=Button(log_frm,text='Check balance?',font=('Arial',15,'bold'),bd=0,relief="sunken",bg="#87C7D3",command=chk_bal)
                check_balance.place(x=70,y=180)
                #BINDING CHECK BALANCE
                check_balance.bind("<Enter>",done_button2)
                check_balance.bind("<Leave>",exitdone_button2)
                check_balance.bind("<Button-1>",chk)
                
                global wdcount
                wdcount=0
                def wd(event):
                    global wdcount
                    wdcount=wdcount+1
                    if(wdcount>1):
                        try:
                            BG_frm.destroy()
                            wd_frm.destroy()
                        except:
                            pass

                #CREATING WITHDRAW
                withdraw_balance=Button(log_frm,text='Withdraw ',font=('Arial',15,'bold'),bd=0,relief="sunken",bg="#91C5D2",command=withdraw_bal)
                withdraw_balance.place(x=70,y=250)
                #BINDING WITHDRAW
                withdraw_balance.bind("<Enter>",done_button3)
                withdraw_balance.bind("<Leave>",exitdone_button3)
                withdraw_balance.bind("<Button-1>",wd)
                
                global dpcount
                dpcount=0
                def dp(event):
                    global dpcount
                    dpcount=dpcount+1
                    if(dpcount>1):
                        try:
                            BGdp_frm.destroy()
                            dp_frm.destroy()
                        except:
                            pass
                
                #CREATING DEPOSIT
                deposit_balance=Button(log_frm,text='Deposit',font=('Arial',15,'bold'),bd=0,relief="sunken",bg="#91C5D2",command=deposit_bal)
                deposit_balance.place(x=70,y=320)
                #BINDING DEPOSIT
                deposit_balance.bind("<Enter>",done_button4)
                deposit_balance.bind("<Leave>",exitdone_button4)
                deposit_balance.bind("<Button-1>",dp)
                
                global tfcount
                tfcount=0
                def tf(event):
                    global tfcount
                    tfcount=tfcount+1
                    if(tfcount>1):
                        try:
                            BG_frm2.destroy()
                            entry_frm3.destroy()
                        except:
                            pass
                
                #CREATING TRANSFER
                transfer_balance=Button(log_frm,text='Transfer',font=('Arial',15,'bold'),bd=0,relief="sunken",bg="#A9C4D2",command=transfer)
                transfer_balance.place(x=70,y=390)
                #BINDING TRANSFER
                transfer_balance.bind("<Enter>",done_button5)
                transfer_balance.bind("<Leave>",exitdone_button5)
                transfer_balance.bind("<Button-1>",tf)
                
                global upcount
                upcount=0
                def upd(event):
                    global upcount
                    upcount=upcount+1
                    if(upcount>1):
                        try:
                            BG_frm3.destroy()
                            entry_frm4.destroy()
                        except:
                            pass
                
                #CREATING UPDATE
                update_profile=Button(log_frm,text='Update profile',font=('Arial',15,'bold'),bd=0,relief="sunken",bg="#B8C2D3",command=updateprofile)
                update_profile.place(x=70,y=460)
                #BINDING UPDATE
                update_profile.bind("<Enter>",done_button6)
                update_profile.bind("<Leave>",exitdone_button6)
                update_profile.bind("<Button-1>",upd)
                
                global hsycount
                hsycount=0
                def tx_hsy(event):
                    global hsycount
                    hsycount=hsycount+1
                    if(hsycount>1):
                        try:
                            BG_frm5.destroy()
                            entry_frm5.destroy()
                        except:
                            pass
                
                #CREATING txn_history
                txn_his=Button(log_frm,text='History',font=('Arial',15,'bold'),bd=0,relief="sunken",bg="#C6C2D2",command=txn_hist)
                txn_his.place(x=70,y=530)
                #BINDING txn_his
                txn_his.bind("<Enter>",done_button7)
                txn_his.bind("<Leave>",exitdone_button7)
                txn_his.bind("<Button-1>",tx_hsy)
                
                
                
                 #BACK BUTTON DISTROY FUNCTION
                def dstry1():
                    log_frm.destroy()
                    entry_frm1.destroy()
                    login_screen()
        
                logout=Button(master=log_frm,image=logimagetk,bd=0,command=dstry1)
                logout.place(relx=.925,rely=.0)
                logout.bind("<Enter>",enter_button)
                logout.bind("<Leave>",exit_button)
                lbl_image=Label(master=log_frm,image=imgtk,bd=0)
                lbl_image.place(x=0,y=0)








  
login_screen()
win.mainloop()
