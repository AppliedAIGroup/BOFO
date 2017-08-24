


from time import sleep

import picamera, leancloud, logging
import leancloud

#### configuration ####
# leancloud
leancloud_APPID = 'hHcG1lVaaroON4QtEi1seRxb-gzGzoHsz'
leancloud_APPKey = 'SbR79lNTiRSM8bAm5D7JuD3E'
# camera
camera_resolution = '1024*768'
# loop
sleep_time = 60  # seconds



def configure_camera():
    picamera.PiCamera.resolution = (640, 480)
    picamera.PiCamera.awb_mode = 'off'


def get_camera_image():
    with picamera.PiCamera() as camera:
        # camera.resolution = (1024,768)
        # camera.awb_mode = 'off'
        camera.capture('zero.jpg')


def init_leancloud(leancloudID, leancloudAPP):
    leancloud.init(app_id=leancloud_APPID, app_key=leancloud_APPKey)
    # logging.basicConfig(level=logging.DEBUG)


def send_result(value):
    Object = leancloud.Object.extend('fleet')
    test_object = Object()
    test_object.set('objectId', 'Tim')
    test_object.set('GaugeIP', IPaddress)
    test_object.save()

    TestObject = leancloud.Object.extend('fleet')
    test_object = TestObject()
    test_object = TestObject.creat_without_data('599e44ef8d6d8100580f8279')
    test_object.set('cont', value)
    test_object.save()


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
    from pylab import plot

    from skimage.draw import (line, polygon, circle,
                              circle_perimeter,
                              ellipse, ellipse_perimeter,
                              bezier_curve)

    #################
    # configuration #
    #################

    file_name = "C:/Users/502640129/Desktop/Boo/bofo_algorithm/image_small/test20/test03_31.jpg"
    # file_name = "test_002.jpg"
    rescale_ratio = 0.5
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


    # calculate the gray
    img = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3
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

    print(grayList)
    print(grayList[0])
    # print(np.where(np.min(grayList)))
    print(grayList[535])

    re = np.where(grayList == np.min(grayList))
    print(re)
    re = re[0][0] / 2 + 51
    # print(re[0][0])
    angle = re / 180 * pi

    # draw a line
    circle_center_xx = int(circle_center_x + diameter * cos(angle))
    circle_center_yy = int(circle_center_y - diameter * sin(angle))
    rr, cc = line(circle_center_x, circle_center_y, circle_center_xx, circle_center_yy)
    img[rr, cc] = 255  # 第三个参数是通道，0,1,2对应RBG

    # circle
    rr, cc = circle_perimeter(circle_center_x, circle_center_y, ID)
    img[rr, cc] = 1

    rr, cc = circle_perimeter(circle_center_x, circle_center_y, OD)
    img[rr, cc] = 1

    #

    # xxx = (circle_center_y, circle_center_x, circle_center_yy, circle_center_xx)
    # rr, cc = line(circle_center_y, circle_center_x, circle_center_yy, circle_center_xx)
    # image[rr, cc] = 255  # 第三个参数是通道，0,1,2对应RGB
    #
    # circle_center_xx, circle_center_yy = int(circle_center_x - diameter * sin(end_angle)), int(
    #     circle_center_y - diameter * cos(
    #         end_angle))
    # rr, cc = line(circle_center_y, circle_center_x, circle_center_yy, circle_center_xx)
    # image[rr, cc] = 255  # 第三个参数是通道，0,1,2对应RGB

    viewer = ImageViewer(img)
    viewer.show()


### main loop ###
init_leancloud()
configure_camera()
cont = 0

# while True:
#     cont = cont + 1
#
#     sleep(sleep_time)
#     get_camera_image()
#     calculate_image()
#     send_result(cont)


    sleep(sleep_time)
    get_camera_image()
    calculate_image()
    send_result(cont)