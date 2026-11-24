import random
import sys
import types
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

# Prevent real translation calls while importing the source module.
fake_googletrans = types.ModuleType("googletrans")
fake_googletrans.Translator = Mock()
sys.modules["googletrans"] = fake_googletrans

# Add the repository root to Python's import path.
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import personal_translator


@pytest.fixture
def translator_factory(monkeypatch):
    """Install a controlled fake translator for each test."""

    def install(expected_text):
        fake_translator = Mock()
        fake_translator.translate.return_value = SimpleNamespace(
            text=expected_text
        )

        translator_constructor = Mock(return_value=fake_translator)
        monkeypatch.setattr(
            personal_translator, "Translator", translator_constructor
        )

        return fake_translator, translator_constructor

    return install


def test_smallest_string_input(translator_factory):
    # Source line 17: the function accepts one input argument.
    # Source lines 19-20: it translates to English and returns .text.
    source_text = "a"
    expected_text = "a"
    original_text = source_text

    fake, constructor = translator_factory(expected_text)

    result = personal_translator.text_translator(source_text)

    constructor.assert_called_once_with()
    fake.translate.assert_called_once_with(source_text, dest="en")
    assert result == expected_text
    assert source_text == original_text



import random
import sys
import types
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

# Prevent real translation calls while importing the source module.
fake_googletrans = types.ModuleType("googletrans")
fake_googletrans.Translator = Mock()
sys.modules["googletrans"] = fake_googletrans

# Add the repository root to Python's import path.
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import personal_translator


@pytest.fixture
def translator_factory(monkeypatch):
    """Install a controlled fake translator for each test."""

    def install(expected_text):
        fake_translator = Mock()
        fake_translator.translate.return_value = SimpleNamespace(
            text=expected_text
        )

        translator_constructor = Mock(return_value=fake_translator)

        monkeypatch.setattr(
            personal_translator,
            "Translator",
            translator_constructor
        )

        return fake_translator, translator_constructor

    return install


def test_smallest_string_input(translator_factory):
    # Source line 17: one input parameter.
    # Source lines 19-20: English destination and returned text.
    source_text = "a"
    expected_text = "a"
    original_text = source_text

    fake, constructor = translator_factory(expected_text)

    result = personal_translator.text_translator(source_text)

    constructor.assert_called_once_with()
    fake.translate.assert_called_once_with(source_text, dest="en")

    assert result == expected_text
    assert source_text == original_text


def test_ordinary_english_input(translator_factory):
    # Source line 33 demonstrates that English text remains constant.
    source_text = "I am fine"
    expected_text = "I am fine"
    original_text = source_text

    fake, constructor = translator_factory(expected_text)

    result = personal_translator.text_translator(source_text)

    constructor.assert_called_once_with()
    fake.translate.assert_called_once_with(source_text, dest="en")

    assert result == expected_text
    assert source_text == original_text


def test_one_hundred_bounded_deterministic_inputs(translator_factory):
    # Source lines 17 and 19 establish the input and destination behaviour.
    rng = random.Random(44044)

    words = [
        "I", "am", "fine", "hello", "good", "morning",
        "thank", "you", "today", "we", "learn", "python",
    ]

    cases = [
        " ".join(
            rng.choice(words)
            for _ in range(rng.randint(1, 5))
        )
        for _ in range(100)
    ]

    assert len(cases) == 100
    assert all(1 <= len(case.split()) <= 5 for case in cases)

    for source_text in cases:
        original_text = source_text
        expected_text = source_text

        fake, constructor = translator_factory(expected_text)

        result = personal_translator.text_translator(source_text)

        constructor.assert_called_once_with()
        fake.translate.assert_called_once_with(source_text, dest="en")

        assert result == expected_text
        assert source_text == original_text
