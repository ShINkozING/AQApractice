import random
import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Функциональность профиля")
class TestProfileFeature(BaseTest):

    @allure.title("Смена имени в профиле")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.my_info.is_opened()
        self.my_info.change_name(f"Test {random.randint(1,100)}")
        self.my_info.save_changes()
        self.my_info.is_changes_saved()
        self.my_info.make_screenshot("Успех")