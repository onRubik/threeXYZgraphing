import platform
from pathlib import Path
import os


class dataIntegrity:
    def imgFolder(self):
        os_type = platform.system()
        if os_type == 'Windows':
            project_path = os.path.dirname(__file__)
        elif os_type == 'Linux':
            project_path = os.path.dirname(os.path.abspath(__file__))

        return project_path, os_type