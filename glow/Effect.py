def list_all():
    import os

    moduledir = os.path.dirname(__file__)
    plugins = filter(
        lambda x: x.startswith("Effect_")
        and x.endswith(".py")
        and os.path.isfile(os.path.join(moduledir, x)),
        os.listdir(moduledir),
    )
    return [i[7:-3] for i in plugins]


def load(name):
    import os.path, sys

    moduledir = os.path.dirname(__file__)
    modulename = "Effect_" + name
    if sys.version_info < (3, 5, 3):
        import imp

        fp, pathname, description = imp.find_module(modulename, [moduledir])
        module = imp.load_module("EffectInstance", fp, pathname, description)
    else:
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            modulename, os.path.join(moduledir, modulename + ".py")
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    return module
