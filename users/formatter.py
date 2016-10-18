"""
Custom Formats
"""

import re

# Get rid of unwanted characters in name and surname
name_format = '/><=+-?!#"  "$%^&*""()" "_+:;'

# Validate email format
email_format = "[\.\w]{2,}[@]\w+[.]\w+"
email_f = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'


def validate_email(address):
    if re.match(email_format, address):
        return False
    else:
        return True
