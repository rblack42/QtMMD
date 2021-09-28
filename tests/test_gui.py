import pytest
from QtMMD.Gui import Gui


def test_window_title(window):
	assert window.windowTitle() == "Math-Magik Designer"

def testWindowGeometry(window):
    """Check that the window width and height are set as declared."""
    assert window.width() == 640
    assert window.height() == 480

