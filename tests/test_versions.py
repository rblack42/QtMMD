import os
import pytest
import subprocess
from QtMMD import __version__
import QtMMD

def test_app_version():
    assert QtMMD.version() == __version__

def test_openscad_version():
    process = subprocess.run(
                ['openscad', '--version'],
                stderr = subprocess.PIPE,
                universal_newlines=True
            )
    osc_version = process.stderr
    assert 'version 20' in osc_version
