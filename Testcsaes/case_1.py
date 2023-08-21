import time

import pytest

from Pages.l_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestSkypeLogin:
    def test_successful_login(self):
        lp = LaunchPage(self.driver)
        lp.Navigate_to_the_URL()
        lp.Permissions_interaction()
        lp.Exprience()
