"""from rpython.translator.tool.cbuild import ExternalCompilationInfo
from rpython.rtyper.tool import rffi_platform as platform
from rpython.rtyper.lltypesystem import rffi, lltype
from rpython.rlib.rarithmetic import intmask

eci = ExternalCompilationInfo(includes=['wand/MagickWand.h','magick/MagickCore.h>'],
                              include_dirs=['/usr/include/mutils/'],
                              library_dirs=['/usr/lib/', ],
                              libraries=['magic'])


class CConfig:
    _compilation_info_ = eci
    MAGIC = platform.Struct('MAGIC', [])

globals().update(platform.configure(CConfig))

def external(name, args, result):
    return rffi.llexternal(name, args, result,
                           compilation_info=eci, releasegil=False)

MAGIC_PTR = lltype.Ptr(MAGIC)

c_resizeImage = external(
    'Imagick::resizeImage',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT,
     rffi.INT],
    rffi.INT
)

c_render = external(
    'Imagick::render',
    [rffi.VOIDP],
    rffi.INT
)
"""
"""
c_clear = external(
    'Imagick::clear',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)


c_commentImage = external(
    'Imagick::clone',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)


c_cropImage = external(
    'Imagick::compositeImage',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)

c_cropImage = external(
    'Imagick::cropImage',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)

c_cropImage = external(
    'Imagick::current',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)

c_cropImage = external(
    'Imagick::destroy',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)

c_cropImage = external(
    'Imagick::displayImage',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)

c_cropImage = external(
    'Imagick::drawImage',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)

c_cropImage = external(
    'Imagick::getFilename',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)

c_cropImage = external(
    'Imagick::getFormat',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)

c_cropImage = external(
    'Imagick::getImage',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)

c_cropImage = external(
    'Imagick::getImageHeight',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)

c_cropImage = external(
    'Imagick::getImageSize',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)

c_cropImage = external(
    'Imagick::getImageWidth',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)

c_cropImage = external(
    'Imagick::getOption',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)

c_cropImage = external(
    'Imagick::getPage',
    [rffi.INT,
     rffi.INT,
     rffi.INT,
     rffi.FLOAT],
    MAGIC_PTR
)
"""
"""
def _resizeImage(columns, rows, filter, blur):
    ll_magic = lltype.nullptr(MAGIC)
    return c_resizeImage(columns, rows, filter, blur, bestfit = 0)

def _render():
    return c_render(sdfsdfd)
    """