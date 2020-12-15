# Backup

Backup folders using python.

## Demo

To copy files in *"my-videos"* to *"external-harddrive"*:

```python
from backup import Backup
my_backup = Backup('my-videos')
my_backup.copy_to('external-harddrive')
```

Instead of starting a backup from scratch, you can backup just those files that
haven't been backed up yet:

```python
my_backup.copy_missing_to('external-harddrive')
```

...or delete files from your backup if they have been deleted from the original
folder:

```python
my_backup.delete_missing_from('external-harddrive')
```
