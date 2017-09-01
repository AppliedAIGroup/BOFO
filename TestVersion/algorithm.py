"""
main algorithm for BOFO project 
calculation: skimage
visualization: skimage.viewer , pylab
"""

from skimage import io

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
floder_path = "/Users/zhizhao/PycharmProjects/BOFO/TestVersion/image"
file_name = '_DSF0282.jpg'
file_path = floder_path + '/' + file_name
rescale_ratio = 0.2
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
img = io.imread(file_path)  # 'True' means gray
# calculate the gray
img_gray = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3
# image_rescale
# img = rescale(img, rescale_ratio, mode='reflect')  # rescale *0.2

# 先使用image_viewer来读取多张图片


viewer = ImageViewer(img)
viewer.show()






#
# # circle
# rr, cc = circle_perimeter(circle_center_x, circle_center_y, 15)
# img[rr, cc, :] = (1, 0, 0)
#

#
# # start line
# circle_center_xx = int(circle_center_x + diameter * cos(start_angle))
# circle_center_yy = int(circle_center_y - diameter * sin(start_angle))
#
# rr, cc = circle_perimeter(circle_center_xx, circle_center_yy, 15)
# img[rr, cc, :] = (1, 0, 0)
#
# rr, cc = line(circle_center_x, circle_center_y, circle_center_xx, circle_center_yy)
# img[rr, cc, 1] = 255  # 第三个参数是通道，0,1,2对应RBG
#
# # end line
# circle_center_xx = int(circle_center_x + diameter * cos(end_angle))
# circle_center_yy = int(circle_center_y - diameter * sin(end_angle))
# rr, cc = circle_perimeter(circle_center_xx, circle_center_yy, 15)
# img[rr, cc, :] = (1, 0, 0)
# rr, cc = line(circle_center_x, circle_center_y, circle_center_xx, circle_center_yy)
# img[rr, cc, 1] = 255  # 第三个参数是通道，0,1,2对应RBG
#
# # middle line
# angle = (end_angle - start_angle) / 2 + start_angle
# circle_center_xx = int(circle_center_x + diameter * cos(angle))
# circle_center_yy = int(circle_center_y - diameter * sin(angle))
# rr, cc = line(circle_center_x, circle_center_y, circle_center_xx, circle_center_yy)
# img[rr, cc, 1] = 255  # 第三个参数是通道，0,1,2对应RBG

#
#
# grayList = []
#
# for angle in range(51 * 2, 319 * 2, 1):
#     # 求权重补偿值
#     weightAngle = angle / 2
#     if (int(weightAngle / 45) % 2) == 0:
#
#         weightAngle = weightAngle - int(weightAngle / 45) * 45
#     else:
#         weightAngle = (weightAngle - (int(weightAngle / 45) - 1) * 45) - (weightAngle - int(weightAngle / 45) * 45) * 2
#
#     # 求沿着画的这条线段上所有灰度值的和
#     angle = float(angle / 180 * pi) / 2
#     xx = int(circle_center_x + ID * cos(angle))
#     yy = int(circle_center_y - ID * sin(angle))
#     xxx = int(circle_center_x + OD * cos(angle))
#     yyy = int(circle_center_y - OD * sin(angle))
#     rr, cc = line(xx, yy, xxx, yyy)
#     temp = np.sum(img[rr, cc])
#
#     # 进行权重补偿
#     temp = temp * (1 / cos(weightAngle/180*pi))
#     grayList = grayList + [temp]
#
# print(grayList)
# print(grayList[0])
# # print(np.where(np.min(grayList)))
# print(grayList[535])
#
# re = np.where(grayList == np.min(grayList))
# print(re)
# re = re[0][0] / 2 + 51
# # print(re[0][0])
# angle = re / 180 * pi
#
# # draw a line
# circle_center_xx = int(circle_center_x + diameter * cos(angle))
# circle_center_yy = int(circle_center_y - diameter * sin(angle))
# rr, cc = line(circle_center_x, circle_center_y, circle_center_xx, circle_center_yy)
# img[rr, cc] = 255  # 第三个参数是通道，0,1,2对应RBG
#
# # circle
# rr, cc = circle_perimeter(circle_center_x, circle_center_y, ID)
# img[rr, cc] = 1
#
# rr, cc = circle_perimeter(circle_center_x, circle_center_y, OD)
# img[rr, cc] = 1

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

#
#
#
# viewer = ImageViewer(img)
# viewer.show()
