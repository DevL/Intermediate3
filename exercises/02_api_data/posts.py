import logging
from argparse import ArgumentParser, Namespace

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
    parser.add_argument("-p", "--post_id", help="The id of a single post to fetch.")
    return parser.parse_args()


if __name__ == "__main__":
    main()
