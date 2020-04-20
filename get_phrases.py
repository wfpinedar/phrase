from importlib import reload
import time

from config import WEB_DRIVER
from config import PHRASES_SITE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=WEB_DRIVER)


def get_phrases(market_url):
    driver.get(market_url)
    # Get list of phrases
    elem = driver.find_elements_by_tag_name("blockquote")
    phrases = list()
    if elem:
        for e in elem:
            phrases.append({"phrase": e.text.split("\n")[0], "author": e.text.split(
                "\n")[1]} if len(e.text.split("\n")) == 2 else {})
    driver.close()
    return phrases


if __name__ == "__main__":
    get_phrases(phrases_url)
