"""
Custom Formats
"""

import re

# Get rid of unwanted characters in name and surname
name_format = '/><=+-?!#"  "$%^&*""()" "_+:;'


# Validate email format
class Email(object):
    email_format = r'[a-z][a-z_\.0-9]{1,}[a-z0-9]@[a-z\.]+\.[a-z]{2,}$'
    email_f = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'

    @classmethod
    def validate_email(self, address):
        address = address.lower().strip()
        return not bool(re.match(self.email_format, address))
