#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ============================================================================
# ROTate - Encryption tool based on the ROT cipher
# Common core module
# Copyright (C) 2018 by Ralf Kilian
# Distributed under the MIT License (https://opensource.org/licenses/MIT)
#
# GitHub: https://github.com/urbanware-org/rotate
# GitLab: https://gitlab.com/urbanware-org/rotate
# ============================================================================

__version__ = "3.0.6"

from . import paval as pv


def get_file_size(file_path):
    """
        Get the size of a file in bytes.
    """
    pv.path(file_path, "", True, True)

    f = open(file_path, "rb")
    f.seek(0, 2)
    file_size = f.tell()
    f.close()

    return int(file_size)


def get_version():
    """
        Return the version of this module.
    """
    return __version__

# EOF
