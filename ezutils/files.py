import os
from typing import List


def readlines(filename: str, strip_newline: bool = True) -> List:
    f = open(os.path.abspath(filename), 'r')
    lines = f.readlines()
    f.close()
    if not strip_newline:
        return lines

    new_lines = []
    for line in lines:
        new_lines.append(line.rstrip())
    return new_lines


def writelines(lines: List, filename, append_newline: bool = True) -> None:
    newlines = []
    for line in lines:
        if append_newline and not line.endswith('\n'):
            newlines.append(f"{line}\n")
        else:
            newlines.append(line)

    f = open(filename, 'w')
    f.writelines(newlines)
    f.close()
