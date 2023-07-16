from dataclasses import dataclass

import aiohttp
import pytest
from multidict import CIMultiDictProxy


@dataclass
class HTTPResponse:
    body: dict
    headers: CIMultiDictProxy[str]
    status: int


@pytest.fixture
async def make_get_request(session):
    async def inner(target: str, **kwargs) -> HTTPResponse:
        url = f"http://nginx/api/v1{target}"
        async with session.get(url, **kwargs) as response:
            return HTTPResponse(
                body=await response.json(),
                headers=response.headers,
                status=response.status,
            )

    return inner


@pytest.fixture
async def make_post_request(session):
    async def inner(target: str, **kwargs) -> HTTPResponse:
        url = f"http://nginx/api/v1{target}"
        async with session.post(url, **kwargs) as response:
            return HTTPResponse(
                body=await response.json(),
                headers=response.headers,
                status=response.status,
            )

    return inner


@pytest.fixture
async def make_send_file_request(session):
    async def inner(target: str, file_path) -> HTTPResponse:
        url = f"http://nginx/api/v1{target}"
        form = aiohttp.FormData()
        form.add_field("file", open(file_path, "rb"))
        async with session.post(url, data=form) as response:
            return HTTPResponse(
                body=await response.json(),
                headers=response.headers,
                status=response.status,
            )

    return inner
