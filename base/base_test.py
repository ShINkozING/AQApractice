import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info import MyInfo
from config.data import Data

class BaseTest:

    data: Data

    login_page: LoginPage
    dashboard_page: DashboardPage
    my_info: MyInfo

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data

        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.my_info = MyInfo(driver)

