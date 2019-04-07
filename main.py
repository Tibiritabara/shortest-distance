"""
Launcher of the project
"""
import os
import sys
import argparse
from typing import List, Optional
from exceptions import TooManyWordsException
from engine import Finder


def main(words: List[str]) -> None:
    """
    :param List[str] words:
    """
    if len(words) > 2:
        raise TooManyWordsException("There should be only two words to search for.")

    finder = Finder(os.getenv("TEXT_FILE"))
    result = finder.find_shortest_distance(words[0], words[1])
    if result:
        print("The shortest distance between the words is: %d" % result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Find the shortest distance between two words in a given text.'
    )
    parser.add_argument(
        'words',
        metavar='W', 
        type=str, 
        nargs='+',
        help='Words to which we are going to find the shortest distance',
    )
    args = parser.parse_args()
    main(args.words)
