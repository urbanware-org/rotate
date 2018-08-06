#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ============================================================================
# ROTate - Encryption tool based on the ROT cipher
# Cracker script
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
    from core import cracker

    try:
        p = clap.Parser()
    except Exception as e:
        print("%s: error: %s" % (os.path.basename(sys.argv[0]), e))
        sys.exit(1)

    p.set_description("Determine which ROT variant and rotation value was "
                      "used to encrypt a file or string by trying all "
                      "supported ROT variants with all rotation values "
                      "available (brute force).")
    p.set_epilog("Further information and usage examples can be found inside "
                 "the documentation file for this script.")

    # Define required arguments
    p.add_avalue("-o", "--output-file", "output file path", "output_file",
                 None, True)
    p.add_avalue("-s", "--string", "string to decrypt", "string", None, True)

    # Define optional arguments
    p.add_switch("-h", "--help", "print this help message and exit", None,
                 True, False)
    p.add_switch(None, "--int-ordinals", "write integer ordinals instead "
                 "of the characters into the output file", "int_ordinals",
                 True, False)
    p.add_predef("-m", "--method", "use only one instead of all supported "
                 "methods to decrypt", "method", ["rot13", "rot47", "rot128"],
                 False)
    p.add_switch(None, "--no-limit", "do not limit the length of the lines "
                 "inside the output file", "no_limit", False, False)
    p.add_switch(None, "--non-printable", "write non-printable characters "
                 "into the output file", "non_printable", True, False)
    p.add_switch(None, "--version", "print the version number and exit", None,
                 True, False)

    if len(sys.argv) == 1:
        p.error("At least one required argument is missing.")
    elif ("-h" in sys.argv) or ("--help" in sys.argv):
        p.print_help()
        sys.exit(0)
    elif "--version" in sys.argv:
        print(cracker.get_version())
        sys.exit(0)

    args = p.parse_args()
    try:
        cracker.brute_force(args.string, args.output_file, args.method,
                            args.int_ordinals, args.non_printable,
                            args.no_limit)
    except Exception as e:
        p.error(e)


if __name__ == "__main__":
    main()

# EOF
