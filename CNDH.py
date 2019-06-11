import tkinter as tk, threading            # python 3
from tkinter import font  as tkfont # python 3
from PIL import ImageTk, Image
import imageio
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")


        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        # use the next line if you also want to get rid of the titlebar
        self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (w, h))
        self.bind("<Escape>", exit)
        self.configure(background='#C8C9CC')

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill= "both", expand=False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self,)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            filler = 50
            frame.grid(row=0, column=0, sticky="S", ipadx= self.winfo_screenheight(), ipady=self.winfo_screenheight(), pady= 3)

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


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
        self.grid_rowconfigure(4, weight=2)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=0)

        self.logo = ImageTk.PhotoImage(Image.open("assetsCNDH/Logo.PNG"))
        logoIm = tk.Label(self, image=self.logo, bg="white")
        logoIm.grid(row=2, column =2, columnspan = 1)

        self.ubi = ImageTk.PhotoImage(Image.open("assetsCNDH/Ubicacion.PNG"))
        label = tk.Label(self, image=self.ubi, font=controller.title_font, bg= "white")
        label.grid(column =2, row =3)

        self.imgbt1= ImageTk.PhotoImage(Image.open("assetsCNDH/BotonComputo.PNG"))
        buttonComputo = tk.Button(self, image = self.imgbt1,
                            command=lambda: controller.show_frame("PageOne"), border=0)
        self.imgbt2 = ImageTk.PhotoImage(Image.open("assetsCNDH/BotonEdificio.PNG"))
        buttonEdificio = tk.Button(self, image = self.imgbt2,
                            command=lambda: controller.show_frame("PageTwo"),border=-1)

        self.imgbt3 = ImageTk.PhotoImage(Image.open("assetsCNDH/botonVideo.png"))
        buttonVideo = tk.Button(self, image=self.imgbt3,
                                   command=lambda: controller.show_frame("PageThree"), border=-1)
        buttonComputo.grid(column =1, row = 4, sticky= "E")
        buttonEdificio.grid(column =3, row =4, sticky= "W")
        buttonVideo.grid(column=2, row=4, sticky="W")




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
        self.grid_rowconfigure(0, weight=6)

        self.configure(background="white")

        self.logo = ImageTk.PhotoImage(Image.open("assetsCNDH/Logo.PNG"))
        logoIm = tk.Label(self, image=self.logo, bg="white")
        logoIm.grid(row=1, column=1, columnspan=1)

        self.ubi = ImageTk.PhotoImage(Image.open("assetsCNDH/seccionesComputo.PNG"))
        label = tk.Label(self, text="SÓTANO\n\nSubdirección de Servicios Generales\n\nPLANTA BAJA\n\nSubdirección de Desarrollo Informático\n\nSubdirección de Desarrollo Tecnológico y Comunicaciones\nSubdirección de Administración de Proyectos\n\nPISO 1\n\nSubdirección de Desarrollo Informático\n\nSubdirección de Desarrollo Tecnológico y Comunicaciones\nSubdirección de Administración de Proyectos\nDirección General de Quejas, Orientación y Transparencia",
                         font=controller.title_font, bg="white", justify = "left")
        label.grid(row = 2, column = 1)

        self.namePlace = ImageTk.PhotoImage(Image.open("assetsCNDH/nombreComputo.PNG"))
        label2 = tk.Label(self, image=self.namePlace, font=controller.title_font)
        label2.grid(row = 1, column = 3)


        self.imgbt1 = ImageTk.PhotoImage(Image.open("assetsCNDH/botonBack.PNG"))
        button = tk.Button(self, image= self.imgbt1,
                           command=lambda: controller.show_frame("StartPage"), border=0)
        button.grid(row = 4, column = 3)

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
        self.grid_rowconfigure(0, weight=6)

        self.configure(background="white")

        self.logo = ImageTk.PhotoImage(Image.open("assetsCNDH/Logo.PNG"))
        logoIm = tk.Label(self, image=self.logo, bg="white")
        logoIm.grid(row=1, column=1, columnspan=1)

        self.ubi = ImageTk.PhotoImage(Image.open("assetsCNDH/seccionesComputo.PNG"))
        label = tk.Label(self,
                         text="SOTANO 2 PERIFÉRICO\nDirección General de Quejas, Orientación y\nTransparencia\n\nSOTANO 1 CONTRERAS\nSubdirección de Servicios Generales\n\nPLANTA BAJA PERIFÉRICO\nDirección General de Quejas, Orientación y\nTransparencia\nUnidad de Transparencia",
                         font=controller.title_font, bg="white", justify="left")
        label.grid(row=2, column=1)

        label = tk.Label(self,
                         text="\nOficialía de Partes\nPLANTA BAJA CONTRERAS\nDirección General de Quejas, Orientación y\nTransparencia\nDirección de Atención al Público\nLudoteca\nSala de Lactancia\nCentro de Atención Telefónica\n\nMEZANINE PERIFÉRICO\nAuditorio\nCuarta Visitaduría:\nDirección de Asuntos de Seguridad Social en\nmateria de Vivienda\nDirección de Asuntos de Indígenas en Reclusión"
                         ,font=controller.title_font, bg="white", justify="left")
        label.grid(row=2, column=3)


        self.namePlace = ImageTk.PhotoImage(Image.open("assetsCNDH/nombreComputo.PNG"))
        label2 = tk.Label(self, image=self.namePlace, font=controller.title_font)
        label2.grid(row=1, column=3)

        self.imgbt1 = ImageTk.PhotoImage(Image.open("assetsCNDH/botonBack.PNG"))
        button = tk.Button(self, image=self.imgbt1,
                           command=lambda: controller.show_frame("StartPage"), border=0)
        button.grid(row=4, column=3)

class PageThree(tk.Frame):
    def stream(label, video):

        for image in video.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image

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
        self.grid_rowconfigure(0, weight=6)

        self.configure(background="white")

        self.video_name = "assetsCNDH/prueba.mp4"  # This is your video file path
        self.video = imageio.get_reader(self.video_name)
        self.my_label = tk.Label(self)
        self.my_label.grid(row =3, column = 2)
        self.thread = threading.Thread(target=PageThree.stream, args=(self.my_label, self.video))
        self.thread.daemon = 1
        self.thread.start()


if __name__ == "__main__":

    app = SampleApp()
    app.mainloop()