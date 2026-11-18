import sys
import types
from pathlib import Path
from unittest.mock import Mock

# Provide a fake googletrans module because it is not installed.
fake_googletrans = types.ModuleType("googletrans")
fake_googletrans.Translator = Mock()
sys.modules["googletrans"] = fake_googletrans

# Add the repository root to Python's import path.
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from personal_translator import text_translator


def test_text_translator_uses_english_and_returns_translated_text():
    expected_text = "Good morning"

    fake_translator = Mock()
    fake_translator.translate.return_value.text = expected_text
    fake_googletrans.Translator.return_value = fake_translator

    result = text_translator("Guten Morgen")

    fake_translator.translate.assert_called_once_with(
        "Guten Morgen", dest="en"
    )
    assert result == expected_text
