import os

import asyncio
import logging
from typing import Optional

import aiohttp


logger = logging.getLogger('aiodownloader')


class Downloader:
    """
    Async file downloader
    """

    def __init__(self,
                 loop: Optional[asyncio.BaseEventLoop]=None,
                 session: Optional[aiohttp.ClientSession]=None):

        self._loop = loop or asyncio.get_event_loop()
        self._session = session or aiohttp.ClientSession(loop=self._loop)

    async def download(self, file_url, save_path='.'):
        async with self._session.get(file_url) as resp:
            if 200 <= resp.status < 300:
                print(resp.headers)
                with open(os.path.join(save_path, file_url)) as file:
                    while True:
                        chunk = await resp.content.read(self._chunk_size)
                        if not chunk:
                            break
                        file.write(chunk)
            else:
                raise aiohttp.errors.HttpProcessingError(
                    message=f'There was a problem processing {file_url}', code=resp.status)

