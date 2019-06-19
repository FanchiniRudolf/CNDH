import sys
import tkinter as tk, threading            # python 3
from tkinter import font  as tkfont # python 3
from PIL import ImageTk, Image
import imageio
import random
#import Tkinter as tk
# python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic" )


        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        # use the next line if you also want to get rid of the titlebar
        self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (w, h))
        self.bind("<Escape>", sys.exit)
        self.configure(background='#C8C9CC')

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill= "both", expand=False)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, Wallpaper):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self,)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            #filler = 50
            frame.grid(row=0, column=0, sticky="S", ipadx= self.winfo_screenheight(), ipady=self.winfo_screenheight(), pady= 3)


        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''

        if page_name == "PageThree":
            self.frames = {}
            for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, Wallpaper):
                page_name = F.__name__
                frame = F(parent=self.container, controller=self, )
                self.frames[page_name] = frame

                # put all of the pages in the same location;
                # the one on the top of the stacking order
                # will be the one that is visible.
                #filler = 50
                frame.grid(row=0, column=0, sticky="S", ipadx=self.winfo_screenheight(),
                           ipady=self.winfo_screenheight(), pady=3)
            self.changeFrame("PageThree")

        elif page_name != "StartPage":
            self.changeFrame(page_name)
            self.sec = 0
            self.tick()
        else:
            self.changeFrame("StartPage")
            self.sec = 0
            self.wallpaper()



    def changeFrame(self, page_name):
        self.sec = 0
        self.secWall = 0
        self.visible_frame = page_name
        frame = self.frames[page_name]
        frame.tkraise()

    def wallpaper(self):
        if self.visible_frame == "StartPage":
            self.secWall += 1
            if self.secWall >= 10 and self.secWall<200:

                self.changeFrame("Wallpaper")
                return
            else:
                self.after(1000, self.wallpaper)
                return
        else:
            self.secWall=300
            return

    def tick(self):
        self.sec += 1
        if self.sec >= 120:
            self.show_frame("StartPage")
            return
        else:
            self.after(1000, self.tick)
            return


class StartPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background= "white")
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=3)
        self.grid_rowconfigure(4, weight=4)
        self.grid_rowconfigure(5, weight=3)
        self.grid_rowconfigure(6, weight=2)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=0)

        ima= Image.open("assetsCNDH/home.png")
        ima = ima.resize((controller.winfo_screenwidth(),controller.winfo_screenheight()))
        self.bg = ImageTk.PhotoImage(ima)
        background = tk.Label(self, image=self.bg, bg="black")
        background.place(x=0, y=0, relwidth=1, relheight=1)

        btn1 = Image.open("assetsCNDH/BotonComputo.png")
        btn1 = btn1.resize((controller.winfo_screenwidth()//5, controller.winfo_screenheight()//7))
        self.imgbt1= ImageTk.PhotoImage(btn1)
        buttonComputo = tk.Button(self, image = self.imgbt1,
                            command=lambda: controller.show_frame("PageOne"), border=0, background="#012BEF")

        btn2 = Image.open("assetsCNDH/BotonEdificio.PNG")
        btn2 = btn2.resize((controller.winfo_screenwidth() // 5, controller.winfo_screenheight() // 7))
        self.imgbt2 = ImageTk.PhotoImage(btn2)
        buttonEdificio = tk.Button(self, image = self.imgbt2,
                            command=lambda: controller.show_frame("PageTwo"),border=-1, background="#012BEF")

        btn3 = Image.open("assetsCNDH/BotonEdificio2.PNG")
        btn3 = btn3.resize((controller.winfo_screenwidth() // 5, controller.winfo_screenheight() // 7))
        self.imgbt3 = ImageTk.PhotoImage(btn3)
        buttonEdificio2 = tk.Button(self, image=self.imgbt3,
                                   command=lambda: controller.show_frame("PageFour"), border=-1, background="#012BEF")

        btn4 = Image.open("assetsCNDH/botonVideo.png")
        btn4 = btn4.resize((controller.winfo_screenwidth() // 5, controller.winfo_screenheight() // 7))
        self.imgbt4 = ImageTk.PhotoImage(btn4)
        buttonVideo = tk.Button(self, image=self.imgbt4,
                                   command=lambda: controller.show_frame("PageThree"), border=-1, background="#012BEF")


        buttonComputo.grid(column =3, row = 1)
        buttonEdificio.grid(column =3, row =3)
        buttonEdificio2.grid(column=3, row=5)
        buttonVideo.grid(column=3, row=7)




class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=3)
        self.grid_rowconfigure(4, weight=2)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=6)

        self.configure(background="white")

        ima = Image.open("assetsCNDH/centroComputo.png")
        ima = ima.resize((controller.winfo_screenwidth(), controller.winfo_screenheight()))
        self.bg = ImageTk.PhotoImage(ima)
        background = tk.Label(self, image=self.bg, bg="white")
        background.place(x=0, y=0, relwidth=1, relheight=1)

        btn = Image.open("assetsCNDH/botonBack.PNG")
        btn = btn.resize((controller.winfo_screenwidth() // 5, controller.winfo_screenheight() // 7))
        self.imgbt1 = ImageTk.PhotoImage(btn)
        button = tk.Button(self, image= self.imgbt1,
                           command=lambda: controller.show_frame("StartPage"), border=0, background="#012BEF")
        button.grid(row = 7, column = 3)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=3)
        self.grid_rowconfigure(4, weight=2)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=6)

        self.configure(background="white")

        ima = Image.open("assetsCNDH/sotanoNones.png")
        ima = ima.resize((controller.winfo_screenwidth(), controller.winfo_screenheight()))
        self.bg = ImageTk.PhotoImage(ima)
        background = tk.Label(self, image=self.bg, bg="white")
        background.place(x=0, y=0, relwidth=1, relheight=1)

        btn = Image.open("assetsCNDH/botonBack.PNG")
        btn = btn.resize((controller.winfo_screenwidth() // 5, controller.winfo_screenheight() // 7))
        self.imgbt1 = ImageTk.PhotoImage(btn)
        button = tk.Button(self, image=self.imgbt1,
                           command=lambda: controller.show_frame("StartPage"), border=0)
        button.grid(row=8, column=2)

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=3)
        self.grid_rowconfigure(4, weight=2)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=6)

        self.configure(background="white")

        ima = Image.open("assetsCNDH/sotanoPares.png")
        ima = ima.resize((controller.winfo_screenwidth(), controller.winfo_screenheight()))
        self.bg = ImageTk.PhotoImage(ima)
        background = tk.Label(self, image=self.bg, bg="white")
        background.place(x=0, y=0, relwidth=1, relheight=1)

        btn = Image.open("assetsCNDH/botonBack.PNG")
        btn = btn.resize((controller.winfo_screenwidth() // 5, controller.winfo_screenheight() // 7))
        self.imgbt1 = ImageTk.PhotoImage(btn)
        button = tk.Button(self, image=self.imgbt1,
                           command=lambda: controller.show_frame("StartPage"), border=0)
        button.grid(row=8, column=2)

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=3)
        self.grid_rowconfigure(4, weight=2)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=6)

        self.configure(background="white")

        self.video_name = "assetsCNDH/prueba.mp4"  # This is your video file path
        self.video = imageio.get_reader(self.video_name)
        self.my_label = tk.Label(self)
        self.my_label.grid(row =3, column = 2)
        self.thread = threading.Thread(target=PageThree.stream, args=(self, self.my_label, self.video, controller))
        self.thread.daemon = 1
        self.thread.start()

    def stream(self, label, video, controller):
        for image in video.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image
        if controller.visible_frame == "PageThree":
            controller.changeFrame("StartPage")

class Wallpaper(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=3)
        self.grid_rowconfigure(4, weight=2)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=6)

        self.configure(background="black")
        self.controller.bind("<Button-1>", self.goback)

        self.logo = ImageTk.PhotoImage(Image.open("assetsCNDH/Logo.PNG"))
        self.logoIm = tk.Label(self, image=self.logo, bg="black")
        self.logoIm.grid(row=1, column=1, columnspan=1)

        self.label = tk.Label(self,  text = "Para ver Directorio\n Toque la pantalla", foreground = "#C8C9CC", bg="black", font = controller.title_font)

        self.after(2000, self.anim)

    def goback(self, event):
        self.controller.show_frame("StartPage")

    def anim(self):
        rowpos = random.randint(0, 6)
        columnpos = random.randint(0,4)
        self.logoIm.grid(row=rowpos, column=columnpos, columnspan=1)
        rowpos = random.randint(0, 6)
        columnpos = random.randint(0, 4)
        self.label.grid(row=rowpos, column=columnpos, columnspan=1)
        self.after(2000, self.anim)
        return




if __name__ == "__main__":

    app = SampleApp()
    app.mainloop()