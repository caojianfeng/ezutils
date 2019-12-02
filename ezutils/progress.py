#!/usr/bin/env python3
import sys
import time


# for x in range(0, 100):
#     sys.stdout.write("%s\r" % (str(x) + "%"))
#     time.sleep(0.1)
# [Python如何输出带颜色的文字方法](https://www.cnblogs.com/easypython/p/9084426.html)
def print_progress(msg, current, max, max_width=60):
    padding = ' '
    if len(msg) > max_width:
        msg = f"{msg[0:max_width-3]}..."
    elif len(msg) < max_width:
        msg = f"{msg}{padding:{max_width-len(msg)}}"

    color_head = '\033[37;42m'
    color_div = '\033[37;44m'
    color_end = '\033[0m'

    rate = float(current)/float(max)
    progress = 100.0*rate
    done_width = int(max_width*rate)
    progress_str = "[ \033[32mDONE\033[0m ]" if progress == 100.0 else f"[{progress:05.02f}%]"

    sys.stdout.write(color_head)
    sys.stdout.write(f"{msg[0:done_width]}")
    sys.stdout.write(color_div)
    sys.stdout.write(f"{msg[done_width:]}")
    sys.stdout.write(color_end)

    sys.stdout.write(f"{progress_str}\r")
    if progress == 100.0:
        sys.stdout.write('\n')

    sys.stdout.flush()


if __name__ == '__main__':
    max = 100
    for i in range(max + 1):
        print_progress(
            "TODO：解决中文长度问题1223123.csv            (%d)" % i, i, max)
        # print_progress(
        #     " ", i, max, 100)
        time.sleep(0.01)
    # print('\033[0m')
