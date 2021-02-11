# Backup

![Python tests and lints status](https://github.com/jacobcallear/backup/workflows/tests/badge.svg)

Backup folders using python.

## Demo

To copy files in *"folder-i-want-to-backup"* to *"external-harddrive"*:

```python
from backup import Backup

my_backup = Backup('folder-i-want-to-backup')
my_backup.copy_to('external-harddrive')
```

You can also just copy those files and folders that haven't been backed up yet:

```python
my_backup.copy_missing_to('external-harddrive')
```

...or delete files from your backup if they have been deleted from the original
folder:

```python
my_backup.delete_missing_from('external-harddrive')
```

## Installation

1. Ensure you have [Python](https://www.python.org/downloads/) >= 3.6 installed
2. [Download](https://github.com/jacobcallear/backup/archive/master.zip)
   and unzip this repository
3. In the terminal, `cd` into the `backup/backup/` folder
4. Run the following command:

   ```bash
   pip install .
   ```
