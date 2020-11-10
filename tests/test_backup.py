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
    # 
    given_path = 'example/string'
    expected_reprs = (
        "Backup(path='example/string')",
        "Backup(path='example\\string')"
    )
    actual_repr = str(Backup(given_path))
    assert actual_repr in expected_reprs

if __name__ == '__main__':
    pytest.main()
