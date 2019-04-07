import os
import pytest
from engine import Finder
from exceptions import TooManyWordsException
from main import main


class TestDistance(object):
    @classmethod
    def setup_class(cls):
        cls.finder = Finder(os.getenv("TEXT_FILE"))

    successful = (
        ('lorem','ipsum', 1,), 
        ('sed', 'elementum', 5,), 
        ('aenean', 'donec', 156,), 
        ('hola', 'mundo', None,), 
    )

    @pytest.mark.parametrize(
        "first_word, final_word, out", 
        successful,
    )
    def test_scenarios(
        self, 
        first_word: str, 
        final_word: str, 
        out: int,
    ) -> None:
        assert self.finder.find_shortest_distance(first_word, final_word) == out

    def test_big_input(self) -> None:
        with pytest.raises(TooManyWordsException):
            main(['Yo', 'We', 'Will', 'Fail'])
    