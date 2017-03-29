"""
Testing for the main downloader class
"""
import asyncio

import aiohttp

from aiodownloader import Downloader


class TestDownloader:
    """Tests for the Downloader class"""

    downloader = Downloader()

    def test_has_loop(self):
        """Tests that the downloader has a asyncio event loop"""
        assert hasattr(self.downloader, '_loop')
        assert isinstance(self.downloader._loop, asyncio.AbstractEventLoop)

    def test_has_session(self):
        """Tests that the downloader has a aiohttp session"""
        assert hasattr(self.downloader, '_session')
        assert isinstance(self.downloader._session, aiohttp.ClientSession)