import light
import time
from neopixel import *


class Solid(light.Light):

    def __init__(self, server):
        self.server = server
        self._running = False
        self._disabled = False
        super().__init__("solidColor")

    def start(self, *args):
        print('This is the start of Solid')
        colors = super(Solid, self).getColorsFromArg(1, *args)
        if colors is not None:
            for i in range(0, self.server.LED_COUNT, 1):
                self.server.setPixelColor(i, colors[0])
            self.server.show()

    def stop(self):
        self._running = False

