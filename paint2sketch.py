import cv2
import numpy as np


def inverse_color(image):
    """
    反色
    :param image:
    :return:image
    """
    height, width = image.shape
    img = image.copy()
    for i in range(height):
        for j in range(width):
            img[i, j] = (255 - image[i, j])
    return img


def erode_img(image, conv_core):
    """
    腐蚀
    :param image:
    :param conv_core: 卷积核:tuple
    :return:image
    """
    kernel = np.ones(conv_core, np.uint8)
    return cv2.erode(image, kernel, iterations=1)


def dilate_img(image, conv_core):
    """
    膨胀
    :param image:
    :param conv_core: 卷积核:tuple
    :return:image
    """
    kernel = np.ones(conv_core, np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


def opening_calc(image, conv_core):
    """
    开运算(腐蚀)
    :param image:
    :param conv_core: 卷积核:tuple
    :return:image
    """
    kernel = np.ones(conv_core, np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


def closing_calc(image, conv_core):
    """
    闭运算(膨胀)
    :param image:
    :param conv_core: 卷积核:tuple
    :return:image
    """
    kernel = np.ones(conv_core, np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)


def canny_contour(image, threshold1=128, threshold2=255):
    """
    canny边缘寻找
    :param image:
    :param threshold1:
    :param threshold2:
    :return:image
    """
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(img, threshold1, threshold2, cv2.THRESH_BINARY)


def get_sketch(src_img_path, conv_core=(2, 2), t1=128, t2=255):
    """
    返回线稿
    :param src_img_path:
    :param conv_core: 卷积核
    :param t1:
    :param t2:
    :return: mat
    """
    img = cv2.imread(src_img_path)
    img = canny_contour(img, t1, t2)
    img = dilate_img(img, conv_core)
    img = inverse_color(img)
    return img


IMG_PATH = "remu1.jpg"

if __name__ == '__main__':
    image = cv2.imread(IMG_PATH)
    image = canny_contour(image, 128, 255)
    image = dilate_img(image, (2, 2))
    image = inverse_color(image)

    cv2.imshow("Canny-Contour", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
