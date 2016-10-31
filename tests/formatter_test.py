import unittest
from nose_parameterized import parameterized

from src.formatter import Email


class TestEmail(unittest.TestCase):
    @parameterized.expand([
        (
                'churq@mail.com',
                False
        ),
        (
                '@mail.com',
                True
        ),
        (
                '.@gmail.com',
                True
        ),
        (
                '_churq@mail.com',
                True
        ),
        (
                'churq_@mail.com',
                True
        ),
        (
                'churq.@mail.com',
                True
        ),
        (
                'churq@mail.',
                True
        ),
        (
                'churq@mail.c',
                True
        ),
        (
                'churq@mail.cn',
                False
        ),
        (
                'churqmail.com',
                True
        ),
        (
                'churq@mailcom',
                True
        )

    ])
    def test_verify_email(self, email_address, result):
        email = Email()
        self.assertEqual(email.validate_email(email_address), result)
