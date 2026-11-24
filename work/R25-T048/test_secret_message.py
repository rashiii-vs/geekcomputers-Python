import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from unittest.mock import patch

import pytest


# Locate the original Python program.
MODULE_PATH = (
    Path(__file__).resolve().parents[2]
    / "Secret message generator GUI by tkinter.py"
)


# Fake Tkinter components so importing the program does not open a GUI.
class FakeStringVar:
    def __init__(self):
        self.value = ""

    def get(self):
        return self.value

    def set(self, value):
        self.value = value


class FakeWidget:
    def __init__(self, *args, **kwargs):
        pass

    def place(self, *args, **kwargs):
        pass


class FakeRoot(FakeWidget):
    def geometry(self, *args):
        pass

    def title(self, *args):
        pass

    def mainloop(self):
        pass


fake_tkinter = ModuleType("tkinter")
fake_tkinter.Tk = FakeRoot
fake_tkinter.StringVar = FakeStringVar
fake_tkinter.Label = FakeWidget
fake_tkinter.Entry = FakeWidget
fake_tkinter.Button = FakeWidget


# Import only the target module with the fake Tkinter module.
spec = importlib.util.spec_from_file_location(
    "secret_message_gui", MODULE_PATH
)
module = importlib.util.module_from_spec(spec)

with patch.dict(sys.modules, {"tkinter": fake_tkinter}):
    spec.loader.exec_module(module)


def test_empty_message():
    # Source lines 117-120: an empty input skips the loop,
    # then the result is updated.
    module.name1.set("")
    module.result1.set("old result")

    actual = module.show1()

    assert actual is None
    assert module.name1.get() == ""
    assert module.result1.get() == "SECRET MESSAGE IS:-\n"


def test_unknown_character_preserves_state_and_recovers():
    # Source line 118: codes[x] raises KeyError for unsupported input.
    # Lines 119-120 run only after successful conversion.
    module.name1.set("!")
    module.result1.set("previous result")

    with pytest.raises(KeyError) as error:
        module.show1()

    assert error.value.args == ("!",)
    assert module.name1.get() == "!"
    assert module.result1.get() == "previous result"

    # A valid call after the failure must still work.
    module.name1.set("Hi")
    actual = module.show1()

    assert actual is None
    assert module.name1.get() == ""
    assert module.result1.get() == "SECRET MESSAGE IS:-\nGh"
