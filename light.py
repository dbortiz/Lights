from abc import ABC,abstractmethod
import time
import re
import server


class Light:

    def __init__(self, name):
        self.name = name
        super().__init__()

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def start(self, *args):
        pass

    @property
    def disabled(self):
        return self._disabled

    @property
    def isRunning(self):
        return self._running

    def getName(self):
        return self.name

    def human_name(self):
        name = re.sub('(?!^)([A-Z][a-z]+)', r' \1', self.name).split()
        name = " ".join(name)
        name = name[0].upper() + name[1:]
        return name

    def getColorsFromArg(self, amt, *args):
        colors = []
        for arg in args:
            print("ARGUMENT:")
            print(arg)
            if arg is not None:
                colors.append(arg)
            if len(colors) >= amt:
                break
        if len(colors) < amt:
            return None
        return colors
