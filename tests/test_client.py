from deepl.client import Translator
import pytest


@pytest.fixture
def translator():
    t = Translator()
    t.start()
    return t


def test_translation(translator):
    assert translator.translate("Hello world!") == "Bonjour le monde !"


def test_switch(translator):
    translator.switch_lang()
    assert translator.translate("Bonjour le monde !") == "Hello world!"


def test_change_lang(translator):
    translator.change_lang(fr="en", to="jp")
    assert translator.translate("Hello") == "こんにちは"
