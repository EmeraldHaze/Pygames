"""
Splits everything into chunks
"""
terrains = {
    "water": 0x0000FF
    "earth": 0x9C461D
}
class Chunk:
    def __init__ (self, around=[], terrain):
        self.around = around
        self.splited = False
        self.within = [[None, None], [None, None]]

    def render (self):
        if self.splited:
            return

    def split ():
        pass
