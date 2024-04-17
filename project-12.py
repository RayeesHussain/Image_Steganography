#GUI
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os
from tkinter import PhotoImage
import cv2
import os 
import string
from stegano import lsb
from tkinter import messagebox

root=Tk()
root.title("steganography")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg="#1aa260")

def showImage():
    text1.delete(1.0,END)
    text2.delete(1.0,END)
    global filename,img1
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select image file',
                                        filetype=(("PNG file","*.png"),
                                                  ("JPEG file","*.jpeg"),
                                                  ("All file","*.txt")))
    img=Image.open(filename)
    
    img.thumbnail((250, 250))
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img
    img1=cv2.imread(filename)

def Hide():
    
    global password,message,img1,d,c
    img1=cv2.imread(filename)
    # base_filename=os.path.basename(filename)
    # print(base_filename)
    message=text1.get(1.0,END).strip()
    print(message)
    password=text2.get(1.0,END).strip()
    print(password)
  
    if not message or not password:
        root = Tk()  # Create a temporary root window
        root.withdraw()  # Hide the temporary root window
        messagebox.showerror("Error", "Enter a message to encode.")
        return
    else:
        print("combined")
        message=message+'\n'+password+'\n'
        print(message)
    
        d={}
        c={}
        for i in range(0,255):
            d[chr(i)]=i
            c[i]=chr(i)
        m=0
        n=0
        z=0
        for i in range(len(message)):
            img1[n,m,z]=d[message[i]]
            n=n+1
            m=m+1
            z=(z+1)%3
        final_filepath=filedialog.asksaveasfilename(initialdir=os.getcwd(),
                                        title='save image',
                                        filetype=(("PNG file","*.png"),
                                                  ("JPEG file","*.jpeg"),
                                                  ("All file","*.txt")))
        cv2.imwrite(final_filepath,img1)
    
    text1.delete(1.0,END)
    text2.delete(1.0,END)


def Show():
    
    d={}
    c={}
    for i in range(0,255):
        d[chr(i)]=i
        c[i]=chr(i)
    message2=""
    n=0
    m=0
    z=0
    for i in range(len(img1)):
        message2=message2+c[img1[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1)%3
    print("in image")
    print(message2)
    lines=message2.split('\n')
    lines=[i for i in lines if i!='']
    pass12=lines[1]

    print("password-" + pass12)
    
    message1=""
    n=0
    m=0
    z=0
    
    pass1=text2.get(1.0,END)
    passl=pass1.split('\n')  
    
    print("entered password-"+passl[0])
    print("done")  
    if pass12==passl[0]:
        # for i in range(len(img1)):
        #     message1=message1+c[img1[n,m,z]]
        #     n=n+1
        #     m=m+1
        #     z=(z+1)%3
        # print(message1)
        # lines=message1.split('\n')
        text1.delete(1.0,END)
        text1.insert(1.0,lines[0])
    else:
        messagebox.showerror("password not valid")


def save():
    final_filepath=filedialog.asksaveasfilename(initialdir=os.getcwd(),
                                        title='save image',
                                        filetype=(("PNG file","*.png"),
                                                  ("JPEG file","*.jpeg"),
                                                  ("All file","*.txt")))
    cv2.imwrite(final_filepath,img1)
    
    print("")
    
image_icon=PhotoImage(file="log.png")
root.iconphoto(False,image_icon)

logo=PhotoImage(file="logo1.png")
Label(root,image=logo).place(x=20,y=5)
Label(root,text="Project-Image Stegnography",bg="#1aa260",fg="white",font="arial 25 bold").place(x=200,y=20)

f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

frame2=Frame(root,bd=3,bg="white",width=340,height=280,relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=330,height=270)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=315,y=0,height=275)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

Label(root,text="Enter key",bg="#1aa260",fg="white",font="arial 20 bold").place(x=100,y=365)

text2=Text(root,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text2.place(x=360,y=365,width=300,height=30)

frame3=Frame(root,bd=3,bg="#1aa260",width=340,height=95,relief=GROOVE)
frame3.place(x=10,y=400)

Button(frame3,text="open image",width=10,height=1,font="arial 14 bold",command=showImage).place(x=20,y=30)
Button(frame3,text="save image",width=10,height=1,font="arial 14 bold",command=save).place(x=180,y=30)
Label(frame3,text="piture,image,photo file",bg="#1aa260",fg="yellow").place(x=20,y=5)


frame4=Frame(root,bd=3,bg="#1aa260",width=340,height=95,relief=GROOVE)
frame4.place(x=350,y=400)

Button(frame4,text="hide data",width=10,height=1,font="arial 14 bold",command=Hide).place(x=20,y=30)
Button(frame4,text="show data",width=10,height=1,font="arial 14 bold",command=Show).place(x=180,y=30)
Label(frame4,text="piture,image,photo file",bg="#1aa260",fg="yellow").place(x=20,y=5)

root.mainloop()