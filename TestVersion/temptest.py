from skimage import data
from skimage.filters import rank
from skimage.filters import threshold_isodata
from skimage.morphology import disk

from skimage.viewer import CollectionViewer
from skimage.viewer.widgets import Slider
from skimage.viewer.plugins.base import Plugin


# Wrap autolevel function to make the disk size a filter argument.
def autolevel(image, nbins):
    return threshold_isodata(image)
    return rank.autolevel(image, nbins)


[row,:, 0]

img_collection = [data.camera(), data.coins(), data.text()]

plugin = Plugin(image_filter=autolevel)
plugin += Slider('nbins', 1, 255, value_type='int')
# plugin.name = "Autolevel"

viewer = CollectionViewer(img_collection)
viewer += plugin

viewer.show()
