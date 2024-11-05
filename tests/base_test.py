# Single point of page import
from pages.signup_page import SignupPage


class BaseTest:

    # Setup method for Test Class
    def setup_method(self):
        self.signup_page = SignupPage(self.page)
