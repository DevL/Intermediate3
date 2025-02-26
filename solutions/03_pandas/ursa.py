import json
import logging
from argparse import ArgumentParser, Namespace
from api import PlaceHolderAPI
from pandas import DataFrame, set_option
from pprint import pprint
from typing import Optional

LOG_LEVEL = logging.INFO

logger = logging.getLogger(__name__)


def main():
    _configure_logging(LOG_LEVEL)
    args = _parse_command_line_args()
    _configure_pandas(args.no_truncation)
    _output(
        dataframe=_merge_data(*_fetch_data()),
        filename=args.file,
    )


def _fetch_data():
    """
    Retrieves posts and users from the API.
    """
    api = PlaceHolderAPI()
    posts = DataFrame(api.posts())
    users = DataFrame(api.users())
    return posts, users


def _merge_data(posts, users):
    """
    Merges posts and users without duplicate columns.
    """
    posts_and_users = posts.merge(users, left_on="userId", right_on="id")
    posts_and_users.rename(columns={"id_x": "postId"}, inplace=True)
    posts_and_users.drop(columns="id_y", inplace=True)
    return posts_and_users


def _output(dataframe: DataFrame, filename: Optional[str]):
    """
    Outputs JSON to the console or optionally to a file.
    """
    formatted = dataframe.to_json(orient="records")

    if filename:
        logger.debug(f"Writing JSON to {filename}")
        with open(filename, "w") as f:
            f.write(formatted)
    else:
        pprint(json.loads(formatted))


def _configure_logging(log_level) -> None:
    logging.basicConfig(level=log_level)
    logger.debug("Logging configured.")


def _configure_pandas(no_truncation: bool):
    if no_truncation:
        set_option("display.max_rows", None)
        set_option("display.max_columns", None)
        set_option("display.width", None)
        set_option("display.max_colwidth", None)
        logger.debug("Disabling Pandas' truncation of DataFrames.")
    else:
        logger.debug("Using standard Pandas settings.")


def _parse_command_line_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        help="Write to this file instead of to the console.",
    )
    parser.add_argument(
        "-t",
        "--no-truncation",
        help="Do not truncate columns and rows when printing a DataFrame.",
        action="store_true",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()
