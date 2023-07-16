import asyncio

import aiohttp
import pytest

pytest_plugins = "fixtures.api_fixtures"


@pytest.fixture(scope="session")
async def session() -> aiohttp.ClientSession:
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
