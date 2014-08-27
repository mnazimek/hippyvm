from hippy.objects.resources import W_Resource


from hippy.module.imagick.cimagick import _scaleImage


CLOSE, OPEN = range(2)


class W_ImagickResource(W_Resource):
    def __init__(self, space):
        W_Resource.__init__(self, space)
        self.initialized = False
        self.space = space


    def scaleImage(self, cols,rows):
        ll_res = _scaleImage(cols,rows)
        if not ll_res:
            self.space.ec.warn("scaleImage(): Could "
                               "not scale Image")
        self.llhandler = ll_res
