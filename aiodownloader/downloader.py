import os

import asyncio
import logging
from typing import Optional

import aiohttp
import aiofiles
from tqdm import tqdm

logger = logging.getLogger('aiodownloader')


class Downloader:
    """
    Async file downloader
    """

    def __init__(self,
                 loop: Optional[asyncio.BaseEventLoop]=None,
                 session: Optional[aiohttp.ClientSession]=None,
                 chunk_size: Optional[int]=None):

        self._loop = loop or asyncio.get_event_loop()
        self._session = session or aiohttp.ClientSession(loop=self._loop)
        self._chunk_size = chunk_size or 1024

    def _progress_bar(self, length: int, file_name: str):
        """
        Progress bar for the downloads made using tqdm. It works using a generator. Everytime 
        that a chunk of the file is downloaded it can call the next function on the progress 
        bar to make it advance. It sets the total length of the bar equal to the content_length.
        And the updates are done with the predefined chunk size of the class.
        """
        with tqdm(total=length, desc=file_name, unit_scale=True, unit='B') as pbar:
            while True:
                yield
                pbar.update(self._chunk_size)

    async def download_bulk(self,
                            files_url: list[str],
                            save_path: Optional[str]=None):
        """
        Dowloads a bulk of files from the given list of urls to the given path.
        
        :param files_url: list of urls where the files are located
        :param save_path: path to be used for saving the files. Defaults to the current dir
        :return: 
        """

    async def download(self, file_url: str,
                       save_path: Optional[str]=None,
                       file_name: Optional[str]=None):
        """
        Downloads a file from the given url to a file to the given path.
        
        :param file_url: the url where the file is located 
        :param save_path: path to be used for saving the file. Defaults to the current dir
        :param file_name: file name to be used when saving the file. Defaults to the end of the 
        url
        :return: 
        """

        file_name = file_name or file_url.split('/')[~0]
        file_path = os.path.join(save_path, file_name) if save_path else file_name

        async with self._session.get(file_url) as resp:
            if 200 <= resp.status < 300:
                async with aiofiles.open(file_path, 'wb') as file:
                    # Starting progress bar
                    pbar = self._progress_bar(length=int(resp.headers['Content-Length']),
                                              file_name=file_name)

                    # Downloading the file using the aiohttp.StreamReader
                    async for data in resp.content.iter_chunked(self._chunk_size):
                        await file.write(data)
                        next(pbar)
            else:
                raise aiohttp.errors.HttpProcessingError(
                    message=f'There was a problem processing {file_url}', code=resp.status)
