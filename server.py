from neopixel import *
# LED strip configuration:
LED_COUNT = 600  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 128  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

class Server:
    LED_COUNT = LED_COUNT

    def __init__(self):
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.strip.begin()
        super().__init__()

    def toggleOffLights(self):
        pass

    def setPixelRGB(self, loc, r, g, b):
        self.strip.setPixelColorRGB(loc, r, g, b)

    def setPixelColor(self, loc, Color):
        self.strip.setPixelColor(loc, Color)

    def show(self):
        self.strip.show()

    def getBrightness(self):
        return self.strip.getBrightness();

    def setBrightness(self,val):
        self.strip.setBrightness(val)
        self.show()
