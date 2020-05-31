import modulos.utils as utl
import cv2
import matplotlib.pyplot as plt
import numpy as np


class Datos:

    def __init__(self):
        # self.ruta_imagen = r'C:\Users\fabia\Downloads\ASD\ICR\Datos ejemplo\Antioquia/197303ANT068T-013.tif'
        # self.ruta_imagen = r'C:\Users\fabia\Downloads\ASD\ICR\Datos ejemplo\Antioquia/197402ANT028T-014.tif'
        # self.ruta_imagen = r'C:\Users\fabia\Downloads\ASD\ICR\Codigo\Tkinter\Datos\gato.png'
        self.ruta_imagen = r'C:\Google Drive\Cursos\Python_OpenCV\Deskew\Docs\Texto.png'
        self.imagen_original = cv2.imread(self.ruta_imagen, 1)
        self.imagen_original_gray = cv2.cvtColor(self.imagen_original, cv2.COLOR_BGR2GRAY)
        self.imagen_original_gray = cv2.bitwise_not(self.imagen_original_gray)
        self.imagen_trabajo = self.imagen_original_gray

        self.flt_angulo_actual = 0.0
        self.indice_angulo = 0
        self.flt_rango_angular = np.arange(-450, 450, 1) / 10
        self.plt_figura, self.plt_ejes = plt.subplots(3)

        self.plt_ejes[0].set_ylim(ymin=-0.1, ymax=1.1)
        self.plt_ejes[0].set_title('Promedios', y=0.9)
        self.plt_ejes[0].set_xlabel('N° de línea horizontal')
        self.plt_ejes[0].set_ylabel('Promedio de línea normalizado')

        self.plt_ejes[1].set_ylim(ymin=-0.1, ymax=1.1)
        self.plt_ejes[1].set_title('FFT', y=0.9)
        self.plt_ejes[1].set_xlabel('Frecuencia')
        self.plt_ejes[1].set_ylabel('PSD normalizada')

        self.plt_ejes[2].set_ylim(ymin=-0.1, ymax=1.1)
        self.plt_ejes[2].set_title('Suma de PSD normalizada', y=0.9)
        self.plt_ejes[2].set_xlabel('Angulo')
        self.plt_ejes[2].set_ylabel('Sum PSD')

        self.plt_y = np.array([], np.float)
        self.plt_psd_y = np.array([], np.float)
        self.plt_fft_y_cplx = np.array([], np.complex_)
        self.sum_psd = np.ones(self.flt_rango_angular.shape, np.float) * 0.001

        print(self.sum_psd.shape, self.flt_rango_angular.shape)

        # self.analizar_imagen()
        self.iniciar_suma_psd()
        self.plt_x = range(0, len(self.plt_y), 1)
        self.plt_frec = range(0, len(self.plt_psd_y), 1)
        self.line_prom, = self.plt_ejes[0].plot(self.plt_x, self.plt_y)
        self.line_fft, = self.plt_ejes[1].plot(self.plt_frec, self.plt_psd_y)
        self.line_sum_psd, = self.plt_ejes[2].plot(self.flt_rango_angular, self.sum_psd)

    def get_imagen_cv2(self):
        return self.imagen_trabajo

    def get_imagen_tk(self):
        return utl.imagen_cv2tk(self.imagen_trabajo)

    def rotar_imagen(self):
        self.imagen_trabajo = utl.rotar_imagen_cv2(self.imagen_original_gray, self.flt_angulo_actual)

    def get_figura_plt(self) -> plt.Figure:
        return self.plt_figura

    def actualizar_figura_plt(self):
        self.analizar_imagen()
        self.actualizar_figura_sum_psd()
        self.plt_psd_y_n = utl.normalizar_datos(self.plt_psd_y)
        self.line_prom.set_ydata(self.plt_y)
        self.line_fft.set_ydata(self.plt_psd_y_n)
        self.plt_figura.canvas.draw()

    def analizar_imagen(self):
        self.plt_y = np.average(self.imagen_trabajo, axis=1) / 255
        self.plt_fft_y_cplx = np.fft.fft(self.plt_y, self.plt_y.shape[0])[2:]
        self.plt_psd_y = self.plt_fft_y_cplx * np.conj(self.plt_fft_y_cplx) / self.plt_y.shape[0]
        self.plt_psd_y = self.plt_psd_y[:len(self.plt_psd_y) // 2]
        self.valor_suma_psd = np.sum(self.plt_psd_y)

    def actualizar_figura_sum_psd(self):
        for id_1, angulo in enumerate(self.flt_rango_angular):
            if angulo == self.flt_angulo_actual:
                self.indice_angulo = id_1
        self.sum_psd[self.indice_angulo] = self.valor_suma_psd
        self.sum_psd_n = utl.normalizar_datos(self.sum_psd)
        self.line_sum_psd.set_ydata(self.sum_psd_n)

    def iniciar_suma_psd(self):
        print('Iniciando suma de PSD')
        for id_1, angulo in enumerate(self.flt_rango_angular):
            self.flt_angulo_actual = angulo
            self.rotar_imagen()
            self.analizar_imagen()
            self.sum_psd[id_1] = self.valor_suma_psd
            print('Angulo:', angulo)
        self.flt_angulo_actual = 0
