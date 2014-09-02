from hippy.builtin import wrap, Optional
from ext_module.imagick.wrappers import ImagickResourceArg


@wrap(['space', ImagickResourceArg(None), int, int])
def scaleImage(space, w_imagick_res, cols, rows):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.scaleImage(cols, rows))


@wrap(['space', ImagickResourceArg(None)])
def getImageWidth(space, w_imagick_res):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.getImageWidth())


@wrap(['space', ImagickResourceArg(None)])
def getImageHeight(space, w_imagick_res):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.getImageHeight())


@wrap(['space', ImagickResourceArg(None)])
def valid(space, w_imagick_res):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.valid())


@wrap(['space', ImagickResourceArg(None)])
def clone(space, w_imagick_res):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.clone())


@wrap(['space', ImagickResourceArg(None), int, int, int, int])
def setPage(space, w_imagick_res, width, height, x, y):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.setPage(width, height, x, y))


@wrap(['space', ImagickResourceArg(None), str, str])
def setOption(space, w_imagick_res, key, value):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.setOption(key, value))


'''
@wrap(['space', ImagickResourceArg(None)])
def setType(space, w_imagick_res):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.setType())
'''


@wrap(['space', ImagickResourceArg(None), int, int])
def setSize(space, w_imagick_res, width, height):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.setSize(width, height))


@wrap(['space', ImagickResourceArg(None), str])
def commentImage(space, w_imagick_res, ):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.commentImage(str))


@wrap(['space', ImagickResourceArg(None), str])
def commentImage(space, w_imagick_res, comment):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.commentImage(comment))


@wrap(['space', ImagickResourceArg(None), str])
def writeImage(space, w_imagick_res, fileName):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.writeImage(fileName))


@wrap(['space', ImagickResourceArg(None), str, int])
def writeImages(space, w_imagick_res, filename, adjoin):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.writeImages(filename, adjoin))


"""
@wrap(['space', ImagickResourceArg(None),int,int])
def thumbnailImage(space, w_imagick_res,columns,rows):
    ""jakis komentarz""
    return space.wrap(w_imagick_res.thumbnailImage(columns,rows))
"""


@wrap(['space', ImagickResourceArg(None), float])
def setImageOpacity(space, w_imagick_res, opacity):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.setImageOpacity(opacity))


@wrap(['space', ImagickResourceArg(None), int])
def setImageCompressionQuality(space, w_imagick_res, quality):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.setImageCompressionQuality(quality))


@wrap(['space', ImagickResourceArg(None), int, int, int, float, Optional(int)])
def resizeImage(space, w_imagick_res, columns, rows, filter, blur, bestfit=0):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.setImageCompressionQuality(columns, rows, filter, blur, bestfit))


