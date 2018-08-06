#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# ============================================================================
# ROTate - Encryption tool based on the ROT cipher
# ROT47 encryption/decryption script
# Copyright (C) 2018 by Ralf Kilian
# Distributed under the MIT License (https://opensource.org/licenses/MIT)
#
# GitHub: https://github.com/urbanware-org/rotate
# GitLab: https://gitlab.com/urbanware-org/rotate
# ============================================================================

import os
import sys


def main():
    from core import clap
    from core import rot47

    try:
        p = clap.Parser()
    except Exception as e:
        print "%s: error: %s" % (os.path.basename(sys.argv[0]), e)
        sys.exit(1)

    p.set_description("Encrypt or decrypt a file using ROT47 with the "
                      "default rotation value or a user-defined one (using "
                      "the ROT47 character set).")
    p.set_epilog("Further information and usage examples can be found inside "
                 "the documentation file for this script.")

    # Define required arguments
    p.add_predef("-a", "--action", "action to perform", "action",
                 ["encrypt", "decrypt"], True)
    p.add_avalue("-i", "--input-file", "input file path", "input_file", None,
                 True)
    p.add_avalue("-o", "--output-file", "output file path", "output_file",
                 None, True)

    # Define optional arguments
    p.add_avalue("-b", "--buffer-size", "buffer size in bytes", "buffer_size",
                 4096, False)
    p.add_switch("-h", "--help", "print this help message and exit", None,
                 True, False)
    p.add_avalue("-v", "--value", "user-defined rotation value between 0 and "
                 "93", "value", 47, False)
    p.add_switch(None, "--version", "print the version number and exit", None,
                 True, False)

    if len(sys.argv) == 1:
        p.error("At least one required argument is missing.")
    elif ("-h" in sys.argv) or ("--help" in sys.argv):
        p.print_help()
        sys.exit(0)
    elif "--version" in sys.argv:
        print rot47.get_version()
        sys.exit(0)

    args = p.parse_args()
    if args.action is None:
        p.error("The required action argument is missing.")
    elif args.action.lower() == ("encrypt"):
        encrypt = True
    elif args.action.lower() == ("decrypt"):
        encrypt = False
    else:
        p.error("An unsupported action was given.")

    try:
        if encrypt:
            rot47.encrypt_file(args.input_file, args.output_file,
                               args.buffer_size, args.value)
        else:
            rot47.decrypt_file(args.input_file, args.output_file,
                               args.buffer_size, args.value)
    except Exception as e:
        p.error(e)


if __name__ == "__main__":
    main()

# EOF
