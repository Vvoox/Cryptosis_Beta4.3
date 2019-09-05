from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from tkinter import scrolledtext
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import tkinter
import tkinter.filedialog
import base64
from tkinter.ttk import *
import webbrowser
from subprocess import call


root=Tk()
root.title("Cryptosis")
root.iconbitmap('icon.ico')



height = root.winfo_screenheight()
width = root.winfo_screenwidth()
print(height)
print(width)
canvas1 = Canvas(root, width=width, height=height-100)
print("\n width x height = %d x %d (in pixels)\n" %(width, height))
height1=canvas1.winfo_screenheight()
width1=canvas1.winfo_screenwidth()

print(height1)
print(width1)
 #The (250, 250) is (height, width)
 # convert to PhotoImage
# image.pack() # canvas objects do not use pack() or grid()

img = PhotoImage(file="cry.ppm")
  # PIL solution
canvas1.create_image(width/4,40, anchor=NW, image=img)

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)

#root.overrideredirect(True)
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#root.focus_set()  # <-- move focus to this widget
#root.bind("<Escape>", lambda e: e.widget.quit())
#scrollbar = Scrollbar(root)
#scrollbar.pack( side = RIGHT, fill = Y )
#mylist = Listbox(root, yscrollcommand = scrollbar.set )
#for line in range(100):
 #  mylist.insert(END, 'This is line number' + str(line))
#mylist.pack( side = LEFT, fill = BOTH )
#scrollbar.config( command = mylist.yview )
#input="Insert your text here...or browse your file"
output="Outputs"


#root.title("Cryptosis")


#text.tag_add("Write Here", "1.0", "1.4")
#text.tag_add("Click Here", "1.8", "1.13")

#text.tag_config("Write Here", background="yellow", foreground="black")
#text.tag_config("Click Here", background="black", foreground="white")

text = Text(root, height=height/95, width=60)
#text.tag_config("Write Here")
input1="Insert your text here...or browse your file"
text.insert(INSERT,input1)
canvas1.create_window(width/2.6, height-600, window=text)

def Contact():

    contact = Tk()
    contact.title("Contact")
    height_root = canvas1.winfo_screenheight()
    width_root = canvas1.winfo_screenwidth()
    Contact_canvas = Canvas(contact, width=width_root/2, height=height_root/2)
    ourMessage = 'Welcome in our software Cryptosis , i wish that its useful for you'
    ourMessage1 = 'if there any quations , please contact us in : www.Crisis.com'

    whatever_you_do = "Welcome in our software Cryptosis , hopely is useful for you ," \
                      "if there's any question , please contact us in "
    new = 1
    url = "https://www.crisi5.com"

    def openweb() :
        webbrowser.open(url, new=new)

    #Btn = Button(contact, text="This opens Google", command=openweb)
    #contact.iconbitmap('./Img/fb.png')
    #x_image = './Img/fb.png'
    #x_image_for_button = PhotoImage(file=x_image)
    #Btn = Button(contact, image='icon.ico', command=openweb)
    b = Button(contact, text="Click Here",command=openweb)
    #b.config(width="40", height="40")
    b.place(x=5, y=5)

    msg = Message(contact, text=whatever_you_do)
    msg.config(bg='white', font=('times', 16, 'bold'))
    msg.pack()
    b.pack()
    #contact.pack()
    #messageVar = Text(contact )
    #Contact_canvas = Text(Contact)
    #contact.config(bg='lightgreen')


def About_us():

    messagebox.showinfo("Info", "  Information systems are now an integral part of the functioning of public administrations, business activity and the way of life of citizens. From now on, they have become indispensable and unavoidable"+
"Securing and controlling the information conveyed by information systems is becoming more and more of an issue as the size of environments that are strongly linked to the information domain is expanding. Today, cyberattacks may have the purpose of stealing data, damaging or altering the normal operation of the IS. These have negative consequences for organizations or individuals who are victims."+
"In the face of these risks and threats and as in the advanced countries in the field of information systems security, and following the national strategy of cyber security founded by the DGSSI which aims to to provide our information systems with a defense and resilience capability, capable of creating the conditions for an environment of trust and security conducive to the development of the information society, CRSIS has begun a movement that will change the citizens perspective towards the IT field and will emphasize the importance of good personal data protection practices against all forms of attacks as well as train competent people able to meet the demands of the current market ")
    b = Button(canvas1, text="Info", image=r'.\Img\fb.png', compound=CENTER)

def Options():

    MsgBox = messagebox.showinfo('Notification', 'SOON...',icon='info')



#--------------------------------------------------------------------------------------------------
def ExitApplication():
    MsgBox = messagebox.askquestion('Notification', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


FILETYPES = [("text files", "*")]

filename = StringVar(root)

entry = Entry(root, textvariable=filename)


def set_filename():
    file = tkinter.filedialog.askopenfilename(
        parent=root, initialdir='*',
        title='Choose file',
        filetypes=[('Text file', '.txt')]
    )
    with open(file) as f:
        with open("input.txt", "w") as f1:
            for line in f:
                f1.write(line)
                #input.write(line)
            text.delete('1.0', END)
            input=line
            text.insert(INSERT, input)


"""def Copy():

    def __init__(self, master, **kw) :
        output.__init__(self, master, **kw)
        self.bind('<Control-c>', self.copy)
        self.bind('<Control-x>', self.cut)
        self.bind('<Control-v>', self.paste)

    def copy(self, event=None) :
        self.clipboard_clear()
        cp_text = self.get("sel.first", "sel.last")
        self.clipboard_append(cp_text)
        print(cp_text)"""
def Copy():
    MsgBox = messagebox.showinfo('Notification', 'SOON...',icon='info')
def Share():
    MsgBox = messagebox.showinfo('Notification', 'SOON...',icon='info')


CODE=['A','.-', 'B','-...',
   'C','-.-.','D','-..',
   'F' , '..-.', 'G' , '--.', 'H','....',
   'I' ,'..', 'J','.---', 'K','-.-',
   'L' ,'.-..', 'M','--', 'N','-.',
   'O' ,'---', 'P' , '.--.', 'Q','--.-',
   'R','.-.' , 'S' ,'...', 'T','-',
   'U' ,'..-' , 'V','...-', 'W','.--',
   'X' ,'-..-' , 'Y','-.--', 'Z','--..',
   '1' ,'.----' , '2','..---', '3','...--',
   '4' ,'....-' , '5','.....', '6','-....',
   '7' ,'--...' , '8','---..', '9','----.',
   '0' ,'-----' , ', ' , '--..--' ,
   '?' , '..--..' ,
   '(' , '-.--.' ,  ')' , '-.--.-' ]
CODE1=[ 'E' ,'.' ]
CODE2=['-', '-....-']
CODE3=[' ','/']
CODE4=['.' , '.-.-.-' ]
CODE5=['/' , '-..-.']

def Crypt():

    #ASCII-----------------------------------------------------------------------------------------

    input1 = text.get("1.0", END)
    list=[]
    for i in input1 :
        list+=i
    output = "ASCII = " + ''.join(" "+ str(ord(c)) for c in input1) + "\n"+ "\n"

    #Base64----------------------------------------------------------------------------------------

    encodedBytes = base64.b64encode(input1.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    output +="Base64 = " + encodedStr +"\n"+ "\n"

    #HEX-------------------------------------------------------------------------------------------
    output += "HEX = ...SOON" +"\n"+ "\n"



    #Cesar-----------------------------------------------------------------------------------------

    input1 = text.get("1.0", END)
    Alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Alphabet2 = "abcdefghijklmnopqrstuvwxyz"
    numbers="1234567890/~!#$%^&*(()_+}{?><|\-.,][="

    #key = int(input("Enter your key : "))
    """MsgBox = messagebox.askquestion('Notification', 'Do you have the key for CESAR encryption?',
                                       icon='info')
     IMPORTANT if MsgBox == 'yes':
        return call(["python", "Thekey.py"])



    else:
        messagebox.showinfo('Return', 'The program will continue without teh key')"""
    key=3
    n=len(input1)
    m=len(Alphabet1)
    l=len(numbers)
    output_cesar=""
    for i in range(n):

        if input1[i]==" ":
            output_cesar+=" "

        if input1[i]=="\n":
            output_cesar+=" "

        for j in range(m):

            if input1[i]==Alphabet1[j]:

                if j+key<=25 :
                    output_cesar += Alphabet1[j+key]
                else :
                    X=25-j
                    Y=key-X
                    output_cesar += Alphabet1[Y-1]


            if input1[i]==Alphabet2[j]:

                if j + key <= 25 :

                    output_cesar += Alphabet1[j + key-1]
                else :
                    X = 25 - j
                    Y = key - X -1
                    output_cesar += Alphabet1[Y-1]

            if input1[i]==numbers[j]:
                output_cesar+=numbers[j]


    output += "CESAR = " + output_cesar + "\n"+ "\n"

    #Morse_code-------------------------------------------------------------------------------------------------

    output_morse = ""
    input1 = text.get("1.0", END)
    n=len(input1)
    m=len(CODE)
    i=0
    #while(i<n):
            ##i+=1
    for i in range(n):
        if input1[i]=='E':
            output_morse+=CODE1[1]+" "
        if input1[i]=='-':
            output_morse += CODE2[1]+" "
        if input1[i]==' ':
            output_morse+= CODE3[1]+" "
        if input1[i]=='.':
            output_morse+=CODE4[1]+" "
        if input1[i]=='/':
            output_morse+=CODE5[1]+" "
        else :
            for j in range(m) :
                input1 = input1.upper()
                if input1[i] == CODE[j] :
                    output_morse += CODE[j + 1]+" "




  # output += output_morse

    output += "MORSE =" + output_morse + "\n"+ "\n"




    #Binary----------------------------------------------------------------------------------------

    input1 = text.get("1.0", END)
    output_binary = ' '.join(format(ord(x), 'b') for x in input1)
    print(output_binary.split())
    forme1=output_binary.split()
    forme2=""
    for i in forme1:
        if len(i)==7:
            i="0"+i
        if len(i)==6:
            i="00"+i
        if len(i)==5:
            i="000"+i
        if len(i)==4:
            i="0000"+i

        forme2+=i+" "
    output+= "Binary = "+forme2






    #-----------------------------------------------------------------------------------------------
    with open("output.txt", "w") as f1:
        for line in output:
            f1.write(line)
    text1.delete('1.0', END)
    text1.insert(INSERT,output)
    print("File registered")
    #messagebox.showinfo("Info", "Your outputs is saved in output.txt , you'll find it in your Cryptosis file.")




def Decrypt() :
    try :

        decodedMessage = ""
        input = text.get("1.0", END)

        for item in input.split() :
            decodedMessage += chr(int(item))
            output = "ASCII to Plaintext =  " + decodedMessage + "\n"
            print(decodedMessage)
            text1.delete('1.0', END)
            text1.insert(INSERT, output)
    except:
         return Base64()

            # Base64-------------------------------------------------------------------------------------
def Base64():

    try:
        input = text.get("1.0", END)
        encodedBytes = base64.b64decode(input)
        decodedStr = str(encodedBytes, "utf-8")
        output = "Base64 to Plaintext =  " + decodedStr
        text1.delete('1.0', END)
        text1.insert(INSERT, output)
        with open("output.txt", "w") as f1 :
            for line in output :
                f1.write(line)

    except:
        return Cesar()

def Cesar():
    input1 = text.get("1.0", END)
    Alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Alphabet2 = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890/~!#$%^&*(()_+}{?><|\-.,][="

    # key = int(input("Enter your key : "))
    key = 3

    n = len(input1)
    m = len(Alphabet1)
    l = len(numbers)
    output_cesar = ""

    for i in range(n) :

        if input1[i] == " " :
            output_cesar += " "

        if input1[i] == "\n" :
            output_cesar += " "

        for j in range(m) :

            if input1[i] == Alphabet1[j] :

                if j + key >= 0 :
                    output_cesar += Alphabet1[j - key]
                else :
                    X = 25 - j
                    Y = key - X
                    output_cesar += Alphabet1[Y - 1]

            if input1[i] == Alphabet2[j] :
                if j + key >= 0 :
                    output_cesar += Alphabet1[j - key - 1]
                else :
                    X = 25 - j
                    Y = key - X - 1
                    output_cesar += Alphabet1[Y - 1]

            if input1[i] == numbers[j] :
                output_cesar += numbers[j]
    text1.delete('1.0', END)
    output = "Cesar to Plaintext =  " + output_cesar +"\n"
    text1.insert(INSERT, output)
    with open("output.txt", "w") as f1 :
        for line in output :
            f1.write(line)

    output_morse = ""
    input1 = text.get("1.0", END)
    n = len(input1)
    m = len(CODE)
    i = 0
    # while(i<n):
    ##i+=1
    print(input1)
    x = input1.split()
    xx = len(x)
    print(x)
    for i in range(xx) :
        if x[i] == '.' :
            output_morse += CODE1[0]
        if x[i] == '-....-' :
            output_morse += CODE2[0]
        if x[i] == '/' :
            output_morse += CODE3[0]
        if x[i] == '.-.-.-' :
            output_morse += CODE4[0]
        if x[i] == '-..-.' :
            output_morse += CODE5[0]
        else :
            for j in range(m) :
                if x[i] == CODE[j] :
                    output_morse += CODE[j - 1]

    output = "Morse to Plaintext =  " + output_morse
    text1.insert(INSERT, output)
    with open("output.txt", "w") as f1 :
        for line in output :
            f1.write(line)






#Menu----------------------------------------------------------------------------------------------

menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=None)
file.add_command(label='Open...', command=set_filename)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit', command=ExitApplication)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Cut', command=Copy)
edit.add_command(label='Copy', command=Copy)
edit.add_command(label='Paste', command=Copy)
edit.add_command(label='Select All', command=Copy)
edit.add_separator()
edit.add_command(label='Find...', command=None)
edit.add_command(label='Find again', command=None)

# Adding Help Menu
help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Help', command=Options)
help_.add_command(label='Contact us', command=Contact)
help_.add_separator()
help_.add_command(label='About us', command=About_us)

# display Menu
root.config(menu=menubar)


#------------------------------------------------------------------------------------------------------
text1= Text(root, height=1, width=5)
text1.insert(INSERT, "INPUT")
canvas1.create_window(width/4.5, 400, window=text1)



text1= Text(root, height=1, width=6)
text1.insert(INSERT, "OUTPUT")
canvas1.create_window(width/4.5, 600, window=text1)

text1 = Text(root, height=height/95, width=60)
text1.insert(INSERT, output)
canvas1.create_window(width/2.6, height-400, window=text1)


#Buttons------------------------------------------------------------------------------------------------

button2 = Button(root, text='   Browse  ', command=set_filename )
canvas1.create_window(width/1.6, height/2.55, window=button2)


button3 = Button(root, text='  Crypt  ', command=Crypt)
canvas1.create_window(width/1.6, height/2.35, window=button3)

button4 = Button(root, text='  Decrypt  ', command=Decrypt )
canvas1.create_window(width/1.6, height/2.15, window=button4)

button1 = Button(root, text='  EXIT  ', command=ExitApplication )
canvas1.create_window(width/1.6, height/2, window=button1)

button1 = Button(root, text='  Copy  ', command=Copy)
canvas1.create_window(width/1.6, height/1.7, window=button1)

button1 = Button(root, text='  Share  ', command=Share )
canvas1.create_window(width/1.6, height/1.55, window=button1)

#button3 = Button(root, text='  Modify IDs  ', command=openexcel )
#canvas1.create_window(500, 900, window=button3)

w = Label(root, text='Crisis.com | ©2020')




saveinfo = Label(root,
                 text=" Your Outputs and Inputs will be saved in text files , you'll find it in your Cryptosis file.")


#text2 = Text(root,height=10, width=90)
#s = Scrollbar(root)
#ext2.focus_set()
##s.pack(side=RIGHT, fill=text2.winfo_height)

#s.config(command=text2.winfo_height)
##text2.insert(INSERT, output)



#canvas1.create_window(400, 700, window=text2)
#canvas1.create_window(750, 700, window=s)


#s = Scrollbar(root)
#T = Text(root)

#T.focus_set()
#s.pack(side=RIGHT, fill=Y)
#T.pack(side=LEFT, fill=Y)
#s.config(command=T.yview)
#T.config(yscrollcommand=s.set)

#for i in range(40):
 #  T.insert(END, "This is line %d\n" % i)
#scrollbar.config( command = mylist.yview )
canvas1.pack()
saveinfo.pack()
w.pack()

root.mainloop()

