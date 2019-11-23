# ezutils
Utils to save your time on python coding

Life is short we use ezutils !

## Installing
```bash
pip install ezutils
```

## Using

### readlines:

readlines(filename: str, strip_newline: bool = True) 

#### params:
```txt
filename: the filename tobe read

strip_newline: strip the last space/newline


```
#### return lines readed from file

#### Example:

```python
    lines = readlines(brother_path('cfg.txt'))
    print(lines)
```


### writelines:

writelines(lines: List, filename, append_newline: bool = True) 

#### params:
```txt
lines: lines tobe written
filename: file tobe written
append_newline: add a newline to each line writtend
```
#### return None

Example:

```python
    lines = ['hello', 'ezflines']
    writelines(lines, brother_path('cfg.txt'))
```


### Demo

```python
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from ezutils.files import readlines, writelines


def brother_path(filename): return os.path.join(
    os.path.dirname(__file__), filename)


def read():
    lines1 = readlines(brother_path('cfg.txt'))
    print(f"lines1:{lines1}")
    '''
    lines1:['hello', 'ezflines']
    '''
    lines2 = readlines(brother_path('cfg.txt'), False)
    print(f"lines2:{lines2}")
    '''
    lines2:['hello\n', 'ezflines\n']
    '''


def write():
    lines = ['hello', 'ezflines']
    writelines(lines, brother_path('cfg.txt'))
    '''
    cfg.txt:
    hello
    ezflines

    '''
    writelines(lines, brother_path('cfg_oneline.txt'), False)
    '''
    cfg_oneline.txt:
    helloezflines
    '''


if __name__ == "__main__":
    write()
    read()

```

