#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# ============================================================================
# ROTate - Encryption tool based on the ROT cipher
# Cracker core module
# Copyright (C) 2018 by Ralf Kilian
# Distributed under the MIT License (https://opensource.org/licenses/MIT)
#
# GitHub: https://github.com/urbanware-org/rotate
# GitLab: https://gitlab.com/urbanware-org/rotate
# ============================================================================

__version__ = "3.0.6"

import os
import paval as pv
import rot13
import rot47
import rot128
import string as st
import sys

from datetime import datetime as dt


def brute_force(string, file_output, method=None, int_ordinals=False,
                non_printable=False, limit=True):
    """
        Brute-force the given string to find out which ROT variant and
        rotation value was used to encrypt.
    """
    pv.path(file_output, "output", True, False)
    pv.string(string, "string to decrypt", True)
    file_output = os.path.abspath(file_output)

    if method is None:
        method = "All"
    else:
        method = method.upper()
        pv.compstr(method, "method", ["ROT13", "ROT47", "ROT128"])

    list_values_rot13 = []
    list_values_rot47 = []
    list_values_rot128 = []
    timestamp = str(dt.now())
    output = "\r\n" + "=" * 78 + \
             "\r\nFile type:           ROTate Cracker output file" \
             "\r\n" + "-" * 78 + \
             "\r\nOutput file name:    " + file_output + \
             "\r\nString to decrypt:   " + string + \
             "\r\nMethods used:        " + method + \
             "\r\n" + "-" * 78 + \
             "\r\nTimestamp:           " + timestamp[:-7] + \
             "\r\nROTate version:      " + get_version() + \
             "\r\n" + "=" * 78 + "\r\n\r\n"

    if method == "All" or method == "ROT13":
        list_values_rot13 = \
            __get_values_rot13(string, int_ordinals, non_printable, limit)
    if method == "All" or method == "ROT47":
        list_values_rot47 = \
            __get_values_rot47(string, int_ordinals, non_printable, limit)
    if method == "All" or method == "ROT128":
        list_values_rot128 = \
            __get_values_rot128(string, int_ordinals, non_printable, limit)

    if len(list_values_rot13) > 0:
        output += "\r\n  [ROT13]\r\n"
        for value in list_values_rot13:
            output += "    - %s\r\n" % value
        output += "\r\n"
    if len(list_values_rot47) > 0:
        output += "\r\n  [ROT47]\r\n"
        for value in list_values_rot47:
            output += "    - %s\r\n" % value
        output += "\r\n"
    if len(list_values_rot128) > 0:
        output += "\r\n  [ROT128]\r\n"
        for value in list_values_rot128:
            output += "    - %s\r\n" % value
        output += "\r\n"

    fh_output = open(file_output, "wb")
    fh_output.write(output)
    fh_output.close()


def get_version():
    """
        Return the version of this module.
    """
    return __version__


def __get_int_ordinals(string):
    """
        Return the integer ordinals of a string.
    """
    output = ""

    for char in string:
        output += str(ord(char)).rjust(3, " ") + ", "
    output = output.rstrip(", ")

    return output


def __get_printable(string):
    """
        Replace non-printable characters inside a string with whitespaces
    """
    output = ""

    chars_remove = "\t\n\r\x0b\x0c"
    for char in chars_remove:
        string = string.replace(char, " ")

    for char in string:
        if char not in st.printable:
            output += " "
        else:
            output += char

    if output.strip() == "":
        output = "(only non-printable characters or spaces)"

    return output


def __get_values_rot13(string, int_ordinals, non_printable, limit):
    """
        Core method to get all possible ROT13 values for the given string.
    """
    list_values = []
    for i in range(1, 26):
        output = __prepare_line(rot13.decrypt_string(string, i),
                                int_ordinals, non_printable, limit)
        list_values.append("Value %s:   %s" % (str(i).rjust(3, " "), output))

    return list_values


def __get_values_rot47(string, int_ordinals, non_printable, limit):
    """
        Core method to get all possible ROT47 values for the given string.
    """
    list_values = []
    for i in range(1, 94):
        output = __prepare_line(rot47.decrypt_string(string, i),
                                int_ordinals, non_printable, limit)
        list_values.append("Value %s:   %s" % (str(i).rjust(3, " "), output))

    return list_values


def __get_values_rot128(string, int_ordinals, non_printable, limit):
    """
        Core method to get all possible ROT128 values for the given string.
    """
    list_values = []
    for i in range(1, 256):
        output = __prepare_line(rot128.decrypt_string(string, i),
                                int_ordinals, non_printable, limit)
        list_values.append("Value %s:   %s" % (str(i).rjust(3, " "), output))

    return list_values


def __prepare_line(line, int_ordinals, non_printable, limit):
    """
        Prepare the line before it gets written into the file.
    """
    if int_ordinals:
        line = __get_int_ordinals(line)
    else:
        if not non_printable:
            line = __get_printable(line)

    if limit:
        if len(line) > 58:
            line = line[:55] + "..."

    return line

# EOF
