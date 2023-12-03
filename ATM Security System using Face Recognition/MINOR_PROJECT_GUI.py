from tensorflow.keras.models import load_model
from tkinter import *
from tkinter.ttk import *
import time
import cv2
import camera
import os
#from message_box import message_Box as mesg
from PIL import Image, ImageTk
import warnings
warnings.filterwarnings("ignore")
warnings.filterwarnings("error")


master = Tk()
master.geometry("1920x1080")
master.title("ATM SECURITY ENHANCEMENT USING COMPUTER VISION")
#master.configure(bg="#121212")
image = Image.open(r"D:\Chinmay Jain\Subject\ATM Minor project\2818505.jpg")
bg = ImageTk.PhotoImage(image)
Label(master, image=bg).place(relwidth=1, relheight=1)

################################### functions to be created ########################################
class gui_maker():
    
    prototxtPath=None
    weightsPath=None
    faceNet=None
    cover_model=None
    filename=None
    entry_time=None

    def __init__(self):
        self.prototxtPath = r"D:\Chinmay Jain\Subject\ATM Minor project\deploy.prototxt"
        self.weightsPath = r"D:\Chinmay Jain\Subject\ATM Minor project\res10_300x300_ssd_iter_140000.caffemodel"
        self.faceNet = cv2.dnn.readNet(self.prototxtPath, self.weightsPath)
        
        self.cover_model = load_model(r"D:\Chinmay Jain\Subject\ATM Minor project/mask_detector.model") 
    
    def cash_wd():
        return


    def Balance():
        return

    def camera_face_detect(self):

        fd = camera.faceDetection()
        f = fd.start(self.faceNet, self.cover_model, master)
        if f == True:
            self.pin_win()

    def main_menu(self):
        main = Toplevel(master)
        main.geometry("1920x1080")
        
        Button(main, text="Cash withdraw").pack()
        Button(main, text="Mini Statement").pack()
        Button(main, text="Balance Info").pack()
        #Button(main, text="Cancel",command=main.destroy()).pack()

        main.mainloop()
        
# function to check pin..........................
    def pin_win(self):
    # HERE WE ARE TAKING PIN AND WILL CHECK THE PIN.....
        global win4
        win4 = Toplevel(master)
        win4.geometry("1920x1080")
        
        image = Image.open("pin_window.jpg")
        bg = ImageTk.PhotoImage(image)
        Label(win4, image=bg).place(relwidth=1, relheight=1)
        
        Label(win4, text="Enter your unique pin below").pack()
        
        global pin
        pin = Entry(win4, show="*")
        pin.pack(ipadx=50)
        
        enter = Button(win4, text="Enter",command=lambda:self.pin_check())
        enter.pack()

        back = Button(win4, text='back', command=lambda : win4.destroy())
        back.pack()

    def pin_check(self):
        psswd=pin.get()
        if psswd=='1234':
            pin.destroy()
            self.main_menu()
        #else:
           # mesg.show_error(master=master, text="worng pin")

f = gui_maker()
label1 = Label(master, text="STATE BANK OF INDIA", font=("Bell MT", 60))
label1.grid(row=0, column=0, padx=300, pady=100)
bt1 = Button(master, text="Start \n शुरू ", command=lambda:f.camera_face_detect())
bt1.grid(row=1, column=0)
mainloop()

