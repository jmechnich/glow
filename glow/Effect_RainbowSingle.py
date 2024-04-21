from glow.Effect_Rainbow import Rainbow
from glow.RainbowCommon import iterate_lin
from glow.Conversion import convert, toRGB


class RainbowSingle(Rainbow):
    def __init__(self, args):
        super(RainbowSingle, self).__init__(args)

    def iterate(self):
        self.step_hue()
        rgb = [self.hue, 1, 1]
        convert(rgb, [toRGB])
        return rgb * self.nled


def create_parser():
    from glow.RainbowCommon import create_parser as cp

    return cp()


def instance(args):
    return RainbowSingle(args)
