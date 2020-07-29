import tkinter as tk
from tkinter import filedialog
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

class gridder(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.initialize()

    def initialize(self):        
        self.iWidth = tk.StringVar()
        self.iHeight = tk.StringVar()
        self.imgSelect = tk.StringVar()
        self.squareLength= tk.IntVar()
        self.ratioX=tk.IntVar()
        self.ratioY=tk.IntVar()
        self.checkSquare = tk.IntVar()
        
        self.checkSquare.set(0)
        self.ratioX.set(10)
        self.ratioY.set(10)
        self.squareLength.set(120)
        

        # row 1
        labelDisclaim = tk.Label(self, text='Currently only works with jpegs')
        labelDisclaim.grid(column=2, row=1)

        # row 2
        buttonOpen = tk.Button(self, text="Select an Image", command=self.openExplorer)
        buttonOpen.grid(column=1, row=2)

        labelSelected= tk.Label(self, text="Selected Image: ")
        labelSelected.grid(column=2,row=2)

        labelImgName = tk.Label(self, textvariable=self.imgSelect)
        labelImgName.grid(column=3,row=2)
        

        # row 3
        labelStaticImg= tk.Label(self, text="Width of image, in pixels: ")
        labelStaticImg.grid(column=1,row=3)

        labelImgWidth = tk.Label(self, textvariable=self.iWidth, anchor='w')
        labelImgWidth.grid(column=2,row=3)

        labelStaticHeight= tk.Label(self, text="Height of image, in pixels: ")
        labelStaticHeight.grid(column=3,row=3)

        labelImgHeight = tk.Label(self, textvariable=self.iHeight, anchor='w')
        labelImgHeight.grid(column=4,row=3)

        # row 4
        labelRatioX = tk.Label(self, text="Enter the Ratio along the X axis, default is 10: ")
        labelRatioX.grid(column=1,row=4)

        entryRatioX = tk.Entry(self, textvariable=self.ratioX)
        entryRatioX.grid(column=2,row=4)

        labelRatioY =tk.Label(self, text="Enter the Ratio along the Y axis, default is 10: ")
        labelRatioY.grid(column=3,row=4)

        entryRatioY = tk.Entry(self, textvariable=self.ratioY)
        entryRatioY.grid(column=4,row=4)

        # row 5
        labelSquare = tk.Label(self, text="For strict squares, in the sense of a battle map, check this ->")
        labelSquare.grid(column=1,row=5)

        checkboxSquare = tk.Checkbutton(self, variable=self.checkSquare, text="If checked, it will ignore the ratio and apply squares that are specified by the entry, (default 120x120) ->",wraplength=150)
        checkboxSquare.grid(column=2,row=5)

        labelSquareLength = tk.Label(self, text="Side length of Square: ")
        labelSquareLength.grid(column=3,row=5)

        entrySquareLength = tk.Entry(self, textvariable=self.squareLength)
        entrySquareLength.grid(column=4,row=5)

        
        # row 6
        execButton = tk.Button(self, text="Gridify", command=self.gridify)
        execButton.grid(column=2,row=6)
        
        # row 9
        button = tk.Button(self,text="Exit",command=self.closeProgram)
        button.grid(column=2,row=9)

        # row 10
        labelSig = tk.Label(self, text='By Johnathan Keith, 2020. Ver 1.0. This is free-to-use, and will always be. This was willingly distributed to the public.',wraplength=350)
        labelSig.grid(column=2,row=10)

    def openFile(self, imagefilename):
        Img = Image.open(imagefilename)
        height, width = Img.size
        self.iHeight.set(height)
        self.iWidth.set(width)

    def gridify(self):
        ratioX=0
        ratioY=0
        sidelengthy=0
        sidelengthx=0
        if self.checkSquare.get():
            ratioX=int(self.squareLength.get())
            ratioY=int(self.squareLength.get())
            sidelengthx=ratioX
            sidelengthy=ratioY
        else:
            ratioX=int(self.ratioX.get())
            ratioY=int(self.ratioY.get())
            sidelengthy=int(self.iWidth.get())/ratioY
            sidelengthx=int(self.iHeight.get())/ratioX
        image=Image.open(self.imgSelect.get())
        my_dpi=300.

        #set the figure up
        fig=plt.figure(figsize=(float(image.size[0])/my_dpi,float(image.size[1])/my_dpi),dpi=my_dpi)
        ax=fig.add_subplot(111)

        #remove whitespace
        fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

        #set gridding interval
        locx = plticker.MultipleLocator(base=sidelengthx)
        locy = plticker.MultipleLocator(base=sidelengthy)
        ax.xaxis.set_major_locator(locx)
        ax.yaxis.set_major_locator(locy)

        #add the grid
        ax.grid(which='major', axis='both', linestyle='-',color='k')

        ax.imshow(image)

        token=self.imgSelect.get().split('/')
        saveName= "gridded_"+token[-1]
        
        # Save the figure
        fig.savefig(saveName,dpi=my_dpi)

    def closeProgram(self):
        self.destroy()
        exit()

    def dataEntry(self):
        if type(int) == type(int(bHeight)):
            self.bHeight = int(entryHeight.get())
        else:
            return
        
    def openExplorer(self):
        filename= filedialog.askopenfilename(initialdir="/", title="Select an Image", filetypes=(("jpeg files", "*.jpg"),("all files", "*.*")))
        if filename:
           print(filename)
           self.imgSelect.set(filename)
           self.openFile(filename)
           

if __name__ == "__main__":
    app = gridder()
    app.title('Image Gridder')
    app.minsize(height= 480, width=680)
    app.mainloop()
