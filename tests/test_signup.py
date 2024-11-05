import time

import pytest
from tests.base_test import BaseTest
from helpers.generate import (generate_negative_username, generate_negative_email,
                              generate_negative_password, generate_negative_referral)


class TestSignupNegative(BaseTest):
    @pytest.mark.parametrize("username,exp_msg", [("", "Поле не заполнено"),
                                                  generate_negative_username(min_length=True),
                                                  generate_negative_username(max_length=True),
                                                  generate_negative_username(start_digit=True),
                                                  generate_negative_username(invalid_chars=True)],
                             ids=["empty", "min_length", "max_length", "start_digit", "invalid_chars"])
    def test_signup_negative_username_field(self, username, exp_msg):
        self.signup_page.open()
        self.signup_page.signup_negative_by_field("username", username)
        self.signup_page.check_msg("username", exp_msg)

    @pytest.mark.parametrize("email,exp_msg", [("", "Поле не заполнено"),
                                                  generate_negative_email(without_delimiter=True),
                                                  generate_negative_email(without_local=True),
                                                  generate_negative_email(without_domain=True)],
                             ids=["empty", "without_delimiter", "without_local", "without_domain",])
    def test_signup_negative_email_field(self, email, exp_msg):
        self.signup_page.open()
        self.signup_page.signup_negative_by_field("email", email)
        self.signup_page.check_msg("email", exp_msg)


    @pytest.mark.parametrize("password,exp_msg", [("", "Поле не заполнено"),
                                                  generate_negative_password(min_length=True),
                                                  generate_negative_password(max_length=True),
                                                  generate_negative_password(only_alpha=True),
                                                  generate_negative_password(only_digits=True)],
                             ids=["empty", "min_length", "max_length", "only_alpha", "only_digits"])
    def test_signup_negative_password_field(self, password, exp_msg):
        self.signup_page.open()
        self.signup_page.signup_negative_by_field("password", password)
        self.signup_page.check_msg("password", exp_msg)

    @pytest.mark.parametrize("referral,exp_msg", [generate_negative_referral(min_length=True),
                                                  generate_negative_referral(max_length=True)],
                             ids=["min_length", "max_length"])
    def test_signup_negative_referral_field(self, referral, exp_msg):
        self.signup_page.open()
        self.signup_page.signup_negative_by_field("referral", referral)
        self.signup_page.check_msg("referral", exp_msg)


    def test_signup_negative_without_user_agreement(self):
        self.signup_page.open()
        self.signup_page.signup_negative_by_field("user_agreement")
        self.signup_page.check_status_user_agreement()
