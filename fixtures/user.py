from random import choice, randint
from faker import Faker
from data.models import User
import string
import pytest

fake = Faker()



@pytest.fixture
def user():
    return User(username=''.join(choice(string.ascii_lowercase)) +
                         ''.join(choice(string.ascii_lowercase + string.digits) for _ in range(10)),
                email=fake.email(),
                password=fake.password(length=8, special_chars=True, upper_case=True, lower_case=True, digits=True),
                referral=''.join(
                    choice(string.ascii_lowercase + string.digits) for _ in range(randint(4, 8))))