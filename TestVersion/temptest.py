from skimage import data
from skimage.restoration import denoise_tv_chambolle
from skimage.util import img_as_float
from numpy import random, clip
from  skimage.color import rgb2gray


from skimage.viewer import ImageViewer
from skimage.viewer.widgets import (Slider, CheckBox, OKCancelButtons,
                                    SaveButtons)
from skimage.viewer.plugins.base import Plugin
from skimage.filters import gabor



image = img_as_float(data.chelsea())
image = rgb2gray(image)
sigma = 30/255.

image = image + random.normal(loc=0, scale=sigma, size=image.shape)
image = clip(image, 0, 1)
viewer = ImageViewer(image)

plugin = Plugin(image_filter=gabor)    #只要返回的是ndarry，就可以自动刷新？
plugin += Slider('bandwidth', 1,2, value=1, value_type='float') #slider的选项名称跟filter的名称一样就可以调整参数？
plugin += Slider('frequency', 0.1,0.6, value=0.1, value_type='float') #slider的选项名称跟filter的名称一样就可以调整参数？
# plugin += Slider('n_iter_max', 1, 100, value=20, value_type='int')
# plugin += CheckBox('multichannel', value=False)
# plugin += SaveButtons()
# plugin += OKCancelButtons()

viewer += plugin
viewer.show()