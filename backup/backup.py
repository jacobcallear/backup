'''Backup folders.
TODO
- Add `copy_missing_to()` method
- Add `delete_missing_from()` method
- Add `to_json()` method
'''
import shutil
from pathlib import Path

class Backup:
    '''Describe a folder you want to back up.'''
    def __init__(self, folder):
        folder = Path(folder).resolve()
        if not folder.exists():
            raise FileNotFoundError(folder)
        if not folder.is_dir():
            raise NotADirectoryError(folder)
        self.path = Path(folder)

    def __repr__(self):
        return f"{type(self).__name__}(path='{self.path}')"

    def copy_to(self, folder):
        '''Copy all folders/files in backup to given folder.'''
        shutil.copytree(self.path, folder)
