# -*- coding: utf-8 -*-
"""
Created on Oct 03, 2024

@author: emmet
"""

import sys
import os

def vaildate_commands(option: str, file: str):
    valid_options = ["-d", ]
    if option in valid_options and os.path.isfile(file):
        return True
    else:
        return False


def display_image(*args):
    pass


if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise
