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
        self.bWidth = 0
        self.bHeight= 0
        

        # row 1
        labelDisclaim = tk.Label(self, text='Currently only works with jpegs')
        labelDisclaim.grid(column=2, row=1)

        # row 2
<<<<<<< HEAD
=======

>>>>>>> ced526c8d061d059d8a23ac2d650dcc927ce2f6c
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
<<<<<<< HEAD
        labelInstructions = tk.Label(self, text='First, select an image, then below enter, in pixels, how wide and tall you want each grid section to be. If left empty, it will try to square them. Default value will try to have a 10x10 grid.', anchor='w', wraplength=200)
        labelInstructions.grid(column=2,row=4)

        # row 5
        labelWidth = tk.Label(self, text='Enter the width of the grid, in pixels: ')
        labelWidth.grid(column=1,row=5)
        
        labelHeight = tk.Label(self, text='Enter the width of the grid, in pixels: ')
        labelHeight.grid(column=3, row=5)

        # row 8 non-grid image to gridded image, pics
        

=======
        defaultLabel = tk.Label(self, text="The default square is a side length of 1/10th the image height/width. Whichever is smaller.", wraplength=100)
        defaultLabel.grid(column=2,row=4)

        # row 5
        dataButton = tk.Button(self, text="Enter", command=self.dataEntry)
        dataButton.grid(column=3,row=5)

        # row 6
        execButton = tk.Button(self, text="Gridify", command=self.gridify)
        execButton.grid(column=3,row=6)
        
>>>>>>> ced526c8d061d059d8a23ac2d650dcc927ce2f6c
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
        sidelengthy=int(self.iWidth.get())/10
        sidelengthx=int(self.iHeight.get())/10
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

        
        
        # Save the figure
        fig.savefig('gridify.jpg',dpi=my_dpi)

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
<<<<<<< HEAD
=======
    app.minsize(height= 480, width=680)
>>>>>>> ced526c8d061d059d8a23ac2d650dcc927ce2f6c
    app.mainloop()
