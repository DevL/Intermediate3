import json
import logging
from argparse import ArgumentParser, Namespace
from collections.abc import Iterable
from typing import Optional

LOG_LEVEL = logging.INFO

logger = logging.getLogger(__name__)


def main():
    _configure_logging(LOG_LEVEL)
    args = _parse_command_line_args()
    logger.debug(args)

    with open(args.input_file, "r") as input_file:
        enumerated = _enumerate_lines(input_file)
        _output(enumerated, filename=args.output_file)


def _enumerate_lines(data: Iterable[str]) -> Iterable[str]:
    """
    Enumerates lines of text, prepending each line with its line number.
    """
    return (_format_line(number, line) for number, line in enumerate(data, start=1))


def _format_line(line_number: int, line: str) -> str:
    """
    Prepends a line number to a line of text.

    >>> _format_line(99, "bottles of milk")
    '    99: bottles of milk'
    """
    return f"{line_number:>6}: {line}"


def _output(lines: Iterable[str], filename: Optional[str] = None):
    data = "".join(lines)
    if filename:
        _output_to_file(filename, data)
    else:
        _output_to_console(data)


def _output_to_file(filename: str, data: str) -> None:
    try:
        with open(filename, "w") as output_file:
            output_file.write(data)
    except:
        logger.error(f"Failed to write data to {filename}")
        _output_to_console(data)


def _output_to_console(data: str) -> None:
    print(data)


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
