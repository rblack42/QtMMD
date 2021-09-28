import os
from PyQt5.QtCore import QSettings, QStandardPaths, QSize, QPoint


class Settings(object):

    def __init__(self):
        self.settings = QSettings("Math-Magik", "Designer")
        self.doc_path = QStandardPaths.writableLocation(
                    QStandardPaths.DocumentsLocation)
        self.default_model_path = os.path.join(self.doc_path, 'MMdesigner')
        self.load_settings()

    def load_settings(self):
        self.size = self.settings.value("main_window_size", QSize(640, 480))
        self.pos = self.settings.value("main_window_pos", QPoint(100,100))
        self.model_path = self.settings.value('model_path',
                self.default_model_path)
        if not os.path.isdir(self.model_path):
            os.makedirs(self.model_path)

    def write_settings(self):
        self.settings.setValue("main_window_size", self.size())
        self.settings.setValue("main_window_pos", self.pos())
        self.settings.setValue("model_path", self.get_model_path())


    def get_settings_filepath(self):
        return self.settings.fileName()

    def get_doc_path(self):
        return self.doc_path

    def get_size(self):
        return self.size

    def get_pos(self):
        return self.pos

    def get_model_path(self):
        return self.model_path


if __name__ == '__main__':
    s = Settings()
    s.load_settings()
    print(s.get_settings_filepath())
    print(s.get_doc_path())
    print(s.get_size())
    print(s.get_pos())
    print(s.get_model_path())
    s.write_settings()


