import math


def iterate_lin(hue, stepsize, n):
    return [hue + i * stepsize for i in range(n)]


def iterate_sin(hue, stepsize, n):
    return [(math.sin(hue + i * stepsize) * 0.5) + 1 for i in range(n)]


def iterate_sin2(hue, stepsize, n):
    return [math.pow(math.sin(hue + i * stepsize), 2) for i in range(n)]


def create_parser():
    from argparse import ArgumentParser, SUPPRESS
    from glow.Common import arg_range, arg_positive

    parser = ArgumentParser(
        add_help=False, usage=SUPPRESS, description="Effect options:"
    )
    parser.add_argument(
        "-s",
        "--stepsize",
        default=math.pi / 1024.0,
        type=arg_positive(float),
        help="rainbow color stepsize (default: math.pi/1024)",
    )
    return parser
