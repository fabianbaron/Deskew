import unittest
import matplotlib.pyplot as plt
import numpy as np
import cv2
import modulos.Datos as dt


class Plt(unittest.TestCase):
    def setUp(self) -> None:
        print('--> Iniciando test')
        datosx = [1, 2, 3, 4, 5, 6]
        datosy = [2, 4, 6, 7, 9, 2]
        self.imagen = cv2.imread(r'C:\Google Drive\Cursos\Python_OpenCV\Deskew\Docs\Texto.png', 1)
        self.datos = dt.Datos()

    def tearDown(self) -> None:
        print('--> Test terminado')

    def test_figura(self):
        fig = plt.Figure(figsize=(5, 5), dpi=100)
        plt_axes = fig.add_subplot(111)
        plt_axes.plot([1, 2, 3, 4, 5, 6], [2, 4, 6, 7, 9, 2])
        plt.show()
        y = np.random.rand(100)
        x = range(0, 100, 1)
        plt_axes.plot(x, y)
        plt.show()
        cv2.imshow('Ventana', self.imagen)
        cv2.waitKey()

    def test_matrices(self):
        self.datos.actualizar_figura_plt()


class FFT(unittest.TestCase):

    def setUp(self) -> None:
        print('--> Iniciando test')

    def tearDown(self) -> None:
        print('--> Test terminado')

    def test_fft(self):
        dti = 0.001
        t = np.arange(0, 1, dti)
        f = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)
        f_clean = f
        f = f + 2.5 * np.random.randn(len(t))
        # plt.plot(t, f)
        # plt.plot(t, f_clean)
        # plt.show()

        n = len(t)
        fhat = np.fft.fft(f, n)
        PSD = fhat * np.conj(fhat) / n
        plt.plot(PSD[:n // 2])
        plt.show()


if __name__ == '__main__':
    unittest.main()
