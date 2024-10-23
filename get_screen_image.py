from PIL import ImageGrab


def get_image(point1, point2):
    return ImageGrab.grab(bbox=[min(point1[0], point2[0]),
                                min(point1[1], point2[1]),
                                max(point1[0], point2[0]),
                                max(point1[1], point2[1])])