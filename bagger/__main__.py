import os
import sys
import json
import argparse
from bdbag import bdbag_api as bdb


def parseargs():
    parser = argparse.ArgumentParser()
    return parser.parse_args(sys.argv[1:])


def main():
    args = parseargs()
    return 0


if __name__ == "__main__":
    sys.exit(main())
