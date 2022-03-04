#!/usr/bin/env python3

import lcm
import cv2

from lois_lcmtypes import image_t, raw_bytes_t

class LOIS():

    def __init__(self, channels, scale=1.0):
        self.channels = channels
        self.scale = scale

    def handle_image_t(self, channel, data):
        msg = image_t.decode(data)
        self.show(channel, msg.image)

    def handle_raw_bytes_t(self, channel, data):
        msg = bytes_t.decode(data)
        # convert jpeg to opencv image
        img = 0
        self.show(channel, img)

    def show(self, channel, img):
        i = cv2.resize(img, fx=self.scale, fy=self.scale)
        cv2.imshow(channel, i)

    def run(self):
        lio = lcm.LCM()
        subscriptions = [lio.subscribe(c, handle_image_t) for c in self.channels]
        try:
            while 1<3:
                lio.handle()

        except KeyboardInterrupt:
            pass


# python3 -m lois images 0.25
