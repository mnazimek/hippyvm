from hippy.builtin import wrap

from hippy.module.imagick.wrappers import ImagickResourceArg



@wrap(['space', ImagickResourceArg(None),int, int])
def scaleImage(space, w_imagick_res, cols, rows):
    """jakis komentarz"""
    return space.wrap(w_imagick_res.scaleImage(cols, rows))