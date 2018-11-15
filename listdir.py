#!/usr/bin/env python3
# coding:utf-8

import os
import argparse
import Exifdata

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "directory", help="directory to list"
    )
    args = parser.parse_args()
    if not os.path.isdir(args.directory):
        print(
            "WARNING: Please provide directory name to list"
        )

    for root, dirs, files in os.walk(args.directory, topdown=True ):
        for d in dirs:
            print(os.path.join(root, d))
        for f in files:
            print(os.path.join(root, f))
            Exifdata.getMetaData(os.path.join(root, f))

if __name__ == '__main__':
    Main()