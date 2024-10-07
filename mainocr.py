import tkinter
from tkinter import *
from tkinter import filedialog
import os.path
from PIL import Image
import pytesseract
from tkinter import messagebox
def ocr():
    pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    savo=en_save.get()
    lang=en_lang.get()
    file=en_load.get()
    img=Image.open(file)
    txt=pytesseract.image_to_string(img, lang='ara')
    ##txt=pytesseract.image_to_string(img,lang='ar')
    with open(savo,'w') as f:
        f.write(str(txt))
    messagebox.showinfo('rami','\n the file saved')    
def openimg():
    file=filedialog.askopenfile(mode='r',filetypes=[('ping files','*.png')])
    if file:
        filepath=os.path.abspath(file.name)
        en_load.insert(0,filepath)
win=Tk()
win.geometry("650x400")
win.title("ocr")
win.resizable('FALSE','FALSE')
f=Frame(win,width=650,height=300,relief='solid',bg='silver')
f.place(x=1,y=1)
en_load=Entry(f,width=50,font=12)
en_load.place(x=100,y=5)
la_load=Label(f,width=13,height=1,text="مسار الصورة",bg='silver',relief='solid',font=('times for roman',10,'bold'),fg='black')
la_load.place(x=1,y=5)

but_load=Button(f,width=5,height=1,text='+',cursor='hand2',command=openimg)
but_load.place(x=550,y=5)

en_save=Entry(f,width=50,font=12)
en_save.place(x=100,y=70)
la_save=Label(f,width=13,height=1,text="مسار الخرج",bg='silver',relief='solid')
la_save.place(x=1,y=70)


en_lang=Entry(f,width=50,font=12)
en_lang.place(x=100,y=150)
la_lang=Label(f,width=13,height=1,text=" اللغة",bg='silver',relief='solid')
la_lang.place(x=1,y=150)

##img=PhotoImage(file="")
##la_img=Label(win,Image=img)
but_convert=Button(f,width=10,height=10,text="تحويل",command=ocr)
but_convert.place(x=560,y=50)

win.mainloop()