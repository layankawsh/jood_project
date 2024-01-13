from tkinter import *
obj = Tk()

def addBtnCliick():
    myfile = open("USER&PASS.txt", "r")
    alldata = myfile.readlines()
    username = txtname.get()
    password = txtcode.get()
    f=0
    for x in alldata:
        linedata = x.split(",")
        print(linedata[1])
        print(linedata[0])
        if username == linedata[0] and password == linedata[1]:
            f = 1
            break
        else:
            f=2
    if f==1 or f==2:
     lblResult.config(text="welcome , member")
     obj = Tk()
     obj.configure(background="#deb2ee")
     main = Label(obj, text=" LADEIS GYM  ", fg="#deb2ee", font=("Century Gothic", 60))
     lbl2 = Button(obj, text="      Offers       ", font=("Century Gothic", 30), fg="#deb2ee", background="#f0dcf7",
                  command=second2)
     lbl3 = Button(obj, text="  for Inquiries  ", font=("Century Gothic", 30), fg="#deb2ee", background="#f0dcf7",
                  command=qu)
     lbl4 = Button(obj, text="     location     ", font=("Century Gothic", 30), fg="#deb2ee", background="#f0dcf7",
                  command=location)
     lblj = Button(obj, text="close", font=("Century Gothic", 30), fg="#f2f3f4", background="#915c83",
                  command=btnClick11)
     main.pack(pady=10)
     # lbl1.pack(pady=10)
     lbl2.pack(pady=10)
     lbl3.pack(pady=10)
     lbl4.pack(pady=10)
     lblj.pack(pady=10)





#
def qu():
             obj220 = Tk()
             obj220.configure(background="#deb2ee")
             main = Label(obj220, text=" LADEIS GYM  ", fg="#deb2ee", font=("Century Gothic", 60))
             lbl01 = Button(obj220, text=" call : 0798746450 ", font=("Century Gothic", 50), fg="#deb2ee", background="#f0dcf7")
             lbl02= Button(obj220, text=" instagram message : LADEIS_GYM  ", font=("Century Gothic", 50), fg="#deb2ee",background="#f0dcf7")

             main.pack(pady=10)
             lbl01.pack(pady=10)
             lbl02.pack(pady=10)
def location():
             objj = Tk()
             objj.configure(background="#deb2ee")
             main = Label(objj, text=" LADEIS GYM  ", fg="#deb2ee", font=("Century Gothic", 60))
             lbl86 = Button(objj, text=" Amman , airport st  ", font=("Century Gothic", 50), fg="#deb2ee", background="#f0dcf7")

             main.pack(pady=10)
             lbl86.pack(pady=10)
def second2():
             obj222 = Tk()
             obj222.configure(background="#deb2ee")
             main = Label(obj222, text=" LADEIS GYM  ", fg="#deb2ee", font=("Century Gothic", 60))
             lbl111 = Button(obj222, text=" 1 monthe + 2 weeks =30 JD ", font=("Century Gothic", 50), fg="#deb2ee", background="#f0dcf7",command=btnClick8)
             lbl22= Button(obj222, text=" 4 monthes + 2 weeks =50 JD ", font=("Century Gothic", 50), fg="#deb2ee",background="#f0dcf7",command=btnClick9)
             lbl33= Button(obj222, text="  1 monthe  Boxing + cardio =40 JD" , font=("Century Gothic", 50), fg="#deb2ee",
                           background="#f0dcf7",command=btnClick10)
             main.pack(pady=10)
             lbl111.pack(pady=10)
             lbl22.pack(pady=10)
             lbl33.pack(pady=10)

obj.configure(background="#deb2ee")
main= Label(obj, text=" LADEIS GYM  ", fg="#deb2ee", font=("Century Gothic", 60))
lblname = Label(obj, text="Enter member name",font=("century gothic",30), fg="#deb2ee", background="#f0dcf7")
lblcode = Label(obj, text="Enter your code ",font=("century gothic",30), fg="#deb2ee", background="#f0dcf7")
lblResult = Label(obj, text="..........")
txtname = Entry(obj)
txtcode = Entry(obj,show="*")
btnAdd = Button(obj, text="Add",command=addBtnCliick,font=("century gothic",15),fg="#deb2ee", background="#f0dcf7")
main.pack(pady=10)
lblname.pack(pady=10)
txtname.pack(pady=10)
lblcode.pack(pady=10)
txtcode.pack(pady=10)
btnAdd.pack(pady=10)
lblResult.pack(pady=10)
# *********************************
def btnClick8():
    myfile = open("total.txt", "a")
    myfile.writelines("(1monthe + 2weeks),30,end\n")
def btnClick9():
    myfile = open("total.txt", "a")
    myfile.writelines("(4 monthes + 2 weeks),50,end\n")
def btnClick10():
    myfile = open("total.txt", "a")
    myfile.writelines("( 1 monthe  Boxing + cardio) ,40,end\n")
def btnClick11():
    cl=Tk()
    myfile=open("total.txt","r")
    alldata=myfile.readlines()
    total=0
    for x in alldata:
      data=x.split(",")
      total=total+float(data[1])
      t=(" your total :",total)
      l5 = Label(cl, text=t)
      l5.pack()
myfile = open("total.txt", "w")
myfile.writelines(" ")
obj.mainloop()
