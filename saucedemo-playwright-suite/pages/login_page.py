from pages.base_page import BasePage
from config.config import Config

class LoginPage(BasePage):
    # Locators — all in one place
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"
    URL = Config.BASE_URL

    def open(self):
        self.navigate(self.URL)
    
    def login(self, username:str,password:str):
        self.page.fill(self.USERNAME,username)
        self.page.fill(self.PASSWORD,password)
        self.page.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return  self.page.locator(self.ERROR_MESSAGE)
