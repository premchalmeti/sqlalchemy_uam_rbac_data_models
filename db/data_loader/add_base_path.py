
__author__ = 'premkumar30'


def set_path():
    import os
    import sys

    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    sys.path.append(ROOT_DIR)
    print(ROOT_DIR, 'base path added')
