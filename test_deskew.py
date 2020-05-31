import unittest
import matplotlib.pyplot as plt


class Plt(unittest.TestCase):
    def setUp(self) -> None:
        print('--> Iniciando test')
        datosx = [1, 2, 3, 4, 5, 6]
        datosy = [2, 4, 6, 7, 9, 2]

    def tearDown(self) -> None:
        print('--> Test terminado')

    def test_figura(self):
        fig = plt.Figure(figsize=(5, 5), dpi=100)
        plt_axes = fig.add_subplot(111)
        plt_axes.plot([1, 2, 3, 4, 5, 6], [2, 4, 6, 7, 9, 2])
        plt.show()


if __name__ == '__main__':
    unittest.main()
