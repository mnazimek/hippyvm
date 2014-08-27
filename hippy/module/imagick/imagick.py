from rpython.translator.tool.cbuild import ExternalCompilationInfo
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

def _resizeImage(columns, rows, filter, blur):
    ll_magic = lltype.nullptr(MAGIC)
    return c_resizeImage(columns, rows, filter, blur, bestfit = 0)

def _render():
    return c_render(sdfsdfd)