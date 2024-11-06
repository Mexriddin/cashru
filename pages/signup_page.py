from pages.base_page import BasePage
from data.links import Links


class SignupPage(BasePage):
    _PAGE_URL = Links.SIGNUP_PAGE

    _SIGNUP_SHADOW = "div[p1='signup']"
    _USER_NAME = "div[data-wi='user-name'] input"
    _EMAIL = "div[data-wi='identificator'] input"
    _PASSWORD = "div[data-wi='password'] input"
    _REFERRAL = "div[data-wi='referral'] input"
    _USER_AGREEMENT = "div[data-wi='user-agreement'] input"
    _SUBMIT_BTN = "div[data-wi='submit-button'] button"

    _MSG_USERNAME = "div[data-wi='user-name'] div[data-wi='message'] span"
    _MSG_EMAIL = "div[data-wi='identificator'] div[data-wi='message'] span"
    _MSG_PASSWORD = "div[data-wi='password'] div[data-wi='error'] span"
    _MSG_REFERRAL = "div[data-wi='referral'] div[data-wi='message'] span"
    _STATUS_USER_AGREEMENT = "div[data-wi='user-agreement']>div"

    def __signup_shadow(self, element_locator):
        element = self.shadow_root(self._SIGNUP_SHADOW).query_selector(f"css={element_locator}")
        return element

    def enter_username(self, username: str):
        self.__signup_shadow(self._USER_NAME).fill(username)

    def enter_email(self, email: str):
        self.__signup_shadow(self._EMAIL).fill(email)

    def enter_password(self, password: str):
        self.__signup_shadow(self._PASSWORD).fill(password)

    def enter_referral(self, referral: str):
        self.__signup_shadow(self._REFERRAL).fill(referral)

    def check_user_agreement(self):
        return self.__signup_shadow(self._USER_AGREEMENT).click()

    def click_signup_button(self):
        self.__signup_shadow(self._SUBMIT_BTN).click()

    def signup_negative_by_field(self, user, field_name, value=None):
        self.enter_username(value) if field_name == "username" else self.enter_username(user.username)
        self.enter_email(value) if field_name == "email" else self.enter_email(user.email)
        self.enter_password(value) if field_name == "password" else self.enter_password(user.password)
        self.enter_referral(value) if field_name == "referral" else self.enter_referral(user.referral)
        if field_name != "user_agreement":
            self.check_user_agreement()
        if field_name != "referral":
            self.click_signup_button()


    def check_msg(self, filed_name, exp_msg):
        msg_locator = ""
        if filed_name == "username":
            msg_locator = self._MSG_USERNAME
        elif filed_name == "email":
            msg_locator = self._MSG_EMAIL
        elif filed_name == "password":
            msg_locator = self._MSG_PASSWORD
        elif filed_name == "referral":
            msg_locator = self._MSG_REFERRAL
        actual_msg = self.__signup_shadow(msg_locator).text_content().strip()
        assert actual_msg == exp_msg, f"Actual msg:{actual_msg}\nExpected:{exp_msg}"

    def check_status_user_agreement(self):
        assert "v-input--is-label-active" not in self.__signup_shadow(self._STATUS_USER_AGREEMENT).get_attribute("class")