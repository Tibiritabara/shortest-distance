import os
import sys
import argparse
from typing import List, Optional


def main(words: List[str]) -> Optional[int]:
    pass


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
    main(args)
