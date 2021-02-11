'''Backup folders.
'''
import shutil
from collections import namedtuple
from os import walk
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

    def find_missing_from(self, folder):
        '''Find files from `self` to `folder` if they're not there already.'''
        paste_folder = Path(folder)
        if not paste_folder.exists():
            raise FileNotFoundError(paste_folder)
        MissingPath = namedtuple('MissingPath', 'path_to_copy paste_path is_file')
        # Look for folders / files in backup that are not in `folder`
        for folder, subfolders, file_names in walk(self.path):
            folder = Path(folder)
            expected_folder_path = paste_folder / folder.relative_to(self.path)
            if not expected_folder_path.exists():
                # Copy folder across if it's not there already
                yield MissingPath(folder, expected_folder_path, is_file=False)
                # Don't look at contents of this folder as it is already copied
                subfolders[:] = []
                continue
            # Copy files across if they're not there already
            for file_name in file_names:
                expected_file_path = expected_folder_path / file_name
                if not expected_file_path.exists():
                    file_path = folder / file_name
                    yield MissingPath(file_path, expected_file_path, is_file=True)

    def copy_missing_to(self, folder, interactive=True):
        '''Copy files in `self` to `folder` that are not there already.'''
        for missing_path in self.find_missing_from(folder):
            path_to_copy, paste_path, is_file = missing_path
            print(f'Copying "{path_to_copy}"')
            print(f'     to "{paste_path}"')
            if interactive and input('Continue (y/n)?').strip().lower() != 'y':
                continue
            if is_file:
                try:
                    shutil.copy(path_to_copy, paste_path)
                except OSError:
                    print('FAILED TO COPY previous file')
                    paste_path.unlink()
            else:
                try:
                    shutil.copytree(path_to_copy, paste_path)
                except OSError:
                    print('FAILED TO COPY previous folder')

    def delete_missing_from(self, folder, interactive=True):
        '''Delete files in `folder` that are not in `self`.'''
        folder = Backup(folder)
        for path in folder.find_missing_from(self.path):
            path_to_delete, _, is_file = path
            print(f'Deleting "{path_to_delete}"')
            if interactive and input('Continue (y/n)?').strip().lower() != 'y':
                continue
            if is_file:
                path_to_delete.unlink()
            else:
                shutil.rmtree(path_to_delete)
