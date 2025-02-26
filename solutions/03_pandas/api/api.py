import logging
from requests import HTTPError, Session

logger = logging.getLogger(__name__)

API_BASE_URL = "https://jsonplaceholder.typicode.com"


class PlaceHolderAPI:
    def __init__(self, session=None):
        self.session = session or Session()

    def posts(self):
        return self._get(f"{API_BASE_URL}/posts/")

    def users(self):
        return self._get(f"{API_BASE_URL}/users/")

    def _get(self, url: str):
        logger.debug(f"Making a GET request to {repr(url)}.")
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except HTTPError as error:
            logger.error(error)
            exit(1)
