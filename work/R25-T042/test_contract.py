import importlib.util
import sys
from pathlib import Path
from types import ModuleType

SOURCE = Path(__file__).resolve().parents[2] / "Polyline.py"


def load_polyline(monkeypatch):
    fake_simplegui = ModuleType("simplegui")

    class FakeFrame:
        def set_mouseclick_handler(self, handler):
            pass

        def set_draw_handler(self, handler):
            pass

        def add_button(self, text, handler):
            pass

        def start(self):
            pass

    fake_simplegui.create_frame = lambda *args: FakeFrame()
    monkeypatch.setitem(sys.modules, "simplegui", fake_simplegui)

    spec = importlib.util.spec_from_file_location("Polyline", SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def test_click_first_point_on_empty_polyline(monkeypatch):
    module = load_polyline(monkeypatch)

    # Source precondition: Polyline.py line 5 initializes polyline = [].
    pos = (0, 0)

    result = module.click(pos)

    assert result is None
    assert module.polyline == [(0, 0)]


def test_click_appends_to_existing_polyline(monkeypatch):
    module = load_polyline(monkeypatch)

    # Source precondition: Polyline.py line 5 initializes polyline = [].
    module.polyline.append((10, 20))
    pos = (100, 50)

    result = module.click(pos)

    assert result is None
    assert module.polyline == [(10, 20), (100, 50)]
