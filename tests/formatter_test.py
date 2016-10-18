import unittest
from nose_parameterized import parameterized

from users.formatter import Email
class TestEmail(unittest.TestCase):
    @parameterized.expand([
        (
            'churq@hotmail.com',
            False
        ),
        (
            '@hotmail.com',
            True
        ),
        (
            '.@gmail.com',
            True
        ),
        (
            '_churq@hotmail.com',
            True
        ),
        (
            'churq_@hotmail.com',
            True
        ),
        (
            'churq.@hotmail.com',
            True
        ),
        (
            'churq@hotmail.',
            True
        ),
        (
            'churq@hotmail.c',
            True
        ),
        (
            'churq@hotmail.cn',
            False
        ),
        (
            'churqhotmail.com',
            True
        ),
        (
            'churq@hotmailcom',
            True
        )

    ])
    def test_varify_email(self, email_address, result):
        email = Email()
        self.assertEqual(email.validate_email(email_address), result)