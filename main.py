import cv2
import glob
from tkinter import Button,Label,filedialog,Grid,Tk,Listbox,StringVar,Entry,Text,END
from tkinter.font import Font
from backend import Photo
import ToolTips

class Window(object):
    def __init__(self,window):

        font_obj=Font(family="Courier",size=25)

        self.window=window
        self.window.title("Face Finder")
        self.text_widget = Text(window,height=1,width=35)
        self.text_widget.grid(row=0,column=0)

        self.sf=Label(window,text="Scale (in %)",font=font_obj)
        self.mn=Label(window,text="minNeighbors",font=font_obj)
        self.sf.grid(row=2,column=0)
        self.mn.grid(row=3,column=0)
        self.scale_filed=StringVar()
        self.minNeighbors_filed=StringVar()
        self.e1=Entry(window,textvariable=self.scale_filed)
        self.e2=Entry(window,textvariable=self.minNeighbors_filed)
        self.e1.grid(row=2,column=1)
        self.e2.grid(row=3,column=1)

        self.button = Button(window, text="Open", command=self.Upload)
        self.face_button = Button(window, text="Find Faces",command=self.values)
        self.button.grid(row=0, column=1)
        self.face_button.grid(row=4, column=0)
        widgets=[]
        tooltip_text=[]
        tooltip_text.append("scaleFactor: This function compensates a false perception in "
                            "size that occurs when one face appears to be bigger than the "
                            "other simply because it is closer to the camera.")
        tooltip_text.append("minNeighbors: This is a detection algorithm that uses a moving "
                            "window to detect objects, it does so by defining how many objects"
                            " are found near the current one before it can declare the face found")
        widgets.append(self.e1)
        widgets.append(self.e2)

        scaleFactor_tooltip=ToolTips.ToolTips(widgets,tooltip_text,font_obj)

    def Upload(self):
        self.filename=filedialog.askopenfilename()
        self.text_widget.delete('1.0',END)
        self.text_widget.insert('1.0',self.filename)

    def values(self):
        self.sf=float(self.scale_filed.get())/100+1.0
        self.mf=self.minNeighbors_filed.get()
        photo = Photo(self.filename, self.sf, self.mf)
        photo.loadfile()
        photo.rectangle()
        photo.viewing()
        print("photo")

window=Tk()
Window(window)
window.mainloop()