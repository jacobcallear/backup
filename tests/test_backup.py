'''Test Backup class.'''
from pathlib import Path

import pytest

from backup import Backup

@pytest.mark.parametrize(
    'given_path',
    [
        'this path does not exist',
        Path('this path also does not exist')
    ]
)
def test_backup_init_not_exists(given_path):
    '''Check error raising for non-existent paths.'''
    with pytest.raises(FileNotFoundError):
        Backup(given_path)

@pytest.mark.parametrize(
    'given_path',
    [
        'this path does not exist',
        Path('this path also does not exist')
    ]
)
def test_backup_init_not_dir(monkeypatch, given_path):
    '''Check error raising for non-directories'''
    # Pretend path exists
    monkeypatch.setattr(Path, 'exists', lambda _: True)
    with pytest.raises(NotADirectoryError):
        Backup(given_path)

def test_backup_repr(monkeypatch):
    # Pretend path exists and is directory to allow initialisation
    monkeypatch.setattr(Path, 'is_dir', lambda _: True)
    monkeypatch.setattr(Path, 'exists', lambda _: True)
    # Get absolute path from current working directory to allow tests on
    # different platforms
    cwd = Path.cwd()
    given_path = cwd / 'example/string'
    expected_reprs = (
        f"Backup(path='{cwd}/example/string')",
        f"Backup(path='{cwd}\\example\\string')"
    )
    # Act, assert
    actual_repr = str(Backup(given_path))
    assert actual_repr in expected_reprs

if __name__ == '__main__':
    pytest.main()
