#  Copyright 2020, Maxim Kuznetsov.
#  License: Apache License 2.0 (see LICENSE for details).

from unittest import TestCase

import pytest

from bypass import BypassSolution, BypassManager


class TestBypassSolution(TestCase):
    def test_raises_when_id_none(self):
        with pytest.raises(ValueError):
            BypassSolution(None, "token")

    def test_raises_when_token_none(self):
        with pytest.raises(ValueError):
            BypassSolution("id", None)
