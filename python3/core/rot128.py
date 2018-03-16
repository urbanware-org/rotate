#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ============================================================================
# ROTate - Encryption tool based on the ROT cipher
# ROT128 encryption/decryption core module
# Copyright (C) 2018 by Ralf Kilian
# Distributed under the MIT License (https://opensource.org/licenses/MIT)
#
# Website: http://www.urbanware.org
# GitHub: https://github.com/urbanware-org/rotate
# ============================================================================

__version__ = "3.0.6"

import os
from . import common
from . import paval as pv


def encrypt_file(file_input, file_output, buffer_size=4096, rot_value=128):
    """
        Encrypt a file using ROT128.
    """
    pv.path(file_input, "input", True, True)
    pv.path(file_output, "output", True, False)
    pv.intvalue(buffer_size, "buffer size", True, False, False)
    pv.intvalue(rot_value, "ROT", True, False, False)
    pv.compfile(file_input, "input", [[file_output, "output"]])

    buffer_size = int(buffer_size)
    rot_value = int(rot_value)
    file_input = os.path.abspath(file_input)
    file_output = os.path.abspath(file_output)

    fh_input = open(file_input, "rb")
    fh_output = open(file_output, "wb")

    file_size = common.get_file_size(file_input)
    byte_blocks = int(file_size / buffer_size)
    byte_remainder = file_size % buffer_size

    for block in range(byte_blocks):
        data_input = bytearray(b"" + fh_input.read(buffer_size))
        fh_output.write(__transform_bytes(True, data_input, rot_value))
    if byte_remainder > 0:
        data_input = bytearray(b"" + fh_input.read(byte_remainder))
        fh_output.write(__transform_bytes(True, data_input, rot_value))

    fh_input.close()
    fh_output.close()


def encrypt_string(string, rot_value):
    """
        Encrypt a string using ROT128.
    """
    pv.string(string, "string", True)
    pv.intvalue(rot_value, "ROT", True, False, False)

    return __transform_string(True, string, rot_value)


def decrypt_file(file_input, file_output, buffer_size=4096, rot_value=128):
    """
        Decrypt a file using ROT128.
    """
    pv.path(file_input, "input", True, True)
    pv.path(file_output, "output", True, False)
    pv.intvalue(buffer_size, "buffer size", True, False, False)
    pv.intvalue(rot_value, "ROT", True, False, False)
    pv.compfile(file_input, "input", [[file_output, "output"]])

    buffer_size = int(buffer_size)
    rot_value = int(rot_value)
    file_input = os.path.abspath(file_input)
    file_output = os.path.abspath(file_output)

    fh_input = open(file_input, "rb")
    fh_output = open(file_output, "wb")

    file_size = common.get_file_size(file_input)
    byte_blocks = int(file_size / buffer_size)
    byte_remainder = file_size % buffer_size

    for block in range(byte_blocks):
        data_input = bytearray(b"" + fh_input.read(buffer_size))
        fh_output.write(__transform_bytes(False, data_input, rot_value))
    if byte_remainder > 0:
        data_input = bytearray(b"" + fh_input.read(byte_remainder))
        fh_output.write(__transform_bytes(False, data_input, rot_value))

    fh_input.close()
    fh_output.close()


def decrypt_string(string, rot_value):
    """
        Decrypt a string using ROT128.
    """
    pv.string(string, "string", True)
    pv.intvalue(rot_value, "ROT", True, False, False)

    return __transform_string(False, string, rot_value)


def get_version():
    """
        Return the version of this module.
    """
    return __version__


def __transform_bytes(encrypt, data_input, rot_value):
    """
        Core method to manipulate bytes.
    """
    data_output = bytearray(b"")

    for byte in data_input:
        if encrypt:
            data_output.append(((byte + rot_value) % 256))
        else:
            data_output.append(((byte - rot_value) % 256))

    return data_output


def __transform_string(encrypt, string, rot_value):
    """
        Core method to manipulate a string.
    """
    output = ""

    for char in string:
        if encrypt:
            output += chr(((ord(char) + rot_value) % 256))
        else:
            output += chr(((ord(char) + rot_value) % 256))

    return output

# EOF
