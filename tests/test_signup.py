import allure
import pytest
from tests.base_test import BaseTest
from helpers.generator import (generate_negative_username, generate_negative_email,
                               generate_negative_password, generate_negative_referral)


@allure.parent_suite("Registrations tests area")
@allure.suite("Positive tests for Registrations")
class TestSignupPositive(BaseTest):
    def test_signup_with_valid_data_with_referral(self, user):
        self.signup_page.open()
        self.signup_page.signup_positive(user)
        self.signup_page.check_captcha()

    def test_signup_with_valid_data_without_referral(self, user):
        self.signup_page.open()
        self.signup_page.signup_positive(user, without_referral=True)
        self.signup_page.check_captcha()


@allure.parent_suite("Registrations tests area")
@allure.suite("Negative tests for Registrations")
class TestSignupNegative(BaseTest):
    @pytest.mark.parametrize("username,exp_msg", [("", "Поле не заполнено"),
                                                  generate_negative_username(min_length=True),
                                                  generate_negative_username(max_length=True),
                                                  generate_negative_username(start_digit=True),
                                                  generate_negative_username(invalid_chars=True)],
                             ids=["empty", "min_length", "max_length", "start_digit", "invalid_chars"])
    # @allure.title(f"Signup tests with invalid username")
    def test_signup_negative_username_field(self, request, user, username, exp_msg):
        test_id = request.node.name[request.node.name.index("-")+1:-1]
        allure.dynamic.title(f"Signup with invalid username({test_id})")
        self.signup_page.open()
        self.signup_page.signup_negative_by_field(user, "username", username)
        self.signup_page.check_msg("username", exp_msg)

    @pytest.mark.parametrize("email,exp_msg", [("", "Поле не заполнено"),
                                               generate_negative_email(without_delimiter=True),
                                               generate_negative_email(without_local=True),
                                               generate_negative_email(without_domain=True)],
                             ids=["empty", "without_delimiter", "without_local", "without_domain", ])
    # @allure.title("Signup tests with invalid email")
    def test_signup_negative_email_field(self, request, user, email, exp_msg):
        test_id = request.node.name[request.node.name.index("-") + 1:-1]
        allure.dynamic.title(f"Signup with invalid email({test_id})")
        self.signup_page.open()
        self.signup_page.signup_negative_by_field(user, "email", email)
        self.signup_page.check_msg("email", exp_msg)

    @pytest.mark.parametrize("password,exp_msg", [("", "Поле не заполнено"),
                                                  generate_negative_password(min_length=True),
                                                  generate_negative_password(max_length=True),
                                                  generate_negative_password(only_alpha=True),
                                                  generate_negative_password(only_digits=True)],
                             ids=["empty", "min_length", "max_length", "only_alpha", "only_digits"])
    # @allure.title("Signup tests with invalid password")
    def test_signup_negative_password_field(self, request, user, password, exp_msg):
        test_id = request.node.name[request.node.name.index("-")+1:-1]
        allure.dynamic.title(f"Signup with invalid password({test_id})")
        self.signup_page.open()
        self.signup_page.signup_negative_by_field(user, "password", password)
        self.signup_page.check_msg("password", exp_msg)

    @pytest.mark.parametrize("referral,exp_msg", [generate_negative_referral(min_length=True),
                                                  generate_negative_referral(max_length=True)],
                             ids=["min_length", "max_length"])
    # @allure.title("Signup tests with invalid referral")
    def test_signup_negative_referral_field(self, request, user, referral, exp_msg):
        test_id = request.node.name[request.node.name.index("-") + 1:-1]
        allure.dynamic.title(f"Signup with invalid referral({test_id})")
        self.signup_page.open()
        self.signup_page.signup_negative_by_field(user, "referral", referral)
        self.signup_page.check_msg("referral", exp_msg)

    @allure.title("Signup without checked user agreement")
    def test_signup_negative_without_user_agreement(self, user):
        self.signup_page.open()
        self.signup_page.signup_negative_by_field(user, "user_agreement")
        self.signup_page.check_status_user_agreement()
