import logging
import requests
from pprint import pprint
from requests import HTTPError
from argparse import ArgumentParser, Namespace

LOG_LEVEL = logging.INFO
API_BASE_URL = "https://jsonplaceholder.typicode.com"
POSTS_URL = f"{API_BASE_URL}/posts"

logger = logging.getLogger(__name__)


def main():
    _configure_logging(LOG_LEVEL)
    args = _parse_command_line_args()
    logger.debug(args)

    try:
        if args.post_id:
            pprint(_fetch_post_and_maybe_comments(args.post_id, args.with_comments))
        else:
            pprint(_fetch_all_posts())
    except HTTPError as error:
        logger.error(error)


def _fetch_post_and_maybe_comments(post_id: int, with_comments: bool):
    post = _fetch_single_post(post_id)
    if with_comments:
        post["comments"] = _fetch_comments(post_id)
    return post


def _fetch_all_posts():
    return _fetch_data(f"{API_BASE_URL}/posts/")


def _fetch_single_post(post_id: int):
    return _fetch_data(_post_url(post_id))


def _fetch_comments(post_id: int):
    return _fetch_data(_comments_url(post_id))


def _fetch_data(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def _comments_url(post_id):
    return f"{_post_url(post_id)}/comments"


def _post_url(post_id):
    return f"{POSTS_URL}/{post_id}"


def _configure_logging(log_level) -> None:
    logging.basicConfig(level=log_level)
    logger.debug("Logging configured.")


def _parse_command_line_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("-p", "--post-id", help="The id of a single post to fetch.")
    parser.add_argument(
        "-w",
        "--with-comments",
        help="Include comments when fetching a single post.",
        action="store_true",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()
