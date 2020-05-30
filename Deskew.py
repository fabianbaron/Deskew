# import cv2
import tkinter as tk
from tkinter import ttk

import os

"""
todo [feat]: Canvas de imágen CV2
todo [feat]: Control de rotación
todo [feat]: Rotar imagen cv2 usando control de rotación
todo [feat]: Canvas de imagen matplotlib
todo [feat]: Barra de navegación

"""


class App(tk.Frame):
    def __init__(self, master_=None, dimensiones_='1280x720', titulo_='Aplicación', icono_=None):
        super().__init__(master=master_)
        self.directorio = os.getcwd()
        self.master.geometry(dimensiones_)
        self.master.title(titulo_)
        self.master.iconbitmap(icono_)
        self.pack(fill='both', expand=True)
        '----------- Widgets -----------'
        self.frame_izquierdo = Frame_izquierdo(self)
        self.frame_derecho = Frame_derecho(self)
        self.separador = ttk.Separator(self, orient='vertical')

        '----------- Layout -----------'
        self.frame_izquierdo.grid(column=0, row=0, sticky='nsew')
        self.separador.grid(column=1, row=0, sticky='nsew')
        self.frame_derecho.grid(column=2, row=0, sticky='nsew')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)


class Frame_izquierdo(tk.Frame):
    def __init__(self, padre_):
        super().__init__(master=padre_)
        self.configure(bg='black')

        '----------- Widgets -----------'
        self.imagen = tk.Canvas(self, bg='gray')
        self.separador = ttk.Separator(self, orient='horizontal')
        '----------- Layout -----------'
        self.imagen.grid(column=0, row=0, sticky='nsew')
        self.separador.grid(column=0, row=1, sticky='nsew')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)


class Frame_derecho(ttk.Frame):
    def __init__(self, padre_):
        super().__init__(master=padre_)
        '----------- Widgets -----------'
        '----------- Layout -----------'
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)


class Modelo:
    pass


# **************** Loop principal ****************
aplicacion = App(dimensiones_='1280x720', titulo_='Prueba de concepto Deskew')
aplicacion.mainloop()
