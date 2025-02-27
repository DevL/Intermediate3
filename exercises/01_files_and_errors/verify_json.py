import json
import logging
from argparse import ArgumentParser, Namespace

LOG_LEVEL = logging.INFO

logger = logging.getLogger(__name__)


def main():
    _configure_logging(LOG_LEVEL)
    args = _parse_command_line_args()
    logger.debug(args)

    try:
        with open(args.json_file) as f:
            json.load(f)
    except FileNotFoundError:
        print(f"Could not find the file '{args.json_file}'")
    except json.decoder.JSONDecodeError as error:
        print(f"Invalid JSON: {error}")
    else:
        print(f"The file '{args.json_file}' contains valid JSON.")


def _configure_logging(log_level) -> None:
    logging.basicConfig(level=log_level)
    logger.debug("Logging configured.")


def _parse_command_line_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "json_file",
        type=str,
        help="verify the contents of this JSON file",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()
