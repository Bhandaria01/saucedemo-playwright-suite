from playwright.sync_api import Page
from config.config import Config

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(Config.TIMEOUT)

    def navigate(self, url: str):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()