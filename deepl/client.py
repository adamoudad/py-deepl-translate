#!/usr/bin/env python 3.8
#https://github.com/eggplants/deepl-cli/blob/master/deepl/deepl.py# https://pypi.org/project/deepl/
# https://github.com/freundTech/deepl-cli
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from .constants import LANGCODES
from .urls import BASE_URL


class ArgCheckingError(Exception):
    pass


class PageLoadError(Exception):
    pass


class UnknownLanguageError(Exception):
    pass


class Translator:
    def __init__(self, url=BASE_URL,
                 fr_lang="en",
                 to_lang="fr",
                 timeout=5,
                 retry=3):
        self.base_url = url
        self.timeout = timeout
        self.retry = retry
        self.fr_lang = fr_lang
        self.to_lang = to_lang

    def change_lang(self, fr=None, to=None):
        if fr:
            if fr not in LANGCODES:
                raise UnknownLanguageError(f"{fr} is not in supported languages. Available languages are {self.lang_codes}.")
            self.fr_lang = fr
        if to:
            if to not in LANGCODES:
                raise UnknownLanguageError(f"{to} is not in supported languages. Available languages are {self.lang_codes}.")
            self.to_lang = to
        self.driver.get(self.base_url.format(fr_lang=self.fr_lang,
                                             to_lang=self.to_lang))
        self.clear()

    def switch_lang(self):
        self.change_lang(fr=self.to_lang, to=self.fr_lang)


    def start(self):
        """
        Start driver and open deepl.com web page in it.
        """
        self.options = Options()
        self.options.add_argument('--headless')    # if commented. window will be open
        self.options.add_argument('--disable-gpu') # if commented, window will be open
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--remote-debugging-port=9222')
        self.options.add_argument('--disable-setuid-sandbox')

        self.driver = webdriver.Chrome(
             options=self.options
        )
        self.change_lang()
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located
            )
        except TimeoutException as te:
            raise PageLoadError(te)

        self.input_area = self.driver.find_element_by_xpath(
            '//textarea[@dl-test="translator-source-input"]'
        )
        self.output_area = self.driver.find_element_by_xpath(
            '//textarea[@dl-test="translator-target-input"]'
        )

    def input_text(self, text):
        self.input_area.clear()
        self.input_area.send_keys(text)

    def get_output(self):
        output = self.output_area.get_attribute('value').rstrip()
        return output

    def clear(self):
        self.input_area.clear()

    def translate(self, text):
        if not self.input_area or not self.output_area:
            raise PageLoadError

        self.input_text(text)
        # Wait for the translation process
        time.sleep(self.timeout)  # fix needed
        return self.get_output()

    def close(self):
        self.driver.close()
