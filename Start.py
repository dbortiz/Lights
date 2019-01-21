from flask import Flask, request, render_template
import light
import server
import time
import re
import flask
from neopixel import *
from lights import *

app = Flask(__name__)
lights = []
lightsHName = []
lightsRName = []
lightServer = None


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("This is a successful post")
        print(request.form)
        if "STOP_ALL_LIGHTS" in request.form:
            print("STOP REQUEST RECIEVED")
            for li in lights:
                li.stop()
            time.sleep(1)
            for i in range(0, lightServer.LED_COUNT, 1):
                lightServer.setPixelRGB(i, 0, 0, 0)
            lightServer.show()
            print("STOP REQUEST ENDED")
        elif "BRIGHTNESS_UPDATE" in request.form:
            lightServer.setBrightness(int(request.form['BRIGHTNESS_UPDATE']));
        else:
            for li in lights:
                if li.getName() in request.form:
                    if li.isRunning:
                        print("I AM NOW Stpoping " + li.getName())
                        li.stop()
                    else:
                        print("I AM NOW STARTING " + li.getName())
                        li.start(convertHexToColor(request.form['color1'] if 'color1' in request.form else None),
                                 convertHexToColor(request.form['color2'] if 'color2' in request.form else None),
                                 convertHexToColor(request.form['color3'] if 'color3' in request.form else None),
                                 convertHexToColor(request.form['color4'] if 'color4' in request.form else None))

    return render_template('index.html', modeHNames=lightsHName, modeRNames=lightsRName, activeMode=None,
                           brightness=lightServer.getBrightness())


def main():
    print(flask.__version__)
    global lightServer
    lightServer = server.Server()
    print(lightServer)
    print([cls.__name__ for cls in light.Light.__subclasses__()])
    for li in light.Light.__subclasses__():
        li_serv = li(lightServer)
        print(li_serv.getName())
        if not li_serv.disabled:
            lights.append(li_serv)
            name = re.sub('(?!^)([A-Z][a-z]+)', r' \1', li_serv.getName()).split()
            name = " ".join(name)
            name = name[0].upper() + name[1:]
            lightsHName.append(name)
            lightsRName.append(li_serv.getName())
            print(" was added")
        else:
            print("Not adding " + li_serv.getName() + " bc its disabled")

    app.run(port=80, debug=True, host='0.0.0.0', threaded=True)


def convertHexToColor(hex):
    if hex is None:
        return None
    colorInput = hex
    currentColor = colorInput.upper()
    print(currentColor)
    h = currentColor
    print('RGB =', tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)))
    val = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    return Color(val[0], val[1], val[2])


if __name__ == '__main__':
    main()
