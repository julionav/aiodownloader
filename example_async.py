"""
Example usage for the downloader in async mode. It shows how to download a single and 
multiple files file with the downloader
"""
import logging
import asyncio

import aiodownloader

logging.basicConfig(level='DEBUG')

async def download_async():

    downloader = aiodownloader.Handler(sync=False)

    # Downloading a file
    await downloader.download('https://media.giphy.com/media/Vuw9m5wXviFIQ/giphy.gif')

    await downloader.download(*[
        'https://www.visualstudio.com/wp-content/uploads/2016/06/python-1-562x309@2x-op.png',
        'https://media.giphy.com/media/Vuw9m5wXviFIQ/giphy.gif',
        'https://cdn-images-1.medium.com/max/800/1*6V7WZZ5rhCWJvRzevnAh5g.png',
    ])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_async())


