"""
power test
"""

# import picamera
import leancloud, logging
from time import sleep
from leancloud import LeanCloudError

# import traceback


# --------------configuration --------------#
# leancloud
leancloud_APPID = 'hHcG1lVaaroON4QtEi1seRxb-gzGzoHsz'
leancloud_APPKey = 'SbR79lNTiRSM8bAm5D7JuD3E'
# camera
camera_resolution = '640*480'  # 640*480,1024*768
# loop
sleep_time = 1  # seconds


# --------------init----------------#


# -------------method ------------#
def configure_camera():
    picamera.PiCamera.resolution = (640, 480)
    picamera.PiCamera.awb_mode = 'off'


def get_camera_image(name):
    with picamera.PiCamera() as camera:
        # camera.resolution = (1024,768)
        # camera.awb_mode = 'off'
        camera.capture('pizero' + str(name) + '.jpg')


def init_leancloud(leancloudID, leancloudAPP):
    leancloud.init(app_id=leancloud_APPID, app_key=leancloud_APPKey)
    logging.basicConfig(level=logging.DEBUG)


def send_result(value):
    TestObject = leancloud.Object.extend('fleet')
    test_object = TestObject.create_without_data('59a61dc58d6d810057fdd202')
    test_object.set('cont', str(value))
    try:
        test_object.save()
        print('save success')
    except Exception as e:
        print(Exception,e)


        # f = open("/Users/zhizhao/Desktop/log.txt", 'a')
        # traceback.print_exc(file=f)
        # f.flush()
        # f.close()


def calculate_image():
    """
    ==================================
    ``Viewer for BOFO project`` with some plugin
    ==================================
    A viewer for BOFO project for viewing collections of images with the
    `detecting algorithm` and a slider plugin.
    """

    from skimage import io
    from skimage.viewer import ImageViewer
    from skimage.transform import (rescale, resize)
    from math import (sin, cos, pi)
    import numpy as np
    from skimage.draw import line

    #################
    # configuration #
    #################

    file_name = "C:/Users/502640129/Desktop/Boo/bofo_algorithm/image_small/test20/test03_31.jpg"
    # file_name = "pizero1.jpg"
    rescale_ratio = 1
    circle_center_y = 200
    circle_center_x = 227
    maxValue = 16
    start_angle = 51  # degree
    end_angle = 319  # degree
    diameter = 180

    valuePerAngle = maxValue / (end_angle - start_angle)
    start_angle = start_angle / 180 * pi  # degree
    end_angle = end_angle / 180 * pi  # degree

    ID = 10
    OD = 180

    #############
    # main loop #
    #############

    # read the image
    img = io.imread(file_name, True)  # 'True' means gray
    img = rescale(img, rescale_ratio, mode='reflect')

    # calculate the gray
    # img = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3
    # img[:, :] = 1

    grayList = []

    for angle in range(51 * 2, 319 * 2, 1):
        # 求权重补偿值
        weightAngle = angle / 2
        if (int(weightAngle / 45) % 2) == 0:

            weightAngle = weightAngle - int(weightAngle / 45) * 45
        else:
            weightAngle = (weightAngle - (int(weightAngle / 45) - 1) * 45) - (weightAngle - int(
                weightAngle / 45) * 45) * 2

        # 求沿着画的这条线段上所有灰度值的和
        angle = float(angle / 180 * pi) / 2
        xx = int(circle_center_x + ID * cos(angle))
        yy = int(circle_center_y - ID * sin(angle))
        xxx = int(circle_center_x + OD * cos(angle))
        yyy = int(circle_center_y - OD * sin(angle))
        rr, cc = line(xx, yy, xxx, yyy)
        temp = np.sum(img[rr, cc])

        # 进行权重补偿
        temp = temp * (1 / cos(weightAngle / 180 * pi))
        grayList = grayList + [temp]

    # print(grayList)
    # print(grayList[0])
    # print(np.where(np.min(grayList)))
    # print(grayList[535])

    re = np.where(grayList == np.min(grayList))
    # print(re)
    re = re[0][0] / 2 + 51
    # print(re[0][0])
    angle = re / 180 * pi
    # return calculate_result


# --------------main loop ------------#
if __name__ == '__main__':
    init_leancloud(leancloud_APPID, leancloud_APPKey)
    # configure_camera()
    cont = 0
    while True:
        cont = cont + 1
        sleep(sleep_time)
        # get_camera_image(cont)
        # calculate_image()
        send_result(cont)
        print(cont)
