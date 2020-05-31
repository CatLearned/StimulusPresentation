#!C:\Users\Vovan\PycharmProjects\StimulsPresentation\venv\Scripts\pythonw.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'PsychoPy==2020.1.2','gui_scripts','psychopy'
__requires__ = 'PsychoPy==2020.1.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('PsychoPy==2020.1.2', 'gui_scripts', 'psychopy')()
    )
