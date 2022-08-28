import os
from threading import Thread
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QVBoxLayout, QLabel
from ui.main_ui import Ui_MainWindow
from ui.my_widgets import SectionCheckbox
from PySide6.QtCore import Slot
import sys
from sys import platform
from site_parser import Parser


class CustomDialog(QDialog):
    def __init__(self, title, text):
        super().__init__()

        self.setWindowTitle(title)

        btn = QDialogButtonBox.Ok
        self.button_box = QDialogButtonBox(btn)
        self.button_box.setCenterButtons(True)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        message = QLabel(text)
        self.layout.addWidget(message)
        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)


class Window(QMainWindow, ):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)
        self.ui.update_section_list_btn.clicked.connect(
            self.parse_sections_titles)
        self.ui.start_parsing_btn.clicked.connect(self.start_parsing)
        self.ui.open_folder_button.clicked.connect(self.open_result_folder)
        self.ui.fast_loading_checkbox.stateChanged.connect(
            lambda a: self.check_fast_loading_checkbox(self.ui.fast_loading_checkbox))
        parser.model.sections_titles_changed.connect(self.add_sections_titles)
        parser.model.parsing_completed.connect(self.parsing_completed_dialog)

    def parsing_completed_dialog(self):
        dialog = CustomDialog(
            'Parsing completed', f'Number of saved photos: {parser.get_saved_photos_count()}')
        dialog.exec()

    @Slot()
    def check_fast_loading_checkbox(self, checkbox):
        if checkbox.isChecked():
            parser.set_fast_photos_loading(True)
        else:
            parser.set_fast_photos_loading(False)

    @Slot()
    def parse_sections_titles(self):
        self.clear_section_layout()
        parser.set_url(self.ui.link_field.text())
        Thread(target=parser.parse_sections_titles, daemon=True).start()

    def add_sections_titles(self):
        sections_titles = parser.get_sections_titles()
        for section_title in sections_titles:
            widget = SectionCheckbox(section_title)
            self.ui.section_layout.addWidget(widget)
        dialog = CustomDialog(
            'Sections titles parsing completed', f'Found {len(sections_titles)} sections')
        dialog.exec()

    def clear_section_layout(self):
        while self.ui.section_layout.count() > 0:
            checkbox = self.ui.section_layout.takeAt(0)
            checkbox.widget().deleteLater()

    def start_parsing(self):
        section_titles_dictionary = {}
        for i in range(self.ui.section_layout.count()):
            checkbox = self.ui.section_layout.itemAt(i).widget().ui.checkBox
            section_titles_dictionary[checkbox.text()] = checkbox.isChecked()
        parser.set_sections_titles_dictionary(section_titles_dictionary)
        parser.set_url(self.ui.link_field.text())
        Thread(target=parser.main, daemon=True).start()

    @Slot()
    def open_result_folder(self):
        if platform == 'linux' or platform == 'linux2':
            os.system('xdg-open "%s"' % './Result')
        if platform == 'win32':
            if os.path.exists('Result'):
                os.startfile('Result')
            else:
                os.mkdir('Result')
                os.startfile('Result')


if __name__ == '__main__':
    app = QApplication()
    parser = Parser()
    window = Window()
    window.setWindowTitle('Yupoo Parser')
    window.show()
    sys.exit(app.exec())
