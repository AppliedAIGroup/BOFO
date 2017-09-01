from skimage.io import imread
from skimage.color import rgb2gray

def gray(im, weight=0.1, eps=2.e-4, n_iter_max=200,
                         multichannel=False):
    #
    # im_type = im.dtype
    # if not im_type.kind == 'f':
    #     im = img_as_float(im)

    if multichannel:
        out = imread('/Users/zhizhao/PycharmProjects/BOFO/Devlog/test.jpg')
    else:
        out = rgb2gray(im)
    return out
