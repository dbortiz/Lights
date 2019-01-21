import light
import time
from neopixel import *
import threading



class RainbowCycle(light.Light):

    def __init__(self, server):
        self.server = server
        self._running = False
        self._disabled = False
        super().__init__("rainbowCycle")

    def start(self, *args):
        self._running = True
        for j in range(256 * 99999):
            for i in range(self.server.LED_COUNT):
                self.server.setPixelColor(i, self.wheel((int(i * 256 / self.server.LED_COUNT) + j) & 255))
            self.server.show()
            time.sleep(20 / 1000.0)
            if not self._running:
                return

    def stop(self):
        self._running = False
        print("Stopping the strobe effect")

    def wheel(self, pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)



