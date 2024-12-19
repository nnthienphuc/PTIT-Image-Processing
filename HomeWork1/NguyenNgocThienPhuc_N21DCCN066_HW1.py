import matplotlib.pyplot as plt
import cv2

def AHE(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to open image {image_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=None, tileGridSize=(8, 8))
    equalized = clahe.apply(gray)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))  # 1 hàng, 2 cột

    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Đổi từ BGR sang RGB
    axes[0].axis('off')
    axes[0].set_title('Original Image')

    axes[1].imshow(equalized, cmap='gray')  # Hiển thị ảnh đã xử lý
    axes[1].axis('off')
    axes[1].set_title('AHE Image')

    plt.show()
    plt.imsave("D:/Full-Document/PTIT/4-Fourth-year/Semester-1/Image-Processing/Exercises/HomeWork1/AHE.png", equalized, cmap='gray')

def CLAHE(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to open image {image_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    equalized = clahe.apply(gray)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))  # 1 hàng, 2 cột

    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Đổi từ BGR sang RGB
    axes[0].axis('off')
    axes[0].set_title('Original Image')

    axes[1].imshow(equalized, cmap='gray')  # Hiển thị ảnh đã xử lý
    axes[1].axis('off')
    axes[1].set_title('CLAHE Image')

    plt.show()
    plt.imsave("D:/Full-Document/PTIT/4-Fourth-year/Semester-1/Image-Processing/Exercises/HomeWork1/CLAHE.png", equalized, cmap='gray')

if __name__ == "__main__":
    # AHE("D:/Full-Document/PTIT/4-Fourth-year/Semester-1/Image-Processing/Exercises/HomeWork1/parrot.jpg")
    CLAHE("D:/Full-Document/PTIT/4-Fourth-year/Semester-1/Image-Processing/Exercises/HomeWork1/parrot.jpg")
