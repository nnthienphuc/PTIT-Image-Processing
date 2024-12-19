import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def problem1():

    lena = np.fromfile('D:/Full-Document/PTIT/4-Fourth-year/Semester-1/Image-Processing/Exercises/HomeWork2/lenabin.sec', dtype=np.uint8).reshape(256, 256)
    peppers = np.fromfile('D:/Full-Document/PTIT/4-Fourth-year/Semester-1/Image-Processing/Exercises/HomeWork2/peppersbin.sec', dtype=np.uint8).reshape(256, 256)

    plt.figure(figsize=(10, 5))
    plt.subplot(121)
    plt.imshow(lena, cmap='gray')
    plt.title('Lena')
    plt.subplot(122)
    plt.imshow(peppers, cmap='gray')
    plt.title('Peppers')
    plt.show()


    J = np.zeros((256, 256), dtype=np.uint8)
    J[:, :128] = lena[:, :128]
    J[:, 128:] = peppers[:, 128:]

    plt.figure()
    plt.imshow(J, cmap='gray')
    plt.title('Image J')
    plt.show()

    # (c) Create image K
    K = np.zeros((256, 256), dtype=np.uint8)
    K[:, :128] = J[:, 128:]
    K[:, 128:] = J[:, :128]

    plt.figure()
    plt.imshow(K, cmap='gray')
    plt.title('Image K')
    plt.show()


# Problem 2
def problem2():
    J1 = np.array(Image.open('D:/Full-Document/PTIT/4-Fourth-year/Semester-1/Image-Processing/Exercises/HomeWork2/lenagray.jpg'))

    plt.figure()
    plt.imshow(J1, cmap='gray')
    plt.title('Original Image (J1)')
    plt.show()

    J2 = 255 - J1

    plt.figure()
    plt.imshow(J2, cmap='gray')
    plt.title('Photographic Negative (J2)')
    plt.show()

    Image.fromarray(J2).save('D:/Full-Document/PTIT/4-Fourth-year/Semester-1/Image-Processing/Exercises/HomeWork2/negative_lena.jpg')


def problem3():

    J1 = np.array(Image.open('D:/Full-Document/PTIT/4-Fourth-year/Semester-1/Image-Processing/Exercises/HomeWork2/lena512color.jpg'))

    plt.figure()
    plt.imshow(J1)
    plt.title('Original Color Image (J1)')
    plt.show()

    J2 = J1.copy()
    J2[:, :, 0] = J1[:, :, 2]  # Red = Blue
    J2[:, :, 1] = J1[:, :, 0]  # Green = Red
    J2[:, :, 2] = J1[:, :, 1]  # Blue = Green

    plt.figure()
    plt.imshow(J2)
    plt.title('Color Swapped Image (J2)')
    plt.show()

    Image.fromarray(J2).save('D:/Full-Document/PTIT/4-Fourth-year/Semester-1/Image-Processing/Exercises/HomeWork2/color_swapped_lena.jpg')


if __name__ == "__main__":
    problem1()
    problem2()
    problem3()
