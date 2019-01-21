import light
import time
from neopixel import *


class Strobe(light.Light):

    def __init__(self, server):
        self.server = server
        self._running = False
        self._disabled = False
        super().__init__("strobeEffect")

    def start(self, *args):
        print('This is the start of Strobe')
        colors = super(Strobe, self).getColorsFromArg(2, *args)
        print("FINAL")
        print(colors)
        if colors is not None:
            self._running = True
        while self._running:
            for i in range(0, self.server.LED_COUNT, 1):
                self.server.setPixelColor(i, colors[0])
            self.server.show()
            time.sleep(.01)
            for i in range(0, self.server.LED_COUNT, 1):
                self.server.setPixelColor(i, colors[1])
            self.server.show()
            time.sleep(.01)


    def stop(self):
        self._running = False
        print("Stopping the strobe effect")





