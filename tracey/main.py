# -*- coding: utf-8 -*-

import argparse
import sys

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import Terminal256Formatter
from pygments.styles import get_all_styles


def processor(specific_style=None):
    traceback_follows = False

    line = sys.stdin.readline()
    tb_lines = []

    lexer = get_lexer_by_name('pytb')
    formatter = Terminal256Formatter(style=specific_style or 'monokai')

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
                lexer,
                formatter,
            ),
            tb_lines = []
        else:
            print line,

        line = sys.stdin.readline()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    available_styles = ', '.join(get_all_styles())
    parser.add_argument(
        '--style',
        help='Use specified pygments style (%s)' % available_styles,
    )
    args = parser.parse_args()

    if args.style not in available_styles:
        print 'Error: unknown style "%s"' % args.style
        exit(-1)

    processor(specific_style=args.style)
