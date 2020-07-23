import tkinter as tk
from tkinter import filedialog
from PIL import Image

class pinger(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.initialize()

    def initialize(self):        
        self.iWidth = tk.StringVar()
        self.iHeight = tk.StringVar()

        # row 1
        labelDisclaim = tk.Label(self, text='Currently only works with jpegs')
        labelDisclaim.grid(column=2, row=1)

        # row 2
        labelWidth = tk.Label(self, text='Enter the width of the grid, in pixels.')
        labelWidth.grid(column=4,row=2)

        buttonOpen = tk.Button(self, text="Select an Image", command=self.openExplorer)
        buttonOpen.grid(column=2, row=2)

        # row 3
        labelStaticImg= tk.Label(self, text="Width of image, in pixels: ")
        labelStaticImg.grid(column=1,row=3)

        labelImgWidth = tk.Label(self, textvariable=self.iWidth)
        labelImgWidth.grid(column=2,row=3)

        labelStaticHeight= tk.Label(self, text="Height of image, in pixels: ")
        labelStaticHeight.grid(column=3,row=3)

        labelImgHeight = tk.Label(self, textvariable=self.iHeight)
        labelImgHeight.grid(column=4,row=3)

        # row 9
        button = tk.Button(self,text="exit",command=self.closeProgram)
        button.grid(column=3,row=9)

        # row 10
        labelSig = tk.Label(self, text='By Johnathan Keith, 2020. Ver 1.0')
        labelSig.grid(column=3,row=10)

    def openFile(self, imagefilename):
        Img = Image.open(imagefilename)
        height, width = Img.size
        self.iHeight.set(height)
        self.iWidth.set(width)

    def closeProgram(self):
        self.destroy()

    def openExplorer(self):
        filename= filedialog.askopenfilename(initialdir="/", title="Select an Image", filetypes=(("jpeg files", "*.jpg"),("all files", "*.*")))
        if filename:
           print(filename)
           self.openFile(filename)

if __name__ == "__main__":
    app = pinger()
    app.title('Image Gridder')
    app.minsize(height=680,width=480)
    app.mainloop()
