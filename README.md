# Backup

Backup folders using python.

## Demo

To copy files in *"my-videos"* to *"external-harddrive"*:

```python
from backup import Backup
my_backup = Backup('my-videos')
my_backup.copy_to('external-harddrive')
```

To only backup those files that haven't been backed up yet:

```python
my_backup.copy_missing_to('external-harddrive')
```
