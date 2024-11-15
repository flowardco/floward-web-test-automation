import pytest
import time
from utils.helpers import load_config
from pages.base_page import BasePage


def test_example(browser_context):
    config = load_config()
    page = browser_context.new_page()
    base_page = BasePage(page)
    base_page.navigate(config["base_url"])
    ##assert "Example Domain" in page.title()
    time.sleep(5)  
    base_page.close()

