from rpython.translator.tool.cbuild import ExternalCompilationInfo
from rpython.rtyper.tool import rffi_platform as platform
from rpython.rtyper.lltypesystem import rffi, lltype

eci = ExternalCompilationInfo(includes=['imageMagick/wand/magick-image.h', 'imageMagick/wand/magick-property.h'],
                              include_dirs=['/usr/include/imageMagick/wand/'],
                              library_dirs=['/usr/lib/', ],
                              libraries=['ImageMagick'])


class CConfig:
    _compilation_info_ = eci
    IMAGICK = platform.Struct('MagickWand', [])


globals().update(platform.configure(CConfig))


def external(name, args, result):
    return rffi.llexternal(name, args, result,
                           compilation_info=eci, releasegil=False)


IMAGICK_PTR = lltype.Ptr(IMAGICK)

c_scaleImage = external(
    'MagickScaleImage',
    [IMAGICK_PTR,
     rffi.INT,
     rffi.INT],
    IMAGICK_PTR
)

c_getImageWidth = external(
    'MagickGetImageWidth',
    [IMAGICK_PTR],
    rffi.INT
)

c_getImageHeight = external(
    'MagickGetImageHeight',
    [IMAGICK_PTR],
    rffi.INT
)

c_setSize = external(
    'MagickSetSize',
    [IMAGICK_PTR,
     rffi.INT,
     rffi.INT],
    rffi.INT
)
'''
c_setType = external(
    'MagickGetImageHeight',
    [IMAGICK_PTR],
    rffi.INT
)
'''
c_setOption = external(
    'MagickSetOption',
    [IMAGICK_PTR.
    rffi.CCHARP,
     rffi.CCHARP],
    rffi.INT
)

c_setPage = external(
    'MagickSetPage',
    [IMAGICK_PTR,
     rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.INT],
    rffi.INT
)
'''
c_valid = external(
    'MagickValid',
    [IMAGIC''K_PTR],
    rffi.INT
)
'''
c_clone = external(
    'CloneMagickWand',
    [IMAGICK_PTR],
    IMAGICK_PTR
)

c_commentImage = external(
    'MagickCommentImage',
    [IMAGICK_PTR],
    rffi.INT
)

c_writeImage = external(
    'MagickWriteImage',
    [IMAGICK_PTR,
     rffi.CCHARP],
    rffi.VOIDP
)

c_writeImages = external(
    'MagickWriteImages',
    [IMAGICK_PTR,
     rffi.INT],
    rffi.VOIDP
)

c_thumbnailImage = external(
    'MagickThumbnailImage',
    [IMAGICK_PTR,
     rffi.INT,
     rffi.INT],
    rffi.VOIDP
)

c_setImageOpacity = external(
    'MagickSetImageOpacity',
    [IMAGICK_PTR,
     rffi.DOUBLE],
    rffi.VOIDP
)

c_setImageCompressionQuality = external(
    'MagickSetImageCompressionQuality',
    [IMAGICK_PTR,
     rffi.INT],
    rffi.VOIDP
)
"""
def c_setInterlaceScheme = external(
    'MagickThumbnailImage',
    [IMAGICK_PTR,
  \],
    \
)"""


def _scaleImage(img, columns, rows):
    return c_scaleImage(img, columns, rows)


'''
def _setType(img, columns, rows):
    return c_setType(img, columns, rows)
'''


def _setSize(img, columns, rows):
    return c_setSize(img, columns, rows)


def _setPage(img, width, height, x, y):
    return c_setPage(img, width, height, x, y)


def _setOption(img, key, value):
    with rffi.scoped_str2charp(key) as ll_key:
        with rffi.scoped_str2charp(value) as ll_value:
            return c_setOption(img, ll_key, ll_value)


def _getImageWidth(img):
    return int(c_getImageWidth(img))


def _getImageHeight(img):
    return int(c_getImageHeight(img))


'''
def _valid(img):
    return int(c_valid(img))
'''


def _clone(img):
    return (c_clone(img))


def _commentImage(img, comment):
    with rffi.scoped_str2charp(comment) as ll_comment:
        return (c_commentImage(img, ll_comment))


def _writeImage(img, fileName):
    with rffi.scoped_str2charp(fileName) as ll_fileName:
        return (c_writeImage(img, ll_fileName))


def _writeImages(img, fileName, adjoin):
    with rffi.scoped_str2charp(fileName) as ll_fileName:
        return (c_writeImages(img, ll_fileName, adjoin))


def _thumbnailImage(img, columns, rows):
    return (c_thumbnailImage(img, columns, rows))


"""

def setInterlaceScheme(img):
    return (c_setInterlaceScheme(img))
"""


def _setImageOpacity(img, opacity):
    return (c_setImageOpacity(img, opacity))


def _setImageCompressionQuality(img, quality):
    return (c_setImageCompressionQuality(img, quality))