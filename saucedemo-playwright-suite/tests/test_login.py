import allure
from playwright.sync_api import expect
from config.config import Config
from pages.inventory_page import InventoryPage

@allure.feature("Authentication")
@allure.story("Valid Login")
def test_valid_login(login_page, inventory_page):
    with allure.step("Open login page"):
        login_page.open()
    with allure.step("Login with standard user"):
        login_page.login(
            Config.USERS["standard"]["username"],
            Config.USERS["standard"]["password"]
        )
    with allure.step("Verify landing on inventory page"):
        expect(login_page.page).to_have_url(inventory_page.URL)
        expect(inventory_page.get_page_title()).to_have_text("Products")

@allure.feature("Authentication")
@allure.story("Invalid Login")
def test_invalid_login(login_page):
    with allure.step("Open login page"):
        login_page.open()
    with allure.step("Login with invalid credentials"):
        login_page.login(
            Config.USERS["invalid"]["username"],
            Config.USERS["invalid"]["password"]
        )
    with allure.step("Verify error message"):
        expect(login_page.get_error_message()).to_be_visible()
        expect(login_page.get_error_message()).to_contain_text("Username and password do not match")

@allure.feature("Authentication")
@allure.story("Locked User")
def test_locked_user(login_page):
    with allure.step("Open login page"):
        login_page.open()
    with allure.step("Login with locked user"):
        login_page.login(
            Config.USERS["locked"]["username"],
            Config.USERS["locked"]["password"]
        )
    with allure.step("Verify locked error message"):
        expect(login_page.get_error_message()).to_contain_text("Sorry, this user has been locked out")