# PyDeepL translate

This is a python package for translating using DeepL. The package uses a web driver to communicate with the page https://deepl.com/translator.
The package is essentially a rewriting of Haruna (eggplants)'s package deepl-cli. I follow roughly the same structure as [py-googletrans](https://github.com/ssut/py-googletrans) package which translate by interacting with Google Translate's AJAX API.

## DeepL API
It was previously possible to make calls to DeepL API via the url https://www.deepl.com/jsonrpc but DeepL have it shut down. Package like https://github.com/freundTech/deepl-cli/ using this url cannot be used anymore.

This package provides a way to translate text using DeepL's freely available web translator. Yet if you care about performance, I strongly advise you to take a subscription and use DeepL official API. You can consider this package as a way to test DeepL's translation quality.

## Requirements

- [Python >= 3.8](https://www.python.org/ftp/python/)
    - (Because of `:=`, Walrus operator)
- [google-chrome >= 83](https://www.google.com/chrome/?platform=linux)
- [chromedriver >= 83](https://chromedriver.chromium.org/downloads)
- [selenium](https://pypi.org/project/selenium/)

## Usage

```
from deepl.client import Translator
t = Translator()
translator.change_lang(fr="en", to="jp")
translator.translate("Hello")
```

## Lisence

MIT

## Author
Adam Oudad.

This is based on deep-cli by Haruna(eggplants). I am rewriting the original code to follow [py-googletrans](https://github.com/ssut/py-googletrans) package structure to be used as a python module.
