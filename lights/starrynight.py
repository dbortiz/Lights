import light
import time
from neopixel import *
import threading
import random



class StarryNight(light.Light):

    def __init__(self, server):
        self.server = server
        self._running = False
        self._disabled = False
        super().__init__("starryNight")

    def start(self, *args):
        self._running = True
        colors = super(StarryNight, self).getColorsFromArg(1, *args)
        if colors is None:
            return

        for i in range(0, self.server.LED_COUNT, 1):
            self.server.strip.setPixelColorRGB(i, 0, 0, 0)

        numbers = list(range(self.server.LED_COUNT))
        for x in range(0, self.server.LED_COUNT, 1):
            choice = random.choice(numbers)
            numbers.remove(choice)
            self.server.strip.setPixelColor(choice, colors[0])
            self.server.strip.show()
            time.sleep(.1)
            if not self._running:
                return

    def stop(self):
        self._running = False
        print("Stopping the starry night effect")



