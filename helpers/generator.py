from typing import Optional
from faker import Faker
import random
import string

fake = Faker()


def generate_negative_username(min_length: Optional[bool] = None, max_length: Optional[bool] = None,
                               start_digit: Optional[bool] = None, invalid_chars: Optional[bool] = None):
    expect_msg = "Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы"
    username = ""
    if min_length:
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    elif max_length:
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(33))
    elif start_digit:
        username = str(random.choice(string.digits)) + ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    elif invalid_chars:
        username = ''.join(random.choice(["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]) for _ in range(10))
    return username, expect_msg


def generate_negative_email(without_local: Optional[bool] = None, without_domain: Optional[bool] = None,
                            without_delimiter: Optional[bool] = None):
    expect_msg = "Формат e-mail: username@test.ru"
    email = ""
    if without_local:
        email = "@" + fake.email().split("@")[1]
    elif without_domain:
        email = fake.email().split("@")[0] + "@"
    elif without_delimiter:
        email = fake.email().replace("@", "")
    return email, expect_msg


def generate_negative_password(min_length: Optional[bool] = None, max_length: Optional[bool] = None,
                               only_digits: Optional[bool] = None, only_alpha: Optional[bool] = None):
    expect_msg = "Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры"
    password = ""
    if min_length:
        password = fake.password(length=7, special_chars=True, upper_case=True, lower_case=True,
                                 digits=True)
        expect_msg = "Пароль должен содержать минимум 8 символов"
    elif max_length:
        password = fake.password(length=65, special_chars=True, upper_case=True, lower_case=True,
                                 digits=True)
    elif only_digits:
        password = "".join(random.choice(string.digits) for _ in range(8))
    elif only_alpha:
        password = "".join(random.choice(string.ascii_lowercase) for _ in range(8))
    return password, expect_msg


def generate_negative_referral(min_length: Optional[bool] = None, max_length: Optional[bool] = None):
    expect_msg = "Неверный формат ссылки"
    referral = ""
    if min_length:
        referral = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3))
    elif max_length:
        referral = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(9))
    return referral, expect_msg


