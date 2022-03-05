#!/usr/bin/env python3

from .spy import LOIS

def main(channel, scale=0.5, verbose=0):
    """Show images"""
    s = LOIS([channel], scale=scale, verbose=verbose)
    s.spy()


if __name__ == "__main__":
    import argparse
    P = argparse.ArgumentParser(description="LCM OpenCV Image Spy")
    P.add_argument('-s', '--scale', type=float, default=0.5,
                   help='display verbose output')
    P.add_argument('-v', '--verbose', action='count', default=0,
                   help='display verbose output')
    P.add_argument('-V', '--version', action='version',
                   version='%(prog)s 0.0.1',
                   help='display version information and exit')
    P.add_argument('channel', help='the LCM channel to listen on')
    A = P.parse_args()
    main(**A.__dict__)
