"""
Set of methods and classes to execute the text operations.
"""
import logging
from typing import List, Optional


logger = logging.getLogger(__name__)


class Finder:
    """
    Class that handles the text operations.
    """
    def __init__(self, filename: str) -> None:
        """
        :param str filename:
        """
        self.filename = filename

    def find_shortest_distance(
        self, 
        first_word: str, 
        final_word: str,
        ) -> Optional[int]:
        """
        Retrieve the shortest distance between the given words.
        :param str first_word:
        :param str final_word:
        :return int:
        """
        word_list = self.__get_text()
        if first_word in word_list and final_word in word_list:
            return abs(
                word_list.index(first_word.lower()) - word_list.index(final_word.lower())
            )
        logger.error(
            "The selected words do not exist: %s, %s" %
            (first_word, final_word)
        )
        return None

    def __get_text(self) -> List[str]:
        """
        Retrieve and split the text
        :return List[str]:
        """
        textfile = open(self.filename, "r")
        text: str = textfile.read()
        textfile.close()
        word_list: List = text.lower().split()
        return word_list
