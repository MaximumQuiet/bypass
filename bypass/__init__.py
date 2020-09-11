#  Copyright 2020, Maxim Kuznetsov.
#  License: Apache License 2.0 (see LICENSE for details).

"""Universal captcha solver for different types of captcha - Google ReCaptcha, image captcha, hCaptcha etc."""

__author__ = "Maxim Kuznetsov"
__version__ = "0.0.1"
__licence__ = "Apache License 2.0"

from abc import ABC, abstractmethod
from enum import Enum
from io import BytesIO


class ReCaptchaBypass(ABC):
    """Bypass for Google ReCaptcha v2/v3"""

    class ReCaptchaVersion(Enum):
        V2 = "v2"
        V3 = "v3"

    @abstractmethod
    def bypass(
            self, page: str, key: str, version: ReCaptchaVersion = ReCaptchaVersion.V2, invisible: bool = False
    ) -> "BypassSolution":
        """Bypasses Google ReCaptcha v2/v3 and returns the solution

        :param page: a page URL that has ReCaptcha
        :param key: a site private key
        :param version: ReCaptcha version
        :param invisible: is ReCaptcha invisible? (has no interaction with user)
        :return: solution
        """
        pass


class ImageBypass:
    """Bypass for simple image-text captcha"""

    class ImageLanguage(Enum):
        EN = "en"
        RU = "ru"

    @abstractmethod
    def bypass(self, image_stream: BytesIO, lang: ImageLanguage = ImageLanguage.EN) -> "BypassSolution":
        """Grabs text from image-text captcha

        :param image_stream: image-text captcha
        :param lang: text language
        :return: solution
        """
        pass


class BypassSolution:
    """Holder for different Bypass implementation results"""

    def __init__(self, solution_id: str, token: str, manager: "BypassManager") -> None:
        """Base constructor

        :param solution_id: solution id
        :param token: bypass solution - token, text, etc
        :param manager: callback to report captcha is invalid
        """
        self._solution_id = solution_id
        self._token = token
        self._manager = manager

    def report_valid(self) -> None:
        """Reports solution with specified id is valid"""
        self._manager.report_valid(self._solution_id)

    def report_invalid(self) -> None:
        """Reports solution with specified id is invalid"""
        self._manager.report_invalid(self._solution_id)


class BypassManager:
    """Manager for interact with Bypass implementation account"""

    def get_balance(self) -> float:
        """Asks current balance of the Bypass implementation account"""
        pass

    def report_valid(self, solution_id: str) -> None:
        """Reports solution with specified id is valid"""
        pass

    def report_invalid(self, solution_id: str) -> None:
        """Reports solution with specified id is invalid"""
        pass
