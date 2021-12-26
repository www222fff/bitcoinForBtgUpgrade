#!/usr/bin/env python3
# Copyright (c) 2012-2018 The Bitcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
'''
Generate valid and invalid base58/bech32(m) address and private key test vectors.

Usage:
    PYTHONPATH=../../test/functional/test_framework ./gen_key_io_test_vectors.py valid 70 > ../../src/test/data/key_io_valid.json
    PYTHONPATH=../../test/functional/test_framework ./gen_key_io_test_vectors.py invalid 70 > ../../src/test/data/key_io_invalid.json
'''
# 2012 Wladimir J. van der Laan
# Released under MIT License
import os
from itertools import islice
from base58 import b58encode_chk, b58decode_chk
import random


if __name__ == '__main__':

    raw = b58decode_chk('3B5fQsEXEaV8v6U3ejYc8XaKXAkyQj2MjV')
    raw[0] = 'G'
    b58encode_chk(raw)
    sys.stdout.write(raw)
