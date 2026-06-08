import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import Config

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@pytest.fixture
def logged_in_user(page):
    """Fixture that logs in before the test starts"""
    login = LoginPage(page)
    login.open()
    login.login(
        Config.USERS["standard"]["username"],
        Config.USERS["standard"]["password"]
    )
    return page

@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    yield
    if request.node.rep_call.failed:
        allure.attach(
            page.screenshot(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)