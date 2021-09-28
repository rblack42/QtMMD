import pytest
from QtMMD.Gui import Gui


@pytest.fixture
def window(qtbot):
	new_window = Gui()
	qtbot.addWidget(new_window)
	new_window.show()
	return new_window

@pytest.fixture
def settings(qtbot):
    settings = QtCore.QSettings('Math-Magick', 'Designer-test')
    config_data_dir = "config"

