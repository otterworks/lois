#!/usr/bin/env python3

import numpy as np
from lcm import EventLog
import cv2

from ..lcmtypes.raw import bytes_t
from ..lcmtypes.image import image_t

class LOIE():

    def __init__(self, verbose=0):
        self.verbose = verbose

    def handle_image_t(self, channel, data):
        msg = image_t.decode(data)
        if self.verbose > 0:
            print("rx {m.height}-by-{m.width} image on {c}".format(c=channel, m=msg))
        img = np.frombuffer(msg.data, np.uint8)
        img.shape = (msg.height, msg.width)
        if self.verbose > 1:
            print("\tmin: {0}, max: {1}".format(img.min(), img.max()))
        self.write(channel, msg.utime, img)

    def handle_raw_bytes_t(self, channel, data):
        msg = bytes_t.decode(data)
        # convert jpeg to opencv image
        img = 0
        self.write(channel, msg.utime, img)

    def write(self, channel, utime, img):
        cv2.imwrite("{utime}.{channel}.png".format(channel=channel, utime=utime), img)

    def extract(self, lcmlog, channel):
        el = EventLog(lcmlog)
        for event in el:
            if event.channel == channel:
                self.handle_image_t(event.channel, event.data)
