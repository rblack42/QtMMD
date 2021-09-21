import os
import subprocess
from QtMMD import __version__
import QtMMD

def test_app_version():
    assert QtMMD.version() == __version__

def test_python_venv():
    cwd = os.getcwd()
    pypath = subprocess.check_output(
                ['which', 'python'],
                universal_newlines=True
            )
    assert cwd in pypath
    print(cwd, pypath)

def test_openscad_version():
    process = subprocess.run(
                ['openscad', '--version'],
                stderr = subprocess.PIPE,
                universal_newlines=True
            )
    osc_version = process.stderr
    assert '2021' in osc_version
