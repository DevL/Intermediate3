import json
import logging
from argparse import ArgumentParser, Namespace
from collections.abc import Iterable
from typing import Optional, Union

LOG_LEVEL = logging.DEBUG

logger = logging.getLogger(__name__)


def main():
    _configure_logging(LOG_LEVEL)
    args = _parse_command_line_args()
    logger.debug(args)

    print("This program has not yet been implemented...")


def _configure_logging(log_level) -> None:
    logging.basicConfig(level=log_level)
    logger.debug("Logging configured.")


def _parse_command_line_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "input_file",
        type=str,
        help="read the contents of this file",
    )
    parser.add_argument(
        "-o",
        "--output-file",
        help="write to this file instead of to the console",
    )
    parser.add_argument(
        "-j", "--json", help="convert the contents to JSON", action="store_true"
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()
