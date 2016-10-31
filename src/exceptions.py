"""
Custom Exceptions
"""


class DuplicateNameError(Exception):
    pass


class DuplicateSurnameError(Exception):
    pass


class IsNotLegalEmailFormatError(Exception):
    pass


class DuplicateEmailError(Exception):
    pass


class WrongFileNameError(Exception):
    pass


class CouldNotReadFileError(Exception):
    pass


class CouldNotFormatNameError(Exception):
    pass


class CouldNotFormatSurnameError(Exception):
    pass


class CouldNotFormatEmailError(Exception):
    pass


class CouldNotFormatDataError(Exception):
    pass


class CouldNotGetDataError(Exception):
    pass
