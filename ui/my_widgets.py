from PySide6.QtWidgets import QWidget, QCheckBox
from PySide6.QtCore import Slot, Signal
from ui.ui_checkbox import Ui_Form

class SectionCheckbox(QWidget):
    sections_titles_checkbox_changed = Signal(int)
    def __init__(self, title: str, parent=None):
        super(SectionCheckbox, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.checkBox.setText(title)
        self.ui.checkBox.setChecked(True)