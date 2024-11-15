import pytest
from playwright.sync_api import sync_playwright
from utils.helpers import load_config

@pytest.fixture(scope="session")
def browser_context():
    config = load_config()
    with sync_playwright() as p:
        browser = getattr(p, config["browser"]).launch(headless=False)
        context = browser.new_context()
        yield context
        context.close()
