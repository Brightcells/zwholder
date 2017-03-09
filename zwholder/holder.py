# -*- coding: utf-8 -*-


import random

from .compat import range


class Placeholder(object):
    def __init__(self):
        # https://en.wikipedia.org/wiki/Zero_width
        self.holders = ['&#8203;', '&#8204;', '&zwnj;', '&#8205;', '&zwj;', '&#8288;']

    def strholder(self, s, n):
        l = list(s)
        [l.insert(random.randint(0, len(l)), random.choice(self.holders)) for _ in range(n)]
        return ''.join(l)


_global_instance = Placeholder()
strholder = _global_instance.strholder