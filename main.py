
# packages #
############
from pyopengltk import OpenGLFrame
from OpenGL import GL
from OpenGL import GLU
from openOBJFile import *
import customtkinter
import configparser
import serial.tools.list_ports
import serial
from pygame.locals import *
import time
from pygame import *

################################################
pygame.init()
ports = serial.tools.list_ports.comports()
serialObj = serial.Serial()


config = configparser.ConfigParser()
config.read('config.ini')
movement = int(config['window']['movement'])


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)



class objViewer(OpenGLFrame):
    rx, ry, rz = (0, 0, 0)
    tx, ty, tz = (0, 0, 0)
    zpos = -80
    x = 0
    y = 0
    z = 0
    # connect
    ser = 0
    s = 0

    def initgl(self): #intional matrix

        glMatrixMode(GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        spl = config['colors']['background_color'].strip().split(',')
        GL.glClearColor(float(spl[0]), float(spl[1]), float(spl[2]), float(spl[3]))
        self.obj = OBJ(config['files']['obj_file'], swapyz=True)
        GLU.gluPerspective(90, (self.width / self.height), 0.1, 120)
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_MODELVIEW)

    def redraw(self): #Draws a frame in a loop
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslate(0, 0, objViewer.zpos) # objViewer.zpos
        glRotate(objViewer.rx, 1, 0, 0)   # objViewer.rx
        glRotate(objViewer.ry, 0, 1, 0)   # objViewer.ry
        glRotate(objViewer.rz, 0, 0, 1)   # objViewer.rz
        GL.glCallList(self.obj.gl_list)

    def up(self, event):
        objViewer.rz += movement


    def down(self, event):
        objViewer.rz -= movement

    def right(self, event):
        objViewer.rx += movement

    def left(self, event):
        objViewer.rx -= movement

    def yAxisPlus(self, event):
        objViewer.ry -= movement

    def yAxisMinus(self, event):
        objViewer.ry += movement

    def zoomIn(event):
        objViewer.zpos += 2 # max(1, objViewer.zpos - 2)

    def getVectorFromArduino(self):
        objViewer.rx = float(entryX.get())
        objViewer.ry = float(entryY.get())
        objViewer.rz = float(entryZ.get())
        self.redraw()


    def serial_ports(self ,event):
            print("stage 2 ")
            port = list(serial.tools.list_ports.comports())
            print (port)
            portshow = []
            for i in range(len(port)):
                portshow.append(port[0][i])
            print(portshow)
            return portshow

    def getEntry(self , x , y , z ):

        # objViewer.rx = int(entryX.get())
        # objViewer.ry = int(entryY.get())
        # objViewer.rz = int(entryZ.get())
        print ("update location  {} {} {}".format(x , y ,z  ))
        x = int(float(x))
        y = int(float(z))
        z = int(float(y))
        x = (x % 360)
        y = (y % 360)
        z = (z % 360)
        if (-20 < x < 50):
            title_lbl1.configure(text="""התקופה אייל ראש
            שנה אלפים כששת כלקוליתית
            הגושרים אתר - זמננו לפני
            באבן מפוסל מקרין חיים בעל של ראש.
            חיים בעלי המתארות צלמיות,
            נפוצות מקרינים חיים בעלי ובעיקר
            חשיבותם על ומעידות הכלקוליתית בתקופה
            אלה חיים בעלי
            הקדומים הפסלים של בתרבותם
            של. מקנה של רעיה על
            ברובה התבססה בתקופה הכלכלה
            - החשיבות ומכאן - פרות עיזים וכבשים.
            מפותלות קרניים בעל אייל מתאר הפסל
             - מבוית חיים בעל
             הזכר את דווקא בצלמית לתאר
             והסימבולי הטקסי בעולמם מקומו על מעידה
             התקופה בני של.""", )
        # if (-20 < x < 50):
        #     title_lbl1.configure(text="""ראש אייל (כבש זכר) התקופה הכלקוליתית כששת אלפים שנה
        #     לפני זמננו - אתר הגושרים.
        #     ראש של בעל חיים מקרין מפוסל באבן.
        #     צלמיות המתארות בעלי חיים, ובעיקר בעלי חיים מקרינים נפוצות
        #     בתקופה הכלקוליתית ומעידות על חשיבותם
        #     של בעלי חיים אלה בתרבותם של הפסלים הקדומים.
        #     הכלכלה בתקופה התבססה ברובה על רעיה של מקנה
        #     - כבשים עיזים ופרות - ומכאן החשיבות.
        #     הפסל מתאר אייל בעל קרניים מפותלות -
        #     בעל חיים מבוית. הבחירה לתאר בצלמית דווקא את הזכר
        #     מעידה על מקומו בעולמם הטקסי והסימבולי
        #     של בני התקופה.""", )
        else:
            title_lbl1.configure(text="""מעולה בעיבור אבן עשויה הצלמית
            המתקדמות יכולותיהם על מעידות
            והגימור הביצוע רמת
            בעבודה הכלקוליתית התקופה אנשי של
            אבן גיר - לעיבור פשוט לא חומר עם
            כל של המעולה לעיבוד לב לשים יש
            ולמטה למעלה. ואחור חזית - הצלמית חלקי
            בעזרת קשה באבן בעיבוד זאת כל
            ביד המוחזקים כלים
            מתכת כלי עדיין אין בה ובתקופה
            מתאימה שאינה רכבה נחושת למעט
            גיר באבן לעבודה.""", )
        # else:
        #     title_lbl1.configure(text="")

        objViewer.rx = int(float(x))
        objViewer.ry = int(float(y))
        objViewer.rz = int(float(z))
        self.redraw()

    def ReadSerial(self ):
            print (self.s)
            print("Read :")
            b = []
            s = ""
            x = 0
            y = 0
            z = 0

            ser = serial.Serial(self.s, 9600)
            print("try Read :")
            try :
                print("11111:")
                #if (ser.in_waiting()>0) :
                b = ser.readline()
                print("try Close  :")
                ser.close()
                print(type(b))
                s = b.decode("utf-8")
                print(type(s))
                print(s)
                s = s.split(";")
                print(s)
                x = s[1]
                y = s[2]
                z = s[3]

                print("Position {} {} {} ".format(x, y, z))
                self.getEntry(y, z, x)
                app.after(30, self.ReadSerial)
            except :
                self.getEntry(0, 0, 0)
                ser.close()
                app.after(30, self.ReadSerial)


    def updtcblist(self, event):
        print("stage 1 ")
        l = []
        port = list(serial.tools.list_ports.comports())
        for port, desc, hwid in sorted(ports):
            l.append(port)
        TCombobox1.configure(values=(l))

        self.s = TCombobox1.get()
        print(self.s)
        if "COM" in self.s:
            print ("****************")
            print("****************")
            self.ReadSerial()

    def zoomOut(self):
        objViewer.zpos -= 2 #  max(1, objViewer.zpos + 2)



def serial_ports():
    return serial.tools.list_ports.comports()

#customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
#customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
app = customtkinter.CTk()  # create CTk window like you do with the Tk window.
app.title(config['window']['title'])  # App title
app.iconbitmap("icon.ico")  # App icon
app.geometry(config['window']['size'])
outer_frame = customtkinter.CTkFrame(master=app, width=1800, height=800)  # App frame
outer_frame.columnconfigure(1)
button_frame = customtkinter.CTkFrame(master=outer_frame, width=10 )  # Side frame for buttons.
title_lbl = customtkinter.CTkLabel(button_frame, text=config['window']['title'])
title_lbl.grid(row=0, pady=20)
button_frame.rowconfigure(10)
button_frame.grid(column=0, row=0, sticky='ns')
frm = objViewer(outer_frame, height=800, width=1200)

'''-----Buttons for moving the object-----'''
app.bind("<Up>", frm.up)
app.bind("<Down>", frm.down)
app.bind("<Right>", frm.right)
app.bind("<Left>", frm.left)
app.bind("<w>", frm.yAxisPlus)
app.bind("<s>", frm.yAxisMinus)
zoom_in_btn = customtkinter.CTkButton(master=button_frame, text='Zoom In', command=frm.zoomIn)
zoom_in_btn.grid(row=1)
zoom_out_btn = customtkinter.CTkButton(master=button_frame, text='Zoom Out', command=frm.zoomOut)
zoom_out_btn.grid(row=2, pady=20)
vcmd = app.register(lambda p:  str.isnumeric(p) or '.' in p or p and p[0] == '-' or '\b' in p or p == '')

##vectorLbl = customtkinter.CTkLabel(button_frame, text="Vector:")
##vectorLbl.grid(pady=10, padx=150)

#####
number = ["chose com port "]
TCombobox1 = customtkinter.CTkComboBox(master=button_frame)
TCombobox1.grid(padx = 80 , pady=80 , row=6 )           # (relx=0.46, rely=0.08, relheight=0.14, relwidth=0.48)
TCombobox1.configure(values=number)  # robotgui_support.Serialcombobox)
# self.TCombobox1.configure(takefocus="")
# self.TCombobox1.configure(invalidcommand="invcmd")
#TCombobox1.configure(show="show")
READONLY = 'readonly'
TCombobox1.configure(state=READONLY)
#TCombobox1.configure(values=serial_ports())
TCombobox1.configure(command=frm.updtcblist)  # check why


'''-----Vector-----'''
# entryX = customtkinter.CTkEntry(button_frame, placeholder_text='0.0', validate='all', validatecommand=(vcmd, '%P'))
# entryX.insert(0, "0")
# entryX.grid(pady=10, padx=15)
# entryY = customtkinter.CTkEntry(button_frame, placeholder_text='0.0', validate='all', validatecommand=(vcmd, '%P'))
# entryY.insert(0, "0")
# entryY.grid(pady=10, padx=15)
# entryZ = customtkinter.CTkEntry(button_frame, placeholder_text='0.0', validate='all', validatecommand=(vcmd, '%P'))
# entryZ.insert(0, "0")
# entryZ.grid(pady=10, padx=15)
# button = customtkinter.CTkButton(button_frame, text='Move Vector', command=frm.getEntry)
# button.grid(pady=30, padx=15)
title_lbl1 = customtkinter.CTkLabel(button_frame , text= "")
title_lbl1.grid(pady=0 ,padx = 0)
outer_frame.grid()
frm.grid(ipadx=250, ipady=100, column=8, row=0, sticky='w')
frm.animate = 10





portList=[]
print(ports)
for onePort in ports:
    portList.append(onePort)
print(portList)
#combobox = customtkinter.CTkOptionMenu(master=button_frame, values=portList, command=optionmenu_callback)
#combobox.grid(padx=20, pady=10)
app.resizable(True , True ) # size limitation


top = customtkinter.CTkToplevel(app)
top.geometry("250x250")
top.title("")
customtkinter.CTkLabel(top, text="Hello World!")
top.withdraw()

app.mainloop()


