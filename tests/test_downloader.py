"""
Testing for the main downloader class
"""
import asyncio

import aiohttp

import aiodownloader


class TestDownloader:
    """Tests for the Handler class"""

    downloader = aiodownloader.Handler()

    def test_has_loop(self):
        """Tests that the downloader has a asyncio event loop"""
        assert hasattr(self.downloader, '_loop')
        assert isinstance(self.downloader._loop, asyncio.AbstractEventLoop)

    def test_has_session(self):
        """Tests that the downloader has a aiohttp session"""
        assert hasattr(self.downloader, '_session')
        assert isinstance(self.downloader._session, aiohttp.ClientSession)


