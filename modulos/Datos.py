import modulos.utils as utl
import cv2


class Datos:
    def __init__(self):
        self.imagen_original = cv2.imread(r'C:\Google Drive\Cursos\Python_OpenCV\Deskew\Docs\Texto.png', 1)
        self.imagen_trabajo = self.imagen_original
        self.flt_angulo_actual = 0.0

    def get_imagen_cv2(self):
        return self.imagen_trabajo

    def get_imagen_tk(self):
        return utl.imagen_cv2tk(self.imagen_trabajo)

    def rotar_imagen(self):
        self.imagen_trabajo = utl.rotar_imagen_cv2(self.imagen_original, self.flt_angulo_actual)
