import os
from .about import *
from .mrmr import hash, hash_unicode, hash_bytes
from .mrmr import hash_64, hash_unicode_64, hash_bytes_64


def get_include():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "include")
