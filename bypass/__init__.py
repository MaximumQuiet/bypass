#  Copyright 2020, Maxim Kuznetsov.
#  License: Apache License 2.0 (see LICENSE for details).

"""Universal captcha solver for different types of captcha - Google ReCaptcha, image captcha, hCaptcha etc."""

__author__ = "Maxim Kuznetsov"
__version__ = "0.0.1"
__licence__ = "Apache License 2.0"

from abc import ABC, abstractmethod
from dataclasses import dataclass
from io import BytesIO


class RecaptchaBypass(ABC):
    """Bypass for Google reCaptcha."""

    def __init__(self, site_url, site_key) -> None:
        """Default constructor, defines site URL and site key for all implementations."""
        self._site_url = site_url
        self._site_key = site_key

    @abstractmethod
    def bypass(self) -> "BypassSolution":
        """Bypasses Google reCaptcha and returns the solution.

        :return: Google reCaptcha solution
        """
        pass


class TextBypass(ABC):
    """Bypass for simple image with text captcha."""

    @abstractmethod
    def bypass(self, image: BytesIO) -> "BypassSolution":
        """Grabs text from image-text captcha.

        :param image: image-text captcha

        :return: solution with text from the captcha image
        """
        pass


class BypassManager(ABC):
    """Manager for interact with Bypass implementation account"""

    def get_balance(self) -> float:
        """Asks current balance of the Bypass implementation account"""
        pass

    def report(self, solution: "BypassSolution", correct: bool = False) -> None:
        """Reports solution with specified id is valid"""
        pass


@dataclass
class BypassSolution:
    """Holder for Bypass solve result."""

    _id: str
    token: str

    def __post_init__(self) -> None:
        """Solution id and token shouldn't be None, as they comes from bypass providers
        and may contain incorrect values.
        """

        if None in [self._id, self.token]:
            raise ValueError(f"bypass solution should have an id and a token, id: {self._id}, token: {self.token}")