#!/usr/bin/env python3

import numpy as np
import lcm
import cv2

from ..lcmtypes.raw import bytes_t
from ..lcmtypes.image import image_t

class LOIS():

    def __init__(self, channels, scale=1.0, verbose=0):
        self.channels = channels
        self.scale = scale
        self.verbose = verbose

    def handle_image_t(self, channel, data):
        msg = image_t.decode(data)
        if self.verbose > 0:
            print("rx {m.height}-by-{m.width} image on {c}".format(c=channel, m=msg))
        img = np.frombuffer(msg.data, np.uint8)
        img.shape = (msg.height, msg.width)
        if self.verbose > 1:
            print("\tmin: {0}, max: {1}".format(img.min(), img.max()))
        self.show(channel, img)

    def handle_raw_bytes_t(self, channel, data):
        msg = bytes_t.decode(data)
        # convert jpeg to opencv image
        img = 0
        self.show(channel, img)

    def show(self, channel, img):
        i = cv2.resize(img, dsize=None, fx=self.scale, fy=self.scale)
        cv2.imshow(channel, img)
        cv2.waitKey(1)

    def spy(self):
        lio = lcm.LCM()
        subscriptions = [lio.subscribe(c, self.handle_image_t) for c in self.channels]
        try:
            while 1<3:
                lio.handle()

        except KeyboardInterrupt:
            pass
