import sys
import importlib

class Platforms:
    def __getattr__(self, name):
        if name == "__path__":
            return []
        for support in ["official", "partner", "community"]:
            candidate = "litex_boards." + support + ".platforms." + name
            if importlib.util.find_spec(candidate) is not None:
                return importlib.import_module(candidate)
        raise ModuleNotFoundError

sys.modules[__name__] = Platforms()
