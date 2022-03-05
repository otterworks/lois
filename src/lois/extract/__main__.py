#!/usr/bin/env python3

from .extract import LOIE

def main(lcmlog, channel, verbose=0):
    """Extract images"""
    e = LOIE(verbose=verbose)
    e.extract(lcmlog, channel)


if __name__ == "__main__":
    import argparse
    P = argparse.ArgumentParser(description="LCM OpenCV Image Extractor")
    P.add_argument('-v', '--verbose', action='count', default=0,
                   help='display verbose output')
    P.add_argument('-V', '--version', action='version',
                   version='%(prog)s 0.0.1',
                   help='display version information and exit')
    P.add_argument('lcmlog', help='the LCM log to extract from')
    P.add_argument('channel', help='the LCM channel to extract from')
    A = P.parse_args()
    main(**A.__dict__)
