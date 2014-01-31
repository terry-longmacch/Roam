from roam.editorwidgets.textwidget import TextWidget, TextBlockWidget

from configmanager.editorwidgets.core import ConfigWidget
from configmanager.editorwidgets.uifiles.textwidget_config import Ui_Form


class TextWidgetConfig(Ui_Form, ConfigWidget):
    description = "Free text field"
    widget = TextWidget

    def __init__(self, parent=None):
        super(TextWidgetConfig, self).__init__(parent)
        self.setupUi(self)


class TextBlockWidgetConfig(TextWidgetConfig):
    description = "Large free text field"
    widget = TextBlockWidget

    def __init__(self, parent=None):
        super(TextBlockWidgetConfig, self).__init__(parent)
