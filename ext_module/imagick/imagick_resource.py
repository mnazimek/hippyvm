from hippy.objects.resources import W_Resource

from ext_module.imagick.cimagick import _scaleImage, \
    _getImageWidth, _getImageHeight, _setSize, _setPage, _setOption, _clone, _commentImage, _thumbnailImage


CLOSE, OPEN = range(2)


class W_ImagickResource(W_Resource):
    def __init__(self, space):
        W_Resource.__init__(self, space)
        self.initialized = False
        self.space = space


    def scaleImage(self, cols, rows):
        return _scaleImage(self.llhandler, cols, rows)

    def getImageWidth(self):
        return _getImageWidth(self.llhandler)

    def getImageHeight(self):
        return _getImageHeight(self.llhandler)


"""
    def valid(self):
        return _valid(self.llhandler)
"""


def setPage(self, width, height, x, y):
    return _setPage(self.llhandler, width, height, x, y)


def setSize(self, cols, rows):
    return _setSize(self.llhandler, cols, rows)


def setOption(self, key, value):
    return _setOption(self.llhandler, key, value)


'''
    def setType(self):
        return _setType(self.llhandler)'''


def clone(self):
    return _clone(self.llhandler)


def commentImage(self, comment):
    return _commentImage(self.llhandler, comment)


def wirteImage(self, comment):
    return _commentImage(self.llhandler, comment)


def writeImage(self, comment, adjoin):
    return _commentImage(self.llhandler, comment, adjoin)


def thumbnailImage(self, columns, rows):
    return _thumbnailImage(self.llhandler, columns, rows)