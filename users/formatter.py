"""
Custom Formats
"""

import re

# Get rid of unwanted characters in name and surname
name_format = '/><=+-?!#"  "$%^&*""()" "_+:;'


# Validate email format
class Email(object):
    email_format = r'[\.\w]{2,}[@]\w+[.]\w+'

    @classmethod
    def validate_email(cls, address):
        address = address.lower().strip()
        return not bool(re.match(cls.email_format, address))
