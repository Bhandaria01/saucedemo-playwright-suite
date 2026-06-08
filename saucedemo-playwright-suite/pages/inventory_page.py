from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = ".title"
    URL = "https://www.saucedemo.com/inventory.html"

    def get_page_title(self):
        return self.page.locator(self.TITLE)
