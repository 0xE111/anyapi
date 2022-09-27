from dataclasses import dataclass, field
from functools import partialmethod
from logging import getLogger
from pathlib import Path
from typing import ClassVar

import requests
from tenacity import TryAgain, retry, retry_if_exception_type, stop_after_attempt, wait_incrementing

from .cookies import load_cookies

log = getLogger(__name__)


class TooManyIterations(Exception):
    pass


@dataclass
class API:
    session: requests.Session = field(default_factory=requests.Session)
    adapter: requests.adapters.HTTPAdapter = requests.adapters.HTTPAdapter(
        pool_maxsize=8,
    )
    cookies: Path | None = None

    BASE_URL: ClassVar[str]
    TIMEOUT: ClassVar[int] = 10

    def __post_init__(self):
        self.session.mount('http://', self.adapter)
        self.session.mount('https://', self.adapter)
        if self.cookies:
            self.session.cookies = load_cookies(self.cookies)

    @retry(
        reraise=True,
        retry=retry_if_exception_type(TryAgain),
        wait=wait_incrementing(start=1, increment=2),
        stop=stop_after_attempt(20),
    )
    def request(self, method: str, path: str, check: bool = True, **kwargs) -> requests.Response:
        if path.startswith('/'):
            path = self.BASE_URL + path

        kwargs.setdefault('timeout', self.TIMEOUT)
        response = self.session.request(method, path, **kwargs)

        if response.status_code == requests.codes.too_many_requests:
            raise TryAgain()

        if check:
            response.raise_for_status()

        return response

    get = partialmethod(request, 'get')
    post = partialmethod(request, 'post')
