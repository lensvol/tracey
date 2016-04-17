# -*- coding: utf-8 -*-

import sys

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import Terminal256Formatter


def processor():
    traceback_follows = False

    line = sys.stdin.readline()
    tb_lines = []

    while line:
        if line.startswith('Traceback (most recent call last)'):
            traceback_follows = True
        elif traceback_follows and not line.startswith('  '):
            tb_lines.append(line)
            traceback_follows = False

        if traceback_follows:
            tb_lines.append(line)
        elif tb_lines:
            print highlight(
                ''.join(tb_lines),
                get_lexer_by_name('pytb'),
                Terminal256Formatter(),
            ),
            tb_lines = []
        else:
            print line,

        line = sys.stdin.readline()


if __name__ == '__main__':
    processor()
