from skimage import data
from skimage.feature import canny

from skimage.viewer import ImageViewer
from skimage.viewer.widgets import Slider
from skimage.viewer.widgets.history import SaveButtons
from skimage.viewer.plugins.overlayplugin import OverlayPlugin
from skimage.viewer.plugins.plotplugin import PlotPlugin
from skimage.viewer.plugins.labelplugin import LabelPainter
from skimage.viewer.widgets import CheckBox
from skimage.viewer.widgets import Button
from skimage.viewer.widgets import ComboBox,Text,BaseWidget,OKCancelButtons,SaveButtons

def printf():
    print('daf')
    return


image = data.camera()

# You can create a UI for a filter just by passing a filter function...
# plugin = OverlayPlugin(image_filter=canny)
plugin = OverlayPlugin()
# plugin = LabelPainter()
# plugin = PlotPlugin()
# ... and adding widgets to adjust parameter values.
plugin += Slider('sigma', 0, 5,value_type='int',value=3) # name, low=0.0, high=1.0, value=None, value_type='float','int',orientation='horizontal'/'vertical'
# plugin += Button('name',callback=printf) # name, callback
plugin += ComboBox('Combo',['123','312','rqr'],callback=printf())  #name, items, ptype='kwarg', callback=None
plugin += Text('text',text='printtext') #name=None, text=''
plugin += SaveButtons()
plugin += CheckBox('check',alignment='left')  # name, value=False, alignment='center'/'left'/'right', ptype='kwarg',callback=None
# ... and we can also add buttons to save the overlay:
# plugin += SaveButtons(name='Save overlay to:')

# Finally, attach the plugin to an image viewer.
viewer = ImageViewer(image)
viewer += plugin
canny_edges = viewer.show()[0][0]




