from hippy.builtin import ValueUnwrapper


class ImagickResourceArg(ValueUnwrapper):
    def __init__(self, error_value):
        self.error_value = error_value

    def line_for_arg(self, i, input_i):
        lines = ['    w_arg = args_w[%d]' % input_i]
        lines += ['    if not space.is_resource(w_arg):']
        lines += ['        raise ExitSilently(space.wrap(%s))' % self.error_value]
        lines += ['    if w_arg.tp != space.tp_mcrypt_res:']
        lines += ['        raise warn_not_mcrypt_res(space, fname, %d, space.int_w(w_arg), w_arg.tp)' % i]
        lines += ['        return space.w_False']
        lines += ['    arg%d = w_arg' % i]
        return lines
