from rpython.translator.tool.cbuild import ExternalCompilationInfo
from rpython.rtyper.tool import rffi_platform as platform
from rpython.rtyper.lltypesystem import rffi, lltype

eci = ExternalCompilationInfo(includes=['wand/magickWand.h','magick/MagickCore.h'],
                              include_dirs=['/usr/include/mutils/'],
                              library_dirs=['/usr/lib/', ],
                              libraries=['ImageMagick'])


class CConfig:
    _compilation_info_ = eci
    IMAGICK = platform.Struct('IMAGICK', [])

globals().update(platform.configure(CConfig))


def external(name, args, result):
    return rffi.llexternal(name, args, result,
                           compilation_info=eci, releasegil=False)

IMAGICK_PTR = lltype.Ptr(IMAGICK)

c_scaleImage = external(
    'scaleImage',
    [IMAGICK_PTR,
     rffi.INT,
     rffi.INT],
    IMAGICK_PTR
)

def _scaleImage(img, columns, rows):
    ll_magic = lltype.nullptr(IMAGICK_PTR)
    return c_scaleImage(img, columns, rows)