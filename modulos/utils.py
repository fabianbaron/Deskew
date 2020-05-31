import glob
from PIL import Image, ImageTk
import numpy as np

import cv2
import os


def find_nombre_archivo(ruta_: str) -> str:
    return os.path.splitext(os.path.basename(ruta_))[0]


def find_ruta_archivo(ruta_: str) -> str:
    return os.path.dirname(ruta_)


def limpiar_directorio(ruta_: str):
    print(f'Limpiando directorio \'{ruta_}\'...')
    files = glob.glob(f'{ruta_}/*.jpg')
    for f in files:
        print(f'Borrando {f}...')
        os.remove(f)


def guardar_archivo(ruta_archivo, datos):
    ruta = find_ruta_archivo(ruta_archivo)
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    archivo = open(ruta_archivo, 'w')
    archivo.write(datos)


def limpiar_acentos(texto: str) -> str:
    return ''.join([letra for letra in texto if ord(letra) < 123])


def convertir_imagenes_a_jpg(archivo_entrada_: str, archivo_salida_: str = '') -> str:
    if archivo_salida_ == '':
        archivo_salida_ = f'{find_ruta_archivo(archivo_entrada_)}/{find_nombre_archivo(archivo_entrada_)}.jpg'
    im = Image.open(archivo_entrada_)
    im.save(archivo_salida_)
    print(f'Imagen guardada en: {archivo_salida_}')
    return archivo_salida_


def imagen_cv2tk(img_cv2):
    img_rgb = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(img_rgb)  # Convertir imagen a formato PIL
    image_tk = ImageTk.PhotoImage(image_pil)  # Covertir imagen a formato Tkinter
    print('Imagen de cv2 a Tkinter')
    return image_tk


def cortar_imagen(imagen_cv2, x1_, y1_, x2_, y2_):
    recorte_cv2 = imagen_cv2[y1_:y2_, x1_:x2_]
    return recorte_cv2


def guardar_imagen_cv2(ruta_archivo, imagen_cv2):
    ruta = find_ruta_archivo(ruta_archivo)
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    cv2.imwrite(ruta_archivo, imagen_cv2)


def rotar_imagen_cv2(imagen_cv2_, angulo_: float):
    (h, w) = imagen_cv2_.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angulo_, 1.0)
    imagen_rotada = cv2.warpAffine(imagen_cv2_, M, (w, h),
                                   flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return imagen_rotada


def normalizar_datos(datos: np.array) -> np.array:
    datos_abs = np.abs(datos)
    datos_normalizados = datos_abs / np.max(datos_abs)
    return datos_normalizados
