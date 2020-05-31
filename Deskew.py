import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import modulos.Datos as dt

import os


class App(tk.Frame):
    def __init__(self, master_=None, dimensiones_='1280x720', titulo_='Aplicación', icono_=None):
        super().__init__(master=master_)
        self.directorio = os.getcwd()
        self.master.geometry(dimensiones_)
        self.master.title(titulo_)
        self.master.iconbitmap(icono_)
        self.pack(fill='both', expand=True)
        self.datos = dt.Datos()

        '----------- Widgets -----------'
        self.frame_izquierdo = Frame_izquierdo(self, self.datos)
        self.frame_derecho = Frame_derecho(self, self.datos)
        self.separador = ttk.Separator(self, orient='vertical')

        '----------- Layout -----------'
        self.frame_izquierdo.grid(column=0, row=0, sticky='nsew')
        self.separador.grid(column=1, row=0, sticky='nsew')
        self.frame_derecho.grid(column=2, row=0, sticky='nsew')
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)


class Frame_izquierdo(tk.Frame):
    def __init__(self, padre_, datos_: dt.Datos):
        super().__init__(master=padre_)
        self.configure(bg='black')
        self.datos = datos_
        self.img_canvas = datos_.get_imagen_tk()

        '----------- Widgets -----------'
        self.cnv_imagen = tk.Canvas(self, bg='gray')
        self.separador = ttk.Separator(self, orient='horizontal')
        self.frame_inferior = ttk.Frame(self)
        '----------- Layout -----------'
        self.cnv_imagen.grid(column=0, row=0, sticky='nsew')
        self.separador.grid(column=0, row=1, sticky='nsew')
        self.frame_inferior.grid(column=0, row=2, sticky='nsew')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)

        '----------- Widgets Frame inferior -----------'
        self.ctrol_angulo = ttk.Spinbox(self.frame_inferior)
        self.ctrol_angulo.configure(command=lambda: self.cmd_ctrl_angulo(), from_=-45.0, to=45.0, increment=0.1)
        self.ctrol_angulo.set(0)
        self.lbl_angulo = ttk.Label(self.frame_inferior)

        '----------- Layout Frame inferior -----------'
        self.frame_inferior.columnconfigure(0, weight=10)
        self.frame_inferior.columnconfigure(1, weight=1)
        self.ctrol_angulo.grid(column=0, row=0, sticky='ew')
        self.lbl_angulo.grid(column=1, row=0, sticky='ew')

        '----------- Rutina de inicio -----------'
        self.actualizar_imagen()

    def actualizar_imagen(self, ):
        self.img_canvas = self.datos.get_imagen_tk()
        self.cnv_imagen.create_image(0, 0, anchor='nw', image=self.img_canvas, tags='analisis')

    def cmd_ctrl_angulo(self):
        print('Cmd Ctrol angulo')
        self.datos.flt_angulo_actual = float(self.ctrol_angulo.get())
        self.datos.rotar_imagen()
        self.actualizar_imagen()
        self.datos.actualizar_figura_plt()


class Frame_derecho(ttk.Frame):
    def __init__(self, padre_, datos_: dt.Datos):
        super().__init__(master=padre_)
        self.datos = datos_

        '----------- Widgets -----------'
        self.cnv_plt_canvas = FigureCanvasTkAgg(self.datos.get_figura_plt(), self, )
        self.lbl_sum_psd = ttk.Label(self, text='Suma de PSD:')

        '----------- Layout -----------'
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.cnv_plt_canvas.get_tk_widget().grid(column=0, row=0, sticky='nsew')
        self.lbl_sum_psd.grid(column=0, row=1, sticky='nsew')


# **************** Loop principal ****************
aplicacion = App(dimensiones_='1280x720', titulo_='Prueba de concepto Deskew')
aplicacion.mainloop()
