#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from supersonic.ext import Extension
from supersonic.utils import UNICODE_SUPPORT

CHARSET_HASH = ("#")
CHARSET_NUMERIC = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "#")
CHARSET_ARROW = (">", "=")
CHARSET_UNICODE_BLOCK = ("█")
CHARSET_UNICODE_SMOOTH = ("▏", "▎", "▍", "▌", "▋", "▊", "▉", "█")
CHARSET_ROCKET = ("🚀", ">")
CHARSET_DEFAULT = CHARSET_UNICODE_SMOOTH if UNICODE_SUPPORT else CHARSET_NUMERIC

class Bar(Extension):
    CHARSET_DEFAULT = CHARSET_DEFAULT
    CHARSET_HASH = CHARSET_HASH
    CHARSET_NUMERIC = CHARSET_NUMERIC
    CHARSET_ARROW = CHARSET_ARROW
    CHARSET_UNICODE_BLOCK = CHARSET_UNICODE_BLOCK
    CHARSET_UNICODE_SMOOTH = CHARSET_UNICODE_SMOOTH
    CHARSET_ROCKET = CHARSET_ROCKET
    def __init__(self, progress_charset=CHARSET_DEFAULT, placeholder=" ", length=20):
        super(Bar, self).__init__()
        self.progress_charset = progress_charset
        self.placeholder = placeholder
        self.length = length
    
    def __len__(self):
        return self.length

    def stat_update(self, current):
        decimal = float(current) / float(self.total)
        blocks_to_fill = decimal * self.length * len(self.progress_charset)
        blocks_to_fill, last_block = divmod(blocks_to_fill, len(self.progress_charset))
        blocks_to_fill = int(blocks_to_fill)
        last_block = int(last_block) - 1
        blocks_not_to_fill = self.length - blocks_to_fill - (0 if last_block == -1 else 1)
        update = blocks_to_fill * self.progress_charset[-1]
        if last_block != -1:
            update += self.progress_charset[last_block]
        update += self.placeholder * blocks_not_to_fill
        return update
