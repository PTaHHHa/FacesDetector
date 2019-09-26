import cv2

class Photo:
    def __init__(self,filename,scaleFactor,minNeighbors):
        self.scaleFactor=scaleFactor
        self.minNeighbors=minNeighbors
        self.file=cv2.imread(filename,1)
        self.face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def loadfile(self):
        self.faces=self.face_cascade.detectMultiScale(self.file,float(self.scaleFactor),int(self.minNeighbors))

    def rectangle(self):
        for x,y,w,h in self.faces:
            self.img=cv2.rectangle(self.file,(x,y),(x+w,y+h),(0,255,0),4)

    def viewing(self):
        self.resized=cv2.resize(self.img,(700,500))
        cv2.imshow("Face Finder",self.resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


